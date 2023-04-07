import axios from "axios";

import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router";

import curatorIcon from "../../svg/start-curator.svg";
import newIcon from "../../svg/start-new.svg";

import "./Start.css";

function Start() {
    
    const [curatorVisible, setCuratorVisible] = useState(true);
    const [newVisible, setNewVisible] = useState(true);

    let navigate = useNavigate();
    const toMain = () => {
        navigate('/main')
    };

    function signInSubmit() {
        var getEmail = document.getElementsByClassName('signin-email-value')[0].value;
        var getPassword = document.getElementsByClassName('signin-pw-value')[0].value;
        axios.post("http://ec2-54-144-19-73.compute-1.amazonaws.com:8080/accounts/signin/", {
            "email": getEmail,
            "password": getPassword
        }).then(function (response) {
            var status = response.status;
            console.log(response);
            if (status === 200) {
                toMain()
            } else {
                console.log(response.data.message)
                alert(response.data.message)
            };
        }).catch(function (error) {
            console.log(error);
        })
    }

    function signUpSubmit() {
        var getEmail = document.getElementsByClassName('signup-email-value')[0].value;
        var getNickname = document.getElementsByClassName('signup-nickname-value')[0].value;
        var getPassword = document.getElementsByClassName('signup-pw-value')[0].value;
        var getPasswordConfirm = document.getElementsByClassName('signup-pw2-value')[0].value;
        axios.post("http://ec2-54-144-19-73.compute-1.amazonaws.com:8080/accounts/signup/", {
            "email": getEmail,
            "nickname": getNickname,
            "password1": getPassword,
            "password2": getPasswordConfirm
        }).then(function (response) {
            if (response.status === 200) {
                toMain();
            } else {
                console.log(response.data.message)
                alert(response.data.message)
            };
        }).catch(function (error) {
            console.log(error);
        })
    }


    return (
        <div className="entire-start-page">
            <div className="to-main" onClick={toMain}>To main page</div>
            <div className="start-body">
                <div className="curator-box" onClick={() => setNewVisible(!newVisible)} style={{ display: curatorVisible ? 'flex' : 'none' }}>
                    <div className="curator">curator</div>
                    <img src={curatorIcon} alt="curator_icon" className="curator-icon" />
                </div>
                <span className="new-register" style={{ display: !curatorVisible ? 'flex' : 'none' }}>
                    <label htmlFor="email" className="start-label">Email</label>
                    <input className="start-input signup-email-value" type="text" />
                    <label htmlFor="nickname" className="label-with-padding start-label">Nickname</label>
                    <input className="start-input signup-nickname-value" type="text" />
                    <label htmlFor="password" className="label-with-padding start-label">Password</label>
                    <input className="start-input signup-pw-value" type="password" />
                    <label htmlFor="confirmation" className="label-with-padding start-label">Password confirmation</label>
                    <input className="start-input signup-pw2-value" type="password" />
                    <button className="new-register-email-confirm-btn btn-margin"onClick={signUpSubmit}>Confirm</button>
                    <button className="new-register-google-btn">Sing up with Google</button>
                </span>
                <span className="new-box" onClick={() => setCuratorVisible(!curatorVisible)} style={{ display: newVisible ? 'flex' : 'none' }}>
                    <div className="new">new</div>
                    <img src={newIcon} alt="new_icon" className="new-icon" />
                </span>
                <span className="curator-login" style={{ display: !newVisible ? 'flex' : 'none' }}>
                    <div className="curator-login-email">
                        <div className="curator-login-input-boxes">
                            <label htmlFor="email" className="start-label">Email</label>
                            <input className="start-input signin-email-value" type="text" />
                            <label htmlFor="password" className="label-with-padding start-label">Password</label>
                            <input className="start-input signin-pw-value" type="password" />
                        </div>
                    </div>
                    <div className="curator-login-confirm-btn" onClick={signInSubmit}>Sign in</div>
                    <div className="curator-login-google-btn">Sign in with Google</div>
                </span>
            </div>
        </div>
    );
}

export default Start;
