import React from 'react'

import './Message.css'

import Header from '../../components/Header/Header.js'

import messageSendIcon from '../../svg/message-send.svg'

import cuttieCatty from '../../image/CuttieCatty.jpeg'
import imadog from '../../image/Imadog.JPG'
import VhamsterV from '../../image/VhamsterV.jpg'


function Message() {
    return (
        <div className="entire-message-page">
            <Header />
            <div className="message-body">
                <div className="message-user-list">
                    <div className="message-user user1">
                        <img src={cuttieCatty} alt="" className="message-user-profile mup1" />
                        <div className="message-user-id mui1">cuttieCatty</div>
                    </div>
                    <div className="message-user user2">
                        <img src={imadog} alt="" className="message-user-profile mup2" />
                        <div className="message-user-id mui2">Imadog</div>
                    </div>
                    <div className="message-user user3">
                        <img src={VhamsterV} alt="" className="message-user-profile mup3" />
                        <div className="message-user-id mui3">VhamsterV</div>
                    </div>
                </div>
                <hr className="message-hr" />
                <div className="chat-window">
                    <div className="chat chat1">hey there!</div>
                    <div className="chat chat2">I really like your feed</div>
                    <div className="chat chat3">Thank you! I love your profile pic :)</div>
                    <div className="chat chat4">Hehe I know it’s me! 🐹</div>
                </div>
                <div className="message-send-section">
                    <input type="text" className="chat-input" placeholder='Type messsage here...'/>
                    <img src={messageSendIcon} alt="" className="message-send-icon" />
                </div>
                <hr className="message-send-hr" />
            </div>
        </div>
    )
}

export default Message;