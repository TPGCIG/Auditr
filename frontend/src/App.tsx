import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import AssignmentPDFInput from './components/AssignmentPDFInput';

const Home: React.FC = () => {
  return (
        <div className="App bg-gray-800  min-h-screen">
          <h1 className='text-white text-center text-3xl font-bold tracking-tight'>Upload</h1>
          <AssignmentPDFInput />
        </div>
    )
}

const Review: React.FC = () => {
  return (
    <div>
      <h1>Review Panel</h1>
    </div>
  )
}

const NotFound: React.FC = () => {
	return (
		<div>
			<h1>404!</h1>
		</div>
	)
}

const App: React.FC = () => {
    return (
    	<Router>
        	<nav>
            	<Link to="/">Home</Link> |{" "}
            	<Link to="/review">Review</Link> |{" "}
          	</nav>

		<Routes>
			<Route path="/" element={<Home />} />
			<Route path="/review" element={<Review />} />
			<Route path="*" element={<NotFound />} />
			</Routes>
		</Router>
    )
}

export default App
