import React, { useState } from 'react'

import './Main.css'

import Nav from '../../components/Nav/Nav';

import message from '../../svg/message.svg'
import notification from '../../svg/notification.svg'
import profile from '../../svg/profile.svg'
import axios from 'axios';

function Main(props) {
    
    console.log(props.user)

    console.log('result');

    axios
        .get("http://localhost:8000/accounts/user/")
        .then((response) => {
            
            console.log(response.data);
        })


    // const [user, userChange] = useState(props.user)
    // const [nickname, nicknameChange] = useState(user[0])

    return (
        <div className='main'>
            <Nav className='nav' />
            <div className='main-wrapper'>
                <div className='header'>
                    <div className='search-box'>
                        <div className='search-filter'></div>
                        <input className='search-input' type='text' placeholder='       Search with song title, artist name...' />
                    </div>
                    <div className='personal-menu'>
                        <img className='message' src={message} />
                        <img className='notification' src={notification} />
                        <img className='profile' src={profile} />
                    </div>
                </div>
                <div className='content-section'>
                    <div className='welcome-comment'>
                        Welcome Back
                        <br />
                        Hong!
                    </div>
                    <div className='recommendation'>
                        <div className='first-column'>
                            <div className='user-recommendation'></div>
                            <div className='genre-recommendation'></div>
                        </div>
                        <div className='second-column'>
                            <div className='playlist-recommendation'></div>
                        </div>


                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;