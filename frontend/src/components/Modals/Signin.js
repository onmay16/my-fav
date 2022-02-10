import axios from 'axios';
import React, { useState } from 'react';
import Form from '../Form/Form';

import google from '../../svg/google.svg'

import './Signin.css'

function Signin(props) {

    const [text, textChange] = useState(['Email', 'Password'])

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    console.log('singin page val:', props.modalOpen)

    const emailHandler = (event) => {
        setEmail(event.target.value);
    }

    const passwordHandler = (event) => {
        setPassword(event.target.value);
    }

    const onClick = (event) => {
        event.preventDefault();

        axios
            .post("http://localhost:8000/accounts/signin/", {
                "email": email,
                "password": password
            })
            .then((response) => {
                console.log(response.data);
                var m = (response.data.message);
                if (m === 'User is not active') {
                    alert('User is not active')
                }
                if (m === 'User does not exist') {
                    alert('User does not exist')
                }
            })
            .catch((response) => {
                console.log(response.data);
            })
        setEmail('');
        setPassword('');
        // modalClose();
    }


    return (
        <div className={props.modalOpen? 'open-container':'close-container'}>
            <div className='modal'>
                <div className='input-box'><Form text={text[0]} type='email' value={email} onChange={emailHandler} /></div>
                <div className='input-box'><Form text={text[1]} type='password' value={password} onChange={passwordHandler} /></div>
                <div className='btns'>
                    <button className='signin' type='submit' onClick={onClick}>SIGN IN</button>
                    <button><img className='google' src={google} /></button>
                </div>
            </div>
        </div>
    );
}

export default Signin;
