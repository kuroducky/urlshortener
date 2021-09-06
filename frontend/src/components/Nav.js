import React from 'react';
import {Link} from 'react-router-dom';
import './style.css'

function Nav(){
    return(
        <div className="banner">
            <div className="navbar">
                <ul>
                    <li><Link to='/' className="nav-item nav-link active">Main Page</Link></li>
                    <li><Link to='/statistics' className="nav-item nav-link">Statistics</Link></li>
                </ul>
            </div>
        </div>
);
}

export default Nav;