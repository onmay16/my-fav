import React from 'react';
import { useNavigate } from "react-router-dom";

import './Splash.css'

import LogoRed from '../../components/LogoRed/LogoRed.js';
import Footer from '../../components/Footer/Footer.js';


function Splash() {

    let navigate = useNavigate();
    function handleClick() {
        navigate('/signup')
    }

    return (
        <div>
            <header>
                <LogoRed />
                <button className='join' onClick={handleClick}>sharing now!</button>
            </header>
            <body>
                <h1>This is Splash page</h1>
            </body>
            <Footer />
        </div>
    );
}

export default Splash;
