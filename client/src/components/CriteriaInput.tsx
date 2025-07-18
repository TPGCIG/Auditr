import React, { useState } from 'react';

const CriteriaInput: React.FC = () => {
  const [value, setValue] = useState<string>('');

  return (
    <div>
      <label>
            Copy-Paste your Criteria here:
            <textarea
                className="w-full h-32 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
                placeholder="Enter your criteria here..."
            ></textarea>


            </label>
    </div>
  );
};

export default CriteriaInput;
