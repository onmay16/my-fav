import React from 'react';
import { useNavigate } from "react-router-dom";

import logo from '../../svg/big-logo.svg';

import './Splash.css'

import LogoRed from '../../components/LogoRed/LogoRed.js';
import Footer from '../../components/Footer/Footer.js';


function Splash() {

    let navigate = useNavigate();
    function handleClick() {
        navigate('/signup')
    }

    return (
        <div className='entire-splash-page'>
            <header className='splash-header'>
                {/* <LogoRed />
                <button className='join' onClick={handleClick}>sharing now!</button> */}
                <marquee behavior="" direction="">curate your own playlist and share. find other’s taste. CURATE YOUR PLAYLIST AND SHARE. FIND OTHER'S TASTE.</marquee>
            </header>
            <body className='splash-body'>
                {/* <h1>This is Splash page</h1> */}
                <img src={logo} alt="curave_logo" className='logo' />
            </body>
            {/* <Footer /> */}
        </div>
    );
}

export default Splash;
