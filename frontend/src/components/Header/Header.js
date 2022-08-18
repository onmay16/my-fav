import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

import './Header.css'

import Notification from '../Modals/Notification';

import logo from '../../svg/big-logo.svg';
import notification from '../../svg/notification.svg'
import message from '../../svg/message.svg'
import userIcon from '../../svg/profile.svg'
import signout from '../../svg/signout.svg'
import axios from 'axios';

function Header() {

    let navigate = useNavigate();
    const toMain = () => {
        navigate('/main')
    }
    const toMessage = () => {
        navigate('/message')
    };
    const toSplash = () => {
        navigate('/')
    }

    const [notiVisible, setNotiVisible] = useState(false);
    
    const [user, setUser] = useState({});
    const userHandler = (user) => {
        setUser(user);
    }

    useEffect(() => {
        axios.get("http://localhost:8000/playlist/user/")
        .then((response) => {
            userHandler(response.data.profile);
        }).catch((error) => {
            console.log(error);
        })
    }, [])
    const toProfile = () => {
        navigate('/'+ user.nickname)
    };

    function signOutSubmit() {
        axios("http://localhost:8000/accounts/signout/")
        .then(function (response) {
            console.log(response);
            if (response.status === 200) {
                toSplash()
            }
        }).catch(function (error) {
            console.log(error);
        })
    }

    return (
        <header className='header'>
            <img src={logo} alt="" className="logo" onClick={toMain} />
            <div className="user-menu">
                <div className="noti">
                    <Notification notiVisible={notiVisible} className='noti-modal' />
                    <img src={notification} alt="" className="noti-icon" onClick={() => setNotiVisible(!notiVisible)} />
                </div>
                <img src={message} alt="" className='message' onClick={toMessage}/>
                <img src={user.profile_pic === null ? userIcon:"http://localhost:8000" + user.profile_pic} alt="" className="profile" onClick={toProfile}/>
                <img src={signout} alt="" className="signout" onClick={signOutSubmit}/>
            </div>
        </header>
    )
}

export default Header