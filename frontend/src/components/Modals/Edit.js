import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router";
import { useLocation } from 'react-router-dom';

import './Edit.css'

import profileDefault from '../../image/profile-ex.jpeg'
import confirm from '../../svg/add-confirm-btn.svg'
import axios from 'axios';

function Edit() {

    const location = useLocation();

    const [profilePic, setProfilePic] = useState(location.state.profile_pic);
    const [nickname, setNickname] = useState(location.state.nickname);
    const [instagram, setInstagram] = useState(location.state.instagram)
    const [bio, setBio] = useState(location.state.bio);

    function editSubmit() {
        
        let currentNickname = document.getElementsByClassName('edit-nickname')[0].value;
        let currentInsta = document.getElementsByClassName('edit-insta')[0].value;
        let currentBio = document.getElementsByClassName('edit-bio')[0].value;
        setNickname(currentNickname);

        // let currentPic = document.getElementById('profile-pic').files[0].mozFullPath;
        // console.log('current pic path:' + currentPic);
        
        axios.post("http://localhost:8000/accounts/profile/" + nickname + "/", {
            'nickname': currentNickname,
            'instagram': currentInsta,
            'bio': currentBio
        })
        .then(function (response) {
            console.log(response);
            toProfile(currentNickname);
        }).catch(function (error) {
            console.log(error);
        })
    }

    let navigate = useNavigate();
    const toProfile = (nickname) => {
        navigate('/'+ nickname)
    };

    function changeProfile(event) {
        let currentPic = URL.createObjectURL(event.target.files[0]);
        setProfilePic(currentPic);
    }

    useEffect(() => {

    }, [profilePic])

    return (
        <div className="entire-edit-page">
            <div className="current-section">
                <img src={profilePic ? profilePic:profileDefault} alt="" className="edit-current-pic" />
                <label htmlFor="profile-pic" className='edit-label-pic'>Upload picture
                    <input type="file" name="profile-pic" className='edit-profile-pic' id ='profile-pic' accept="image/*" onChange={changeProfile} />
                </label>
                <div className="edit-current-nick">{nickname}</div>
            </div>
            <form className='edit-form'>
                <div className="edit-section edit-nickname-section">
                    <div className="edit-label-container">
                        <label htmlFor="nickname" className="edit-label edit-label-nickname">Nickname</label>
                    </div>
                    <input type="text" name='nickname' className='edit-input edit-nickname' defaultValue={nickname} />
                </div>
                <div className="edit-section edit-insta-section">
                <div className="edit-label-container">
                    <label htmlFor="instagram" className="edit-label edit-label-insta">Instagram ID</label>
                </div>
                    <input type="url" name="instagram" className="edit-input edit-insta" defaultValue={instagram} />
                </div>
                <div className="edit-section edit-bio-section">
                <div className="edit-label-container">
                    <label htmlFor="bio" className="edit-label edit-label-bio">Bio</label>
                </div>
                    <textarea type="text" name="bio" className='edit-input edit-bio' defaultValue={bio}/>
                </div>
                <img src={confirm} alt="" className="edit-submit" onClick={editSubmit}/>
            </form>

        </div>
    )
}

export default Edit;