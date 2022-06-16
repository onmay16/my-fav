import React from 'react'

import './NowPlaying.css'

import nowPlaying from '../../image/now-playing.png'

function NowPlaying() {
    return (
        <img src={nowPlaying} alt="" className="now-playing" />
    )
}

export default NowPlaying;