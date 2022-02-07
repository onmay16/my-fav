import { useNavigate } from 'react-router-dom';
import React from 'react';
import logo from '../../svg/logo.svg';

import './LogoRed.css'

function LogoRed() {

    let navigate = useNavigate();
    function handleClick() {
        navigate('/')
    }

    return (
        <div>
            <img src={logo} className="Logo" alt="logo" onClick={handleClick} />
        </div>
    );
}

export default LogoRed;
