import React from 'react'
import EachFollower from './EachFollower';

import './Followers.css';

import close from '../../svg/follow-close.svg'

function Followers(props) {
    const followerShowHide = props.followerModal ? 'follower-list-bg display-block':'follower-list-bg display-none'
    
    function closeFollowerModal() {
        props.setFollowerModal(false);
    }

    // console.log(props.followerArray)
    const followerArray  = props.followerArray;

    return (
        <div className={followerShowHide}>
            <div className="entire-follower-modal">
                <div className="follower-modal-header">
                    <div className="follower-modal-title">Followers</div>
                    <img src={close} alt="" className="follower-close-btn" onClick={closeFollowerModal}/>
                </div>
                <div className="follower-list">
                    {followerArray.map((follower, index) => EachFollower(follower, index, props.profileOwner, props.isMyProfile, closeFollowerModal))}
                </div>
            </div>
        </div>
    )
}

export default Followers