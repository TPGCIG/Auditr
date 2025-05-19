import React, { useState, createContext, useContext, useCallback } from 'react';
import {
  FaFolder,
  FaFolderOpen,
  FaBookOpen,
  FaFilePdf,
  FaVideo,
  FaChevronRight,
  FaChevronDown,
  FaRegFileAlt, // Generic file as fallback
  FaBook, // Alternative for class or subject
} from 'react-icons/fa';
import { VscCollapseAll } from 'react-icons/vsc'; // VS Code like icon for collapse

// 1. Define the Data Structure for LMS Nodes
// -----------------------------------------------------------------------------
export interface LmsNodeData {
  id: string;
  name: string;
  type: 'root' | 'class' | 'folder' | 'textbook' | 'pdf' | 'video' | 'document';
  children?: LmsNodeData[];
  resourceUrl?: string; // URL to the actual resource, e.g., a PDF or video link
}

// 2. Example Data for the LMS
// -----------------------------------------------------------------------------
const lmsStructure: LmsNodeData[] = [
  {
    id: 'class-math101',
    name: 'Mathematics 101',
    type: 'class',
    children: [
      {
        id: 'math101-folder-syllabus',
        name: 'Course Information',
        type: 'folder',
        children: [
          { id: 'math101-doc-syllabus', name: 'Syllabus.pdf', type: 'pdf', resourceUrl: '/path/to/syllabus.pdf' },
          { id: 'math101-doc-schedule', name: 'Course Schedule.pdf', type: 'pdf', resourceUrl: '/path/to/schedule.pdf' },
        ],
      },
      {
        id: 'math101-folder-week1',
        name: 'Week 1: Introduction to Algebra',
        type: 'folder',
        children: [
          { id: 'math101-textbook-algebra', name: 'Algebra Fundamentals (Ch 1-2)', type: 'textbook', resourceUrl: '/path/to/algebra/ch1-2' },
          { id: 'math101-video-intro', name: 'Introductory Video', type: 'video', resourceUrl: '/path/to/intro-video.mp4' },
        ],
      },
      {
        id: 'math101-folder-assignments',
        name: 'Assignments',
        type: 'folder',
        children: [
          { id: 'math101-doc-hw1', name: 'Homework 1.pdf', type: 'pdf', resourceUrl: '/path/to/hw1.pdf' },
        ],
      },
    ],
  },
  {
    id: 'class-hist202',
    name: 'World History: Ancient Civilizations',
    type: 'class',
    children: [
      {
        id: 'hist202-folder-resources',
        name: 'Core Textbooks & Readings',
        type: 'folder',
        children: [
          { id: 'hist202-textbook-main', name: 'Echoes of the Past (Full Text)', type: 'textbook', resourceUrl: '/path/to/history-textbook' },
          { id: 'hist202-pdf-egypt', name: 'Ancient Egypt Overview.pdf', type: 'pdf', resourceUrl: '/path/to/egypt.pdf' },
        ],
      },
      { id: 'hist202-video-rome', name: 'The Rise of Rome (Lecture)', type: 'video', resourceUrl: '/path/to/rome-lecture.mp4' },
    ],
  },
  {
    id: 'class-sci300',
    name: 'Introduction to Biology',
    type: 'class',
    children: [
        // This class is initially empty or has no sub-folders shown by default
    ]
  }
];

// 3. Context for Managing Expanded State (for "Collapse All")
// -----------------------------------------------------------------------------
interface ExpansionContextType {
  expandedNodes: Set<string>;
  toggleNode: (nodeId: string) => void;
  expandAll: () => void;
  collapseAll: () => void;
  isExpanded: (nodeId: string) => boolean;
}

const ExpansionContext = createContext<ExpansionContextType | undefined>(undefined);

const useExpansion = () => {
  const context = useContext(ExpansionContext);
  if (!context) {
    throw new Error('useExpansion must be used within an ExpansionProvider');
  }
  return context;
};

// Props for ExpansionProvider, explicitly defining children and allNodeIds
interface ExpansionProviderProps {
  children: React.ReactNode;
  allNodeIds: string[]; // Though not directly used by expandAll/collapseAll in this version, good for context
  initialData: LmsNodeData[]; // Pass initial data for expandAll to reference
}

