import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import AssignmentPDFInput from './components/AssignmentPDFInput';
import InputInterface from './components/InputInterface';
import './App.css';
import './index.css'
import TestComponent from './components/TestComponent';

const Home: React.FC = () => {
  return (
        <div className="App  min-h-screen">
			<InputInterface/>
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
