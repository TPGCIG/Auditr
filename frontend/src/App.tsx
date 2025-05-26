import React from 'react'
import AssignmentInput from './components/AssignmentInput'
import AssignmentPDFInput from './components/AssignmentPDFInput'

const App: React.FC = () => {
    return (
        <div className="App bg-gray-800  min-h-screen">
          <h1 className='text-white text-center text-3xl font-bold tracking-tight'>Upload your assignment here!</h1>
          <AssignmentPDFInput />
        </div>
    )
}

export default App
