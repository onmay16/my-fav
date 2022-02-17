import React from 'react'
import { useNavigate } from 'react-router-dom'

import './Nav.css'

import chart from '../../svg/chart.svg'
import settings from '../../svg/settings.svg'
import signout from '../../svg/signout.svg'

function Nav() {

    let navigate = useNavigate();
    function handleClick(url) {
        navigate(url)
    }

    return (
        <nav className='nav-bar'>
            <div className='logo-white' onClick={handleClick('/main')}> 
            {/* should change route depending signin status */}
                MY
                <br />
                FAV
            </div>
            <div className='icons'>
                <img className='icon-chart' src={chart} onClick={handleClick('/report')} />
                <br />
                <img className='icon-settings' src={settings} onClick={handleClick('/settings')} />
                <br />
                <img className='signout' src={signout} onClick={handleClick('/splash')} /> 
                {/* add logout action */}
            </div>
        </nav>
    )
}

export default Nav