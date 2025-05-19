const fileTree = [
  {
    name: "src",
    type: "folder",
    children: [
      { name: "App.js", type: "file" },
      { name: "index.js", type: "file" },
      {
        name: "components",
        type: "folder",
        children: [
          { name: "Sidebar.js", type: "file" },
        ]
      }
    ]
  },
  { name: "package.json", type: "file" }
];

export default fileTree;