const ExpansionProvider: React.FC<ExpansionProviderProps> = ({ children, initialData }) => {
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set());

  const toggleNode = useCallback((nodeId: string) => {
    setExpandedNodes(prev => {
      const newSet = new Set(prev);
      if (newSet.has(nodeId)) {
        newSet.delete(nodeId);
      } else {
        newSet.add(nodeId);
      }
      return newSet;
    });
  }, []);

  const expandAll = useCallback(() => {
    const expandableNodeIds = new Set<string>();
    // Recursive function to find all nodes that have children
    function findExpandable(nodes: LmsNodeData[]) {
        nodes.forEach(node => {
            if (node.children && node.children.length > 0) {
                expandableNodeIds.add(node.id);
                // Recursively call for children to expand nested folders/classes
                findExpandable(node.children);
            }
        });
    }
    findExpandable(initialData); // Use initialData passed as prop
    setExpandedNodes(expandableNodeIds);
  }, [initialData]);


  const collapseAll = useCallback(() => {
    setExpandedNodes(new Set());
  }, []);

  const isExpanded = useCallback((nodeId: string) => expandedNodes.has(nodeId), [expandedNodes]);

  return (
    <ExpansionContext.Provider value={{ expandedNodes, toggleNode, expandAll, collapseAll, isExpanded }}>
      {children}
    </ExpansionContext.Provider>
  );
};

// Helper to get all node IDs - can be useful for other purposes, not strictly needed for ExpansionProvider as refactored
// const getAllNodeIds = (nodes: LmsNodeData[]): string[] => {
//   let ids: string[] = [];
//   nodes.forEach(node => {
//     ids.push(node.id);
//     if (node.children) {
//       ids = ids.concat(getAllNodeIds(node.children));
//     }
//   });
//   return ids;
// };


// 4. Resource Node Component (Recursive)
// -----------------------------------------------------------------------------
interface LmsNodeProps {
  node: LmsNodeData;
  level?: number;
  onResourceSelect: (node: LmsNodeData) => void;
  selectedResourceId?: string | null;
}

