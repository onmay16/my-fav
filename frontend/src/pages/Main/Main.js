import React, { useState, useEffect } from 'react'

import './Main.css'

import Nav from '../../components/Nav/Nav';

import message from '../../svg/message.svg'
import notification from '../../svg/notification.svg'
import profile from '../../svg/profile.svg'
import null_pic from '../../svg/bear.svg'

import axios from 'axios';

function Main() {

    const [user1, SetUser1] = useState({});
    const [user2, SetUser2] = useState({});

    const user1Handler = (user) => {
        SetUser1(user);
    }
    const user2Handler = (user) => {
        SetUser2(user);
    }

    useEffect(() => {
        axios
        .get("http://localhost:8000/playlist/main/")
        .then((response) => {
            console.log("raw data", response.data);
            user1Handler(response.data.first_profile);
            user2Handler(response.data.second_profile);
        })
        .catch((error) => {

        })
    }, [])


    return (
        <div className='main' >
            <Nav className='nav' />
            <div className='main-wrapper'>
                <div className='header'>
                    <div className='search-box'>
                        <div className='search-filter'></div>
                        <input className='search-input' type='text' placeholder='      Search with song title, artist name...' />
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
                            <div className='user-recommendation'>
                                <div>
                                    <h2 className='section-title'>Recommended User ✨</h2>
                                    <hr />
                                </div>
                                <div className='users'>
                                    <div className='first-user'>
                                        <img className='profile-pic' src={user1.profile_pic === null ? null_pic:"http://localhost:8000" + user1.profile_pic} />
                                        <br />
                                        <div className='nickname'>{user1.nickname}</div>
                                    </div>
                                    <div className='second-user'>
                                        <img className='profile-pic' src={user2.profile_pic === null ? null_pic:"http://localhost:8000" + user2.profile_pic} />
                                        <br />
                                        <div className='nickname'>{user2.nickname}</div>
                                    </div>
                                </div>
                            </div>
                            <div className='genre-recommendation'>
                                <h2 className='section-title'>Genre Recommendation</h2>
                                <hr />
                            </div>
                        </div>
                        <div className='second-column'>
                            <div className='playlist-recommendation'>
                            <h2 className='section-title'>Playlist Recommendation</h2>
                                <hr />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;