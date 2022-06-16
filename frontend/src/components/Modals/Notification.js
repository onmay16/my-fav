import React, { useState } from "react";
import { useNavigate } from 'react-router-dom'

import './Notification.css'

import heart from '../../svg/heart.svg'
import note from '../../svg/note.svg'
import comment from '../../svg/comment.svg'

const Notification = ({ notiVisible }) => {

    const classShowHide = notiVisible ? "noti-modal display-block" : "noti-modal display-none";

    return (
        <div className={classShowHide}>
            <div className="notification noti1">
                <img src={heart} alt="" className="heart"/>
                <div className="content content1">
                    soo liked your playlist.
                </div>
            </div>
            <div className="notification noti2">
                <img src={note} alt="" className="note" />
                <div className="content content2">
                    soo curated new playlist.
                </div>
            </div>
            <div className="notification noti3">
                <img src={comment} alt="" className="comment" />
                <div className="content content3">
                    soo left a comment on your playlist.
                </div>
            </div>
        </div>
    )
}

export default Notification;