import React, { useState } from 'react';

const TextInputExample: React.FC = () => {
  const [value, setValue] = useState<string>('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };

  return (
    <div>
      <label htmlFor="myInput">Enter text:</label>
      <input
        id="myInput"
        type="text"
        value={value}
        onChange={handleChange}
        placeholder="Type something..."
      />
      <p>You typed: {value}</p>
    </div>
  );
};

export default TextInputExample;

