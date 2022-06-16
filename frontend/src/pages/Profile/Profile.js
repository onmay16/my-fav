import React from 'react'

import './Profile.css'

import Header from '../../components/Header/Header'
import NowPlaying from '../../components/NowPlaying/NowPlaying'

import profileImage from '../../image/profile-image.jpeg'
import instagram from '../../svg/instagram.svg'

import beatles from '../../image/beatles.jpeg'
import radioHead from '../../image/radiohead.png'
import sheIs from '../../image/sheIs.jpeg'
import surfer from '../../image/surfer.jpeg'
import shortHair from '../../image/shorthair.jpeg'
import honne from '../../image/honne.jpeg'
import taylor from '../../image/Taylor.jpeg'

function Profile() {
    return (
        <div className="entire-profile-page">
            <Header />
            <div className="profile-body">
                <div className="profile-section">
                    <img src={profileImage} alt="" className="profile-image" />
                    <div className="profile-info">
                        <div className="left-section">
                            <div className="user-name">Sugyeong</div>
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
                                Hi! I'm Sugyeong. Welcome to my feed.
                            </div>
                        </div>
                        <div className="right-section">
                            <img src={instagram} alt="" className="instagram" />
                            <button className="profile-btn follow-btn">follow</button>
                            <button className="profile-btn message-btn">message</button>
                        </div>
                    </div>
                </div>
                <hr className="profile-hr" />
                <div className="song-display">
                    <div className="row row1">
                        <img src={beatles} alt="" className='cover cover1'/>
                        <img src={radioHead} alt="" className="cover cover2" />
                        <img src={sheIs} alt="" className="cover cover3" />
                        <img src={surfer} alt="" className="cover cover4" />
                    </div>
                    <div className="row row2">
                        <img src={shortHair} alt="" className="cover cover5" />
                        <img src={honne} alt="" className="cover cover6" />
                        <img src={taylor} alt="" className="cover cover7" />
                    </div>
                </div>
                <NowPlaying />
            </div>
        </div>
    )
}

export default Profile