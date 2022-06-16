import React, { useState } from 'react'

import './Header.css'

import Notification from '../Modals/Notification';

import logo from '../../svg/big-logo.svg';
import notification from '../../svg/notification.svg'
import message from '../../svg/message.svg'
import userIcon from '../../svg/profile.svg'
import { useNavigate } from 'react-router-dom';

function Header() {

    let navigate = useNavigate();
    const toMain = () => {
        navigate('/main')
    }
    const toProfile = () => {
        navigate('/profile')
    };

    const [notiVisible, setNotiVisible] = useState(false);

    return (
        <header className='header'>
            <img src={logo} alt="" className="logo" onClick={toMain} />
            <div className="user-menu">
                <div className="noti">
                    <Notification notiVisible={notiVisible} className='noti-modal' />
                    <img src={notification} alt="" className="noti-icon" onClick={() => setNotiVisible(!notiVisible)} />
                </div>
                <img src={message} alt="" className='message' />
                <img src={userIcon} alt="" className="profile" onClick={toProfile}/>
            </div>
        </header>
    )
}

export default Header