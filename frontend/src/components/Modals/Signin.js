import axios from 'axios';
import React, { useState } from 'react';
import { CloseButton } from '@chakra-ui/react'

import Form from '../Form/Form';

import google from '../../svg/google.svg'
import close from '../../svg/gg_close.svg'

import './Signin.css'

function Signin(props) {

    const [text, textChange] = useState(['Email', 'Password'])

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')

    const closeModal = () => {
        props.closeModal(false)
    }

    const emailHandler = (event) => {
        setEmail(event.target.value);
    }

    const passwordHandler = (event) => {
        setPassword(event.target.value);
    }

    const onClick = (event) => {
        event.preventDefault();

        if (email === "" || password === "") {
            setError("Fields are required")
            return;
        }


        axios
            .post("http://localhost:8000/accounts/signin/", {
                "email": email,
                "password": password
            })
            .then((response) => {
                console.log(response.data);
                var d = (response.data);
                var s = (response.status);
                if (s === 200) {
                    localStorage.clear()
                    localStorage.setItem('token', d.Token)
                    // console.log(localStorage)
                    // console.log('Success')
                }
                if (d.message === 'User is not active') {
                    alert('User is not active')
                }
                if (d.message === 'User does not exist') {
                    alert('User does not exist')
                }
            })

        setEmail('');
        setPassword('');
        // modalClose();
    }


    return (
        <div className={props.modalOpen? 'open-container':'close-container'}>
            <div className='modal'>
                <img className='close-btn' src={close} onClick={closeModal} />
                <br />
                <br />
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
