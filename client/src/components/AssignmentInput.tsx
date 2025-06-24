import React, { useState } from 'react';

const AssignmentInput: React.FC = () => {
  const [value, setValue] = useState<string>('');

  return (
    <div>
      <input
        className="h-full w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Insert assignment here..."
      />
      <p>You typed: {value}</p>
    </div>
  );
};

export default AssignmentInput;

