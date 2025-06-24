import React, { useState } from 'react';

const AssignmentPDFInput : React.FC = () => {
    const [file, setFile] = useState<File | null>(null);

    const handleChange: React.ChangeEventHandler<HTMLInputElement> = (event) => {
        const selectedFile = event.target.files?.[0] || null;
        setFile(selectedFile);
    };

    const handleSubmit = async (event : React.FormEvent<HTMLFormElement>): Promise<void> => {
        event.preventDefault();

        if (!file) {
            alert("No file submitted!");
            return;
        }

        const formData = new FormData()
        formData.append('file', file);

        try {
            const response = await fetch('http://localhost:5000/api/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            alert(data.message);
        } catch (err) {
            console.error(err);
            alert("Error uploading file!");
        }
    };

        return (
            <form onSubmit={handleSubmit} className="p-4">
                <div className="flex items-center space-x-4 mb-4">
                    <input
                        type="file"
                        id="file-upload"
                        onChange={handleChange}
                        className="hidden"
                    />
                    <label
                        htmlFor="file-upload"
                        className="cursor-pointer bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded"
                    >
                        Choose File
                    </label>
                    {/* Show selected file name or fallback */}
                    <span className="text-white">{file ? file.name : "No file chosen"}</span>
                    </div>
                <button type="submit" className="cursor-pointer font-semibold bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded">
                    Upload
                </button>
            </form>
        );
    };

    export default AssignmentPDFInput