import React, { useState, useEffect } from 'react'

import './Main.css'

import Header from '../../components/Header/Header';
import NowPlaying from '../../components/NowPlaying/NowPlaying';

function Main() {

    return (
        <div className="entire-main-page">
            <Header />
            <body className='main-body'>
                <div className="welcome">Welcome Back,<br />May!</div>
                <div className="explore-box">
                    <div className='explore-text'>Explore feeds including these songs ☕</div>
                    <div className="songs">
                        <div className="song song1">
                            <div className="title title1">
                                Every Summertime
                            </div>
                            <hr className='main-hr' />
                            <div className="artist artist1">
                                NIKI
                            </div>
                        </div>
                        <div className="song song2">
                            <div className="title title2">
                                The Way It Was Before
                            </div>
                            <hr className='main-hr' />
                            <div className="artist artist2">
                                Johnny Stimson
                            </div>
                        </div>
                        <div className="song song3">
                            <div className="title title3">
                                pizza pepperoni
                            </div>
                            <hr className='main-hr' />
                            <div className="artist artist3">
                                Rahmania Astrini
                            </div>
                        </div>
                        <div className="song song4">
                            <div className="title title4">
                                Lemon
                            </div>
                            <hr className='main-hr' />
                            <div className="artist artist4">
                                Kenshi Yonezu
                            </div>
                        </div>
                    </div>
                </div>
                <NowPlaying />
            </body>
        </div>
    )
}

export default Main;