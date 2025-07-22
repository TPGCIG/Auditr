import React, { useState } from 'react';
import './InputInterface.css'

const InputInterface: React.FC = () => {

    const [fields, setFields] = useState({
        task: '',
        criteria: '',
        assignment: ''
    })

    
    const handleSubmit = async (e: React.FormEvent) => {
            e.preventDefault()

            const payload = {
                task: fields.task,
                assignment: fields.assignment,
                criteria: fields.criteria
            }

            try {
                const response = await fetch('http://localhost:8000/api/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    throw new Error('Failed to submit');
                }

                const result = await response.json();
                console.log('Response'+result)

            } catch (error) {
                console.log(error)
            }
    }


    return (
        <form onSubmit={handleSubmit}>
            <div className="grid-container">
                <div className="item1">
                    <div>
                        <label>
                            Copy-Paste your task here:
                            <textarea
                                className="w-full h-32 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
                                onChange={e => {
                                    setFields({
                                        ...fields, 
                                        task: e.target.value
                                    });
                                }}
                                value={fields.task}
                                placeholder="Enter your task description here..."
                            ></textarea>
                        </label>
                    </div>
                </div>
                <div className="item2">
                    <div>
                        <label>
                            Copy-Paste your Criteria here:
                            <textarea
                                className="w-full h-32 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
                                placeholder="Enter your criteria here..."
                                value={fields.criteria}
                                onChange={e => {
                                    setFields({
                                        ...fields,
                                        criteria: e.target.value
                                    });
                                }}
                            ></textarea>
                        </label>
                    </div>
                </div>
                <div className="item3">
                    <div>
                        <textarea
                            className="h-full w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            value={fields.assignment}
                            onChange={e => {
                                setFields({
                                    ...fields,
                                    assignment: e.target.value
                                });
                            }}
                            placeholder="Insert assignment here..."
                        ></textarea>
                    </div>      
                </div>  
                <button 
                    type='submit'
                    className='bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 btn-submit'
                >
                    Submit
                </button>
            </div>
        </form>
    )





}

export default InputInterface