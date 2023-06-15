import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import './Main.css'

import Header from '../../components/Header/Header';
import NowPlaying from '../../components/NowPlaying/NowPlaying';

function Main() {

    const [user, setUser] = useState({});
    const userHandler = (user) => {
        setUser(user);
    }
    const [mainSongs, setMainSongs] = useState([]);
    const [mainUsers, setMainUsers] = useState([]);

    let navigate = useNavigate();
    const toProfile = (nickname) => {
        navigate('/'+ nickname)
    };

    useEffect(() => {
        axios.get("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/user/")
        // axios.get("http://localhost:8000/playlist/user/")
        .then((response) => {
            userHandler(response.data.profile);
        }).catch((error) => {
            console.log(error);
        })

        // const randomSongs = []
        axios.get("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/main/")
        // axios.get("http://localhost:8000/playlist/main/")
        .then((response) => {
            console.log(response);
            setMainSongs(response.data.songs);
            setMainUsers(response.data.users);
        }).catch((error) => {
            console.log(error);
        })

    }, [])

    return (
        <div className="entire-main-page">
            <Header />
            <body className='main-body'>
                <div className="welcome">Welcome Back,<br />{user.nickname}!</div>
                <div className="explore-box">
                    <div className='explore-text'>Explore new songs ☕</div>
                    <div className="songs">
                        {mainSongs.map((song, i) => {
                            const className1 = "song song" + (i+1)
                            const className2 = "main-title title" + (i+1)
                            const className3 = "main-artist artist" + (i+1)

                            return (
                                <div className={className1} onClick={() => toProfile(mainUsers[i].nickname)}>
                                    <div className={className2}>
                                        {song.title}
                                    </div>
                                    <hr className='main-hr' />
                                    <div className={className3}>
                                        {song.artist}
                                    </div>
                                </div>
                            )
                        })}
                    </div>
                </div>
                <NowPlaying />
            </body>
        </div>
    )
}

export default Main;