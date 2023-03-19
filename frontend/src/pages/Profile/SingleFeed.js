import React, { useState } from 'react'

import './SingleFeed.css'
import PostDetail from '../../components/Modals/PostDetail'
import openDetailModal from '../../pages/Profile/Profile'

function SingleFeed(i, song, post, openDetailModal) {

    const containerClass = "cover-container cc" + i;
    const imgClass = "cover cover" + i;

    return (
        <div className={containerClass} onClick={() => openDetailModal(post, song['jacket'])}>
            {/* <PostDetail detailModal={detailModal} setDetailModal={setDetailModal}/> */}
            <img src={song['jacket']} className={imgClass} />
        </div>
    )
}

export default SingleFeed