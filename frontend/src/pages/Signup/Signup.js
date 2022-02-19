import React, { useState } from 'react';
import axios from 'axios';

import tempimg from '../../svg/music-player.svg'
import google from '../../svg/google.svg'

import './Signup.css'

import LogoRed from '../../components/LogoRed/LogoRed.js';
import Form from '../../components/Form/Form.js'
import Signin from '../../components/Modals/Signin';



function Signup() {

    const [text, textChange] = useState(['Nickname', 'Email', 'Password', 'PasswordConfirmation']);

    const [email, setEmail] = useState('');
    const [nickname, setNickname] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const [signInModalOn, setSignInModalOn] = useState(false);

    const signInClickHandler = () => {
        setSignInModalOn(!signInModalOn);
    }

    const emailHandler = (event) => {
        setEmail(event.target.value);
    }

    const nicknameHandler = (event) => {
        setNickname(event.target.value);
    }

    const passwordHandler = (event) => {
        setPassword(event.target.value);
    }

    const password2Handler = (event) => {
        setPassword2(event.target.value);
    }

    const onClick = (event) => {
        event.preventDefault();

        axios
            .post("http://localhost:8000/accounts/signup/", {
                "email": email,
                "nickname": nickname,
                "password1": password,
                "password2": password2,
            })
            .then((response) => {
                console.log(response.data);
                var m = (response.data.message);
                if (m === 'User already exist.') {
                    alert('User already exist.')
                };
                if (m === 'Please enter valid email address.') {
                    alert('Please enter valid email address.')
                };
                if (m === 'Passwords do not match.') {
                    alert('Passwords do not match.')
                };
            })
            .catch((response) => {
                console.log(response.data);
            })
        setNickname('');
        setEmail('');
        setPassword('');
        setPassword2('');
    }

    // let navigate = useNavigate();
    // function signInClick() {
    //     navigate('/signin')
    // }

    return (
        // onClick={signInModalOn ? signInClickHandler:null}
        <div>
            <Signin modalOpen={signInModalOn} closeModal={setSignInModalOn}/>
            <header>
                <LogoRed />
                <button className='signin-btn' onClick={signInClickHandler}>sign in</button>
            </header>
            <body>
                <div className='wrapper'>
                    <div></div>
                    <div className='signup'>
                        <div className='signup-text'>Share your mood.</div>
                        <div className='signup-components'>
                            <div className='text-box'><Form text={text[0]} type='text' value={nickname} onChange={nicknameHandler} /></div>
                            <div className='text-box'><Form text={text[1]} type='email' value={email} onChange={emailHandler} /></div>
                            <div className='text-box'><Form text={text[2]} type='password' value={password} onChange={passwordHandler} /></div>
                            <div className='text-box'><Form text={text[3]} type='password' value={password2} onChange={password2Handler} /></div>
                            <div className='btns'>
                                <button className='signup-btn' type='submit' onClick={onClick}>SIGN UP</button>
                                <button><img className='google' src={google} /></button>
                            </div>
                        </div>
                    </div>
                    <div></div>
                    <div className='img-area'>
                        <img className='temp-img' src={tempimg} />
                    </div>
                    <div></div>
                </div>
            </body>
        </div>
    );
}

export default Signup;
