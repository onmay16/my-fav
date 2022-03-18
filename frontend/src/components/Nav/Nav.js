import React from 'react'
import { useNavigate } from 'react-router-dom'

import './Nav.css'

import chart from '../../svg/chart.svg'
import settings from '../../svg/settings.svg'
import signout from '../../svg/signout.svg'

function Nav() {

    let navigate = useNavigate();
    
    const toMain = () => {
        navigate('/main')
    }
    const toReport = () => {
        navigate('/report')
    }
    const toSettings = () => {
        navigate('/settings')
    }
    const toSplash = () => {
        navigate('/splash')
    }

    return (
        <nav className='nav-bar'>
            <div className='logo-white' onClick={toMain}> 
            {/* should change route depending signin status */}
                MY
                <br />
                FAV
            </div>
            <div className='icons'>
                <img className='icon-chart' src={chart} onClick={toReport} />
                <br />
                <img className='icon-settings' src={settings} onClick={toSettings} />
                <br />
                <img className='signout' src={signout} onClick={toSplash} /> 
                {/* add logout action */}
            </div>
        </nav>
    )
}

export default Nav