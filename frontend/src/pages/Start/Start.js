import React, { useState, useEffect } from "react";
import useFade from "../../hooks/useFade.js";

import curatorIcon from "../../svg/start-curator.svg";
import newIcon from "../../svg/start-new.svg";

import "./Start.css";

function Start() {
    const [curatorVisible, setCuratorVisible] = useState(true);
    const [newVisible, setNewVisible] = useState(true);

    return (
        <div className="entire-start-page">
            <span className={curatorVisible ? 'curator-box-visible':'curator-box-invisible'} onClick={() => setNewVisible(false)}>
                <div className="curator">curator</div>
                <img src={curatorIcon} alt="curator_icon" className="curator-icon" />
            </span>

            <span className={newVisible ? 'new-box-visible':'new-box-invisible'} onClick={() => setCuratorVisible(false)}>
                <div className="new">new</div>
                <img src={newIcon} alt="new_icon" className="new-icon" />
            </span>
        </div>
    );
}

export default Start;
