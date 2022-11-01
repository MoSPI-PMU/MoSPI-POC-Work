import React from "react";
import './main.css';
import Filter from './Filter';
import DenseTable from "./DenseTable";
import BharatSarkarLogo from './BharatSarkar.png';

const Main = () => {
    
    return (
        
        <div className='container'>
     
                <div className='left'>
                    <div>&nbsp;</div>
                    <h3>&nbsp;Common dimensions
                        
                        <Filter /> 
                        <Filter />
                    </h3>
                
                </div>
        
                <div className='right'>
                    <img  src={BharatSarkarLogo} style={{ float: 'left', width: '50px' }} />
                    
                    <div>&nbsp;</div>
                    <h3 style={{color:"#000066", margin:"0px"}}>&nbsp;&nbsp;Government of India</h3>
                    <h2 style={{color:"#0000CD", margin:"0px"}}>&nbsp;&nbsp;Ministry of Statistics and Programme Implementation</h2>

                    <div>&nbsp;</div>
                    <div>&nbsp;</div>
                    <DenseTable />
                    
                </div>
        </div>
    )
}

export default Main;