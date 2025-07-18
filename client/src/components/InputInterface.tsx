import React, { useState } from 'react';
import './TaskInput'
import './CriteriaInput'
import './AssignmentInput'
import './InputInterface.css'
import TaskInput from './TaskInput';
import CriteriaInput from './CriteriaInput';
import AssignmentInput from './AssignmentInput';

const InputInterface: React.FC = () => {
    return (
        <div className="grid-container">
            <div className="item1"><TaskInput/></div>
            <div className="item2"><CriteriaInput/></div>
            <div className="item3"><AssignmentInput/></div>  

        </div>
    )





}

export default InputInterface