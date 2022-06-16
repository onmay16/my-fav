import React from 'react';
import { useNavigate } from "react-router-dom";

import logo from '../../svg/big-logo.svg';

import './Splash.css'

function Splash() {

    let navigate = useNavigate();
    function handleClick() {
        navigate('/start')
    }

    return (
        <div className='entire-splash-page'>
            <header className='splash-header'>
                <div className='marquee'>
                    <span className='header-text'>----- curate and share your own playlist. find other’s taste. @curave -----</span>
                </div>
                <div className='marquee marquee2'>
                    <span className='header-text2'>----- curate and share your own playlist. find other’s taste. @cruave -----</span>
                </div>
            </header>
            <body className='splash-body'>
                <img src={logo} alt="curave_logo" className='splash-logo' onClick={handleClick} />
            </body>
        </div>
    );
}

export default Splash;
