import React from 'react'
import { useNavigate } from 'react-router-dom'

import './Profile.css'

import Header from '../../components/Header/Header'
import NowPlaying from '../../components/NowPlaying/NowPlaying'

import profileImage from '../../image/profile-image.jpeg'
import instagram from '../../svg/instagram.svg'
import addBtn from '../../svg/add-btn.svg'
import settings from '../../svg/settings.svg'

import beatles from '../../image/beatles.jpeg'
import radioHead from '../../image/radiohead.png'
import sheIs from '../../image/sheIs.jpeg'
import surfer from '../../image/surfer.jpeg'
import shortHair from '../../image/shorthair.jpeg'
import honne from '../../image/honne.jpeg'
import taylor from '../../image/Taylor.jpeg'

function Profile() {

    let navigate = useNavigate();
    const toAddSong = () => {
        navigate('/add')
    }
    const toSettings = () => {
        navigate('/settings')
    }

    return (
        <div className="entire-profile-page">
            <Header />
            <div className="profile-body">
                <div className="profile-section">
                    <img src={profileImage} alt="" className="profile-image" />
                    <div className="profile-info">
                        <div className="left-section">
                            <div className="name-edit">
                                <div className="user-name">May</div>
                                <div className="to-edit">Edit</div>
                            </div>
                            <div className="follow-section">
                                <div className="follow follower">
                                    <div className="fn follower-number">253</div>
                                    <div className='ft follower-text'>Follower</div>
                                </div>
                                <div className="follow following">
                                    <div className="fn following-number">253</div>
                                    <div className='ft following-text'>Following</div>
                                </div>
                            </div>
                            <div className="bio">
                                Hi! I'm May. <br />
                                Welcome to my feed. :)
                            </div>
                        </div>
                        <div className="right-section">
                            <img src={instagram} alt="" className="instagram" />
                            <button className="profile-btn follow-btn">follow</button>
                            <button className="profile-btn message-btn">message</button>
                        </div>
                    </div>
                    <div className="etc-option-btns">
                        <img src={addBtn} alt="" className="add-btn" onClick={toAddSong} />
                        <img src={settings} alt="" className="settings-btn" onclick={toSettings}/>
                    </div>
                </div>
                <hr className="profile-hr" />
                <div className="song-display">
                    <div className="row row1">
                        <div className="cover-container cc1">
                            <img src={beatles} alt="" className='cover cover1' />
                        </div>
                        <div className="cover-container c2">
                            <img src={radioHead} alt="" className="cover cover2" />
                        </div>
                        <div className="cover-container c3">
                            <img src={sheIs} alt="" className="cover cover3" />
                        </div>
                        <div className="cover-container c4">
                            <img src={surfer} alt="" className="cover cover4" />
                        </div>
                    </div>
                    <div className="row row2">
                        <div className="cover-container c5">
                            <img src={shortHair} alt="" className="cover cover5" />
                        </div>
                        <div className="cover-container c6">
                            <img src={honne} alt="" className="cover cover6" />
                        </div>
                        <div className="cover-container c7">
                            <img src={taylor} alt="" className="cover cover7" />
                        </div>
                    </div>
                </div>
                <NowPlaying />
            </div>
        </div>
    )
}

export default Profile