const LmsNode: React.FC<LmsNodeProps> = ({ node, level = 0, onResourceSelect, selectedResourceId }) => {
  const { isExpanded, toggleNode } = useExpansion();
  const isOpen = isExpanded(node.id);

  const hasChildren = node.children && node.children.length > 0;
  // A resource is selectable if it's not a folder/class OR if it's an empty folder/class (user might want to select it to see an "empty" message)
  // For this example, we only make non-container types selectable.
  const isSelectableResource = node.type !== 'folder' && node.type !== 'class';

  const handleToggle = (e: React.MouseEvent) => {
    e.stopPropagation(); // Prevent click from bubbling to parent div if chevron is clicked
    if (hasChildren) {
      toggleNode(node.id);
    }
  };

  const handleNodeClick = () => {
    if (hasChildren) { // If it's a folder/class with children, toggle it
      toggleNode(node.id);
    }
    // Allow selecting any node type if needed, or restrict as per isSelectableResource
    // For this version, we call onResourceSelect for any node type if it doesn't have children,
    // or if it's a resource type even if it accidentally has children (data error).
    if (isSelectableResource) {
      onResourceSelect(node);
    } else if (!hasChildren && (node.type === 'folder' || node.type === 'class')) {
      // Optionally, handle clicks on empty folders/classes if needed
      // onResourceSelect(node); // Or a different handler for empty containers
    }
  };


  const getIcon = () => {
    // Returns the appropriate icon based on the node type
    switch (node.type) {
      case 'class':
        return <FaBook className="mr-2 text-blue-400 flex-shrink-0" aria-hidden="true" />;
      case 'folder':
        return isOpen ?
               <FaFolderOpen className="mr-2 text-yellow-500 flex-shrink-0" aria-hidden="true" /> :
               <FaFolder className="mr-2 text-yellow-500 flex-shrink-0" aria-hidden="true" />;
      case 'textbook':
        return <FaBookOpen className="mr-2 text-green-500 flex-shrink-0" aria-hidden="true" />;
      case 'pdf':
        return <FaFilePdf className="mr-2 text-red-500 flex-shrink-0" aria-hidden="true" />;
      case 'video':
        return <FaVideo className="mr-2 text-purple-500 flex-shrink-0" aria-hidden="true" />;
      case 'document':
        return <FaRegFileAlt className="mr-2 text-gray-400 flex-shrink-0" aria-hidden="true" />;
      default:
        return <FaRegFileAlt className="mr-2 text-gray-400 flex-shrink-0" aria-hidden="true" />;
    }
  };

  // Calculate padding for indentation. Non-children nodes get extra padding to align text.
  const indentStyle = { paddingLeft: `${level * 20 + (hasChildren ? 0 : 24)}px` };
  const isSelected = selectedResourceId === node.id;

  return (
    <div className="text-sm font-medium">
      {/* Clickable area for the node item */}
      <div
        className={`flex items-center py-1.5 px-2 cursor-pointer rounded-md transition-colors duration-150 ease-in-out
                    ${isSelected ? 'bg-blue-600 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
        style={indentStyle}
        onClick={handleNodeClick}
        onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') handleNodeClick();}} // Accessibility: allow keyboard interaction
        tabIndex={0} // Make it focusable
        role="treeitem" // ARIA role
        aria-selected={isSelected}
        aria-expanded={hasChildren ? isOpen : undefined} // aria-expanded only for nodes with children
        title={node.name}
      >
        {/* Chevron icon for expandable nodes */}
        {hasChildren ? (
          <span
            onClick={handleToggle}
            onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') handleToggle(e);}} // Accessibility
            className="mr-1 p-0.5 hover:bg-gray-600 rounded focus:outline-none focus:ring-1 focus:ring-blue-500"
            tabIndex={0} // Make chevron focusable separately if desired, or rely on parent
            aria-hidden="true" // Chevron is presentational for screen readers if parent has aria-expanded
          >
            {isOpen ? <FaChevronDown size="0.8em" /> : <FaChevronRight size="0.8em" />}
          </span>
        ) : (
          // Placeholder for alignment when there's no chevron
          <span className="mr-1 w-[calc(0.8em+4px)] flex-shrink-0" aria-hidden="true"></span>
        )}
        {/* Node type icon */}
        {getIcon()}
        {/* Node name, truncated if too long */}
        <span className="truncate" style={{maxWidth: `calc(100% - ${level * 20 + 60}px)`}}>{node.name}</span>
      </div>

      {/* Recursive rendering of children if the node is open and has children */}
      {hasChildren && isOpen && (
        <div role="group" className="border-l border-gray-600 ml-[calc(0.8em+4px+8px)]"> {/* Adjusted margin for visual alignment */}
          {node.children?.map((childNode) => (
            <LmsNode
              key={childNode.id}
              node={childNode}
              level={level + 1}
              onResourceSelect={onResourceSelect}
              selectedResourceId={selectedResourceId}
            />
          ))}
        </div>
      )}
    </div>
  );
};

// 5. Main LMS Navigator Component
// -----------------------------------------------------------------------------
interface LmsNavigatorProps {
  title?: string;
  data: LmsNodeData[];
  onResourceSelect: (node: LmsNodeData) => void;
  selectedResourceId?: string | null;
}

const LmsNavigator: React.FC<LmsNavigatorProps> = ({ title = "RESOURCES", data, onResourceSelect, selectedResourceId }) => {
  const { collapseAll, expandAll } = useExpansion();
  return (
    <div className="w-full sm:w-72 md:w-80 h-full bg-gray-800 text-gray-300 flex flex-col select-none rounded-lg shadow-lg" role="navigation" aria-label={title}>
      {/* Header section with title and control buttons */}
      <div className="p-3 flex justify-between items-center border-b border-gray-700">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-gray-400" id="lms-navigator-title">{title}</h2>
        <div className="flex space-x-1">
          <button
            onClick={expandAll}
            title="Expand All Folders"
            className="p-1.5 hover:bg-gray-600 rounded hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-blue-500"
            aria-label="Expand All Folders"
          >
            <FaChevronDown size={16} /> {/* Using a generic expand icon */}
          </button>
          <button
            onClick={collapseAll}
            title="Collapse All Folders"
            className="p-1.5 hover:bg-gray-600 rounded hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-blue-500"
            aria-label="Collapse All Folders"
          >
            <VscCollapseAll size={16} />
          </button>
        </div>
      </div>

      {/* Tree View Area - scrollable */}
      <div className="flex-grow overflow-y-auto p-2 space-y-0.5" role="tree" aria-labelledby="lms-navigator-title">
        {data.map((node) => (
          <LmsNode
            key={node.id}
            node={node}
            onResourceSelect={onResourceSelect}
            selectedResourceId={selectedResourceId}
            level={0} // Explicitly set initial level
          />
        ))}
      </div>
    </div>
  );
};


// 6. Main App Component (Example Usage)
// -----------------------------------------------------------------------------
const App: React.FC = () => {
  const [selectedResource, setSelectedResource] = useState<LmsNodeData | null>(null);
  const [contentTitle, setContentTitle] = useState<string>("Welcome to the LMS!");
  const [contentText, setContentText] = useState<string>("Please select a resource from the course navigator to view its details or open it.");

  // const allNodeIds = getAllNodeIds(lmsStructure); // Not strictly needed for provider if initialData is passed

  const handleResourceSelection = (node: LmsNodeData) => {
    console.log('Selected Resource:', node);
    setSelectedResource(node);
    setContentTitle(`${node.type.charAt(0).toUpperCase() + node.type.slice(1)}: ${node.name}`);
    if (node.resourceUrl) {
      setContentText(`You have selected "${node.name}". Click the button below to open the resource.`);
    } else if (node.children && node.children.length > 0) {
      setContentText(`You have selected the container "${node.name}". Expand it to see its contents.`);
    }
     else {
      setContentText(`You have selected "${node.name}". This item does not have a direct resource URL or further content to display here.`);
    }
  };

  return (
    // Pass lmsStructure to ExpansionProvider for the expandAll functionality
    <ExpansionProvider allNodeIds={[]} initialData={lmsStructure}>
      <div className="flex flex-col sm:flex-row h-screen bg-gray-900 font-sans antialiased">
        {/* Sidebar for the LMS Navigator */}
        <aside className="w-full sm:w-72 md:w-80 p-2 sm:p-3 flex-shrink-0 bg-gray-850 sm:h-full sm:overflow-y-auto">
            <LmsNavigator
            title="COURSE NAVIGATOR"
            data={lmsStructure} // Main data for the navigator
            onResourceSelect={handleResourceSelection}
            selectedResourceId={selectedResource?.id}
            />
        </aside>

        {/* Main content area */}
        <main className="flex-grow p-4 sm:p-6 md:p-8 text-white overflow-y-auto">
          <div className="bg-gray-800 p-6 rounded-lg shadow-xl min-h-[200px]">
            <h1 className="text-xl sm:text-2xl font-semibold mb-4 text-blue-400">{contentTitle}</h1>
            <p className="text-gray-300 leading-relaxed">{contentText}</p>

            {/* Button to open the resource if a URL exists */}
            {selectedResource && selectedResource.resourceUrl && (
              <div className="mt-6">
                <a
                  href={selectedResource.resourceUrl}
                  target="_blank" // Open in a new tab
                  rel="noopener noreferrer" // Security best practice for target="_blank"
                  className="inline-flex items-center bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors duration-150 ease-in-out shadow hover:shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-blue-400"
                >
                  <FaBookOpen className="mr-2" /> Open Resource: {selectedResource.name}
                </a>
              </div>
            )}

            {/* Optional: Display raw selected data for debugging/demonstration */}
             {selectedResource && (
                <div className="mt-8 p-4 bg-gray-700 rounded-md shadow">
                    <h3 className="text-md font-semibold text-gray-200 mb-2">Developer Info: Selected Item Data</h3>
                    <pre className="text-xs text-gray-400 whitespace-pre-wrap bg-gray-750 p-3 rounded-sm overflow-x-auto">
                        {JSON.stringify(selectedResource, null, 2)}
                    </pre>
                </div>
            )}
          </div>
        </main>
      </div>
    </ExpansionProvider>
  );
};

export default App;

