import React, { useState, useEffect } from "react";
import { Navigate, useNavigate } from "react-router";

import curatorIcon from "../../svg/start-curator.svg";
import newIcon from "../../svg/start-new.svg";

import "./Start.css";

function Start() {
    const [curatorVisible, setCuratorVisible] = useState(true);
    const [newVisible, setNewVisible] = useState(true);
    const [curatorEmailOption, setCuratorEmailOption] = useState(false);

    let navigate = useNavigate();
    const toMain = () => {
        navigate('/main')
    };

    return (
        <div className="entire-start-page">
            <div className="to-main" onClick={toMain}>To main page ➜</div>
            <div className="start-body">
                <div className="curator-box" onClick={() => setNewVisible(!newVisible)} style={{ display: curatorVisible ? 'flex' : 'none' }}>
                    <div className="curator">curator</div>
                    <img src={curatorIcon} alt="curator_icon" className="curator-icon" />
                </div>
                <span className="new-register" style={{ display: !curatorVisible ? 'flex' : 'none' }}>
                    <label htmlFor="email">Email</label>
                    <input type="text" />
                    <label htmlFor="nickname" className="label-with-padding">Nickname</label>
                    <input type="text" />
                    <label htmlFor="password" className="label-with-padding">Password</label>
                    <input type="password" />
                    <label htmlFor="confirmation" className="label-with-padding">Password confirmation</label>
                    <input type="password" />
                    <button className="new-register-email-confirm-btn btn-margin">Confirm</button>
                    <button className="new-register-google-btn">Sing up with Google</button>
                </span>
                <span className="new-box" onClick={() => setCuratorVisible(!curatorVisible)} style={{ display: newVisible ? 'flex' : 'none' }}>
                    <div className="new">new</div>
                    <img src={newIcon} alt="new_icon" className="new-icon" />
                </span>
                <span className="curator-login" style={{ display: !newVisible ? 'flex' : 'none' }}>
                    <div className="curator-login-email-btn" onClick={() => setCuratorEmailOption(!curatorEmailOption)}>Sign in with email</div>
                    <div className="curator-login-email" style={{ display: curatorEmailOption ? 'flex' : 'none' }}>
                        <label htmlFor="email">Email</label>
                        <input type="text" />
                        <label htmlFor="password" className="label-with-padding ">Password</label>
                        <input type="password" />
                    </div>
                    <div className="curator-login-google-btn">Sign in with Google</div>
                </span>
            </div>
        </div>
    );
}

export default Start;
