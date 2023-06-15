import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import hamster from '../../image/VhamsterV.jpg'
import dot from '../../svg/follow-modal-dot.svg'

import './EachFollower.css'

export default function EachFollower(follower, index, profileOwner, isMyProfile, closeFollowerModal) {

    const className = 'each-follower each-follower ' + index
    const [nickname, setNickname] = useState();
    const [isFollowing, setIsFllowing] = useState(0);

    let navigate = useNavigate();
    const toProfile = () => {
        closeFollowerModal();
        navigate('/' + nickname)
    };

    function follow() {
        axios.post("http://ec2-54-81-90-22.compute-1.amazonaws.com/accounts/followinmodal/", {
        // axios.post("http://localhost:8000/accounts/followinmodal/", {
            'nickname': nickname
        }).then(function (response) {
            setIsFllowing(1);
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        })
    }

    function unfollow() {
        axios.post("http://ec2-54-81-90-22.compute-1.amazonaws.com/accounts/unfollowinmodal/", {
        // axios.post("http://localhost:8000/accounts/unfollowinmodal/", {
            'nickname': nickname
        }).then(function (response) {
            setIsFllowing(0);
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        })
    }

    function changeNickname(nickname) {
        setNickname(nickname)
    }

    function changeIsFollowing(isFollowing) {
        setIsFllowing(isFollowing)
    }

    useEffect(() => {
        axios.post("http://ec2-54-81-90-22.compute-1.amazonaws.com/accounts/profilebyid/", {
        // axios.post("http://localhost:8000/accounts/profilebyid/", {
            'id': follower.follower,
            'profile_owner': profileOwner
        }).then(function (response) {
            changeNickname(response.data.data.nickname);
            changeIsFollowing(response.data.is_following);
        }).catch(function (error) {
            console.log(error);
        })
    }, [follower.follower, profileOwner])


    return (
        <div className={className}>
            <img src={hamster} alt="" className="follower-profile-img" onClick={toProfile} />
            <div className="follower-nickname" onClick={toProfile}>{nickname}</div>
            <img src={dot} alt="" className="dot" style={{ display: isMyProfile ? 'block' : 'none' }}/>
            {/* style={{ display: isMyProfile && isFollowing === 0 ? 'block':'none'}} */}
            <div className="follower-modal-follow-btn" style={{ display: isMyProfile && isFollowing === 0 ? 'block' : 'none' }} onClick={follow}>Follow</div>
            <div className="follower-modal-unfollow-btn" style={{ display: isMyProfile && isFollowing === 1 ? 'block' : 'none' }} onClick={unfollow}>Unfollow</div>
        </div>
    )
}
