import React, { useState, useEffect, useRef }  from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import axios from 'axios';

import './Profile.css'

import Header from '../../components/Header/Header'
import NowPlaying from '../../components/NowPlaying/NowPlaying'
import PostDetail from '../../components/Modals/PostDetail'
import Followers from '../../components/Modals/Followers'
import Following from '../../components/Modals/Following'
import Row from './Row';

import profileImage from '../../image/profile-ex.jpeg'
import instagram from '../../svg/instagram.svg'
import addBtn from '../../svg/add-btn.svg'
import settings from '../../svg/settings.svg'

function Profile() {

    let nickname = useParams();
    let navigate = useNavigate();

    const toAddSong = () => {
        navigate('/add')
    }
    const toSettings = () => {
        navigate('/settings')
    }
    const toEdit = () => {
        navigate('/edit', {state: {nickname: profile.nickname, instagram: profile.insta_url, profile_pic: profile.profile_pic, bio: profile.bio}})
    }
    
    const [user, setUser] = useState({});
    const userHandler = (user) => {
        setUser(user);
    }
    const [profile, setProfile] = useState({});
    const [follower, setFollower] = useState(0);
    const [followerArray, setFollowerArray] = useState([]);
    const [following, setFollowing] = useState(0);
    const [followingArray, setFollowingArray] = useState([]);
    const [rows, setRows] = useState([]);
    const [posts, setPosts] = useState([]);
    const [songArray, setSongArray] = useState([]);
    const [detailModal, setDetailModal] = useState(false);
    const [postInfo, setPostInfo] = useState([]);
    const [postImg, setPostImg] = useState();
    const [isFollowing, setIsFollowing] = useState(false);
    const [followerModal, setFollowerModal] = useState(false);
    const [followingModal, setFollowingModal] = useState(false);
    const [isMyProfile, setIsMyProfile] = useState(false);

    function openDetailModal(post, jacket) {
        setDetailModal(true);
        setPostInfo(post);
        setPostImg(jacket);
    }

    const songDisplayList = useRef(null);

    function follow() {
        axios.get("http://localhost:8000/accounts/follow/"+nickname.nickname+"/")
        .then(function (response) {
            console.log(response.data)
            setFollower(follower+1)
            setIsFollowing(!isFollowing)
        })
    }

    function unfollow() {
        axios.get("http://localhost:8000/accounts/unfollow/"+nickname.nickname+"/")
        .then(function (response) {
            console.log(response.data)
            setFollower(follower-1)
            setIsFollowing(!isFollowing)
        })
    }

    function changeIsMyProfile() {
        setIsMyProfile(true);
    }

    useEffect(() => {
        axios.get("http://localhost:8000/playlist/user/")
        .then((response) => {
            userHandler(response.data.profile)
        }).catch((error) => {
            console.log(error);
        })

        axios.get("http://localhost:8000/accounts/profile/" + nickname.nickname + "/")
        .then((response) => {
            setProfile(response.data.profile);
            setFollower(response.data.follower_count);
            setFollowerArray(response.data.follower);
            setFollowing(response.data.following_count);
            setFollowingArray(response.data.following);
            setIsFollowing(response.data.is_following);

            const songList = [];
            const postList = [];
            const tempRows = [];
            
            Promise.all(response.data.posts.map((post, index) => {
                songList.push(response.data.songs[index]);
                postList.push(post);
                if (index%4 === 0) {
                    tempRows.push(Math.floor(index/4));
                }
            })).then(() => {
                setSongArray(songList);
                setPosts(postList);
                setRows(tempRows);
            })

        }).catch((error) => {
            console.log(error);
        })

        if (user.nickname === profile.nickname) {
            console.log(user.nickname);
            console.log(profile.nickname);
            changeIsMyProfile(true);
        }

    }, [nickname.nickname, ])

    return (
        <div className="entire-profile-page">
            <Header />
            <PostDetail detailModal={detailModal} setDetailModal={setDetailModal} postInfo={postInfo} postImg={postImg} nickname={profile.nickname}/>
            <Followers followerModal={followerModal} setFollowerModal={setFollowerModal} followerArray={followerArray} profileOwner={profile.nickname} isMyProfile={isMyProfile}/>
            <Following followingModal={followingModal} setFollowingModal={setFollowingModal} followingArray={followingArray} profileOwner={profile.nickname} isMyProfile={isMyProfile}/>
            <div className="profile-body">
                <div className="profile-section">
                    <img src={profileImage} alt="" className="profile-image" />
                    <div className="profile-info">
                        <div className="left-section">
                            <div className="name-edit">
                                <div className="user-name">{profile.nickname}</div>
                                <div className="to-edit" onClick={toEdit} style={{display: user.nickname === profile.nickname ? 'block':'none'}}>Edit</div>
                            </div>
                            <div className="follow-section">
                                <div className="follow follower">
                                    <div className="fn follower-number" onClick={() => setFollowerModal(true)}>{follower}</div>
                                    <div className='ft follower-text'>Follower</div>
                                </div>
                                <div className="follow following">
                                    <div className="fn following-number" onClick={() => setFollowingModal(true)}>{following}</div>
                                    <div className='ft following-text'>Following</div>
                                </div>
                            </div>
                            <div className="bio">
                                {profile.bio}
                            </div>
                        </div>
                        <div className="right-section">
                            <a href={"https://www.instagram.com/" + profile.instagram} target="_blank">
                            <img src={instagram} alt="" className="instagram" />
                            </a>
                            <div className="profile-btn-container" style={{ display: user.nickname === profile.nickname ? 'none' : 'flex' }}>
                                <button className="profile-btn follow-btn" onClick={follow} style={{ display: isFollowing ? 'none' : 'block' }}>follow</button>
                                <button className="profile-btn following-btn" onClick={unfollow} style={{ display: isFollowing ? 'block' : 'none' }}><span>following</span></button>
                                <button className="profile-btn message-btn">message</button>
                            </div>
                        </div>
                    </div>
                    <div className="etc-option-btns">
                        <img src={addBtn} alt="" className="add-btn" onClick={toAddSong} />
                        <img src={settings} alt="" className="settings-btn" onclick={toSettings}/>
                    </div>
                </div>
                <hr className="profile-hr" />
                <div className="song-display" ref={songDisplayList}>
                    {rows.map((row) => Row(row, songArray, posts, openDetailModal))}
                </div>
                <NowPlaying />
            </div>
        </div>
    )
}

export default Profile