import React from 'react'

import './Following.css';

import hamster from '../../image/VhamsterV.jpg'

import close from '../../svg/follow-close.svg'
import dot from '../../svg/follow-modal-dot.svg'

function Following(props) {

  const followingShowHide = props.followingModal ? 'following-list-bg display-block':'following-list-bg display-none'
    
    function closeFollowingModal() {
        props.setFollowingModal(false);
    }

  return (
    <div className={followingShowHide}>
        <div className="entire-following-modal">
                <div className="following-modal-header">
                    <div className="following-modal-title">Following</div>
                    <img src={close} alt="" className="following-close-btn" onClick={closeFollowingModal}/>
                </div>
                <div className="following-list">
                    <div className="following">
                        <img src={hamster} alt="" className="following-profile-img" />
                        <div className="following-nickname">VhansterV</div>
                        <div className="following-modal-follow-btn"><span className="following-follow-text">Follow</span></div>
                    </div>
                </div>
            </div>
    </div>
  )
}

export default Following