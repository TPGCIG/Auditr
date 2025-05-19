import React, { useState } from 'react'

const TreeNode = {{ node }} => {
  const [isOpen, setIsOpen] = useState(false);
  const hasChildren = node.children?.length > 0;


  return (
    <div className="pl-2"> 
      <div
        className="cursor-pointer flex items-center hover:bg-gray-200 p-1 rounded"
        onClick={() => hasChildren && setIsOpen(!isOpen)}
      >
        {hasChildren && (
          <span className="mr-1">
            {isOpen ? '📂' : '📁' }
          </span>
        )}
        {!hasChildren && <span className="mr-1">📄</span>}
        {node.name}
      </div>

      {hasChildren && isOpen && (
        <div className="ml-4 border-l border-gray-300 pl-2">
          {node.children.map((child, i) => (
            <TreeNode key={i} node={child} />
          ))}
        </div>
      )}
    </div>
  );
};

const Sidebar = ({ data }) => {
  return (
    <div className="w-64 h-screen bg-gray-100 overflow-y-auto p-2 border-r">
      {data.map((node, i) => (
        <TreeNode key={i} node={node} />
      ))}
    </div>
  );
};

export default Sidebar;
