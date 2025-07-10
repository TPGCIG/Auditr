import React from 'react';


const TaskInput: React.FC = () => {

    return (
        <div>
            <label>
                Copy-Paste your task here:
                <textarea
                    className="w-full h-32 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
                    placeholder="Enter your task description here..."
                ></textarea>


            </label>


        </div>



    )



}

export default TaskInput;