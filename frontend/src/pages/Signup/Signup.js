import React, { useState } from 'react';
import axios from 'axios';
import { useAsync } from 'react-async';

import tempimg from '../../svg/music-player.svg'
import google from '../../svg/google.svg'

import './Signup.css'

import LogoRed from '../../components/LogoRed/LogoRed.js';
import Form from './Form.js'
import useInput from '../../hooks/useInput';
import fetcher from '../../utils/fetcher';



function Signup() {

    const [text, textChange] = useState(['Nickname', 'Email', 'Password', 'Password Confirmation']);

    const [email, setEmail] = useInput('');
    const [nickname, setNickname] = useInput('');
    const [password, setPassword] = useInput('');
    const [password2, setPassword2] = useInput('');

    const [emailCheck, setEmailCheck] = useState(false);
    const [pwCheck, setPwCheck] = useState(false);

    // const router = useRouter();

    // const onSubmitNewStudent = async (e) => {
    //     e.preventDefault();
    //     // if ('@' ) return alert('아이디는 6자리 이상이어야 합니다.');
    //     // if (!isDonePwCheck) return alert('패스워드를 일치시켜주세요.');
    //     // if (parentInfo?.length > 13 || parentInfo?.length < 9) return alert('부모님 연락처를 확인해주세요.');
    //     try {
    //         let obj = {
    //             "email": email,
    //             "nickname": nickname,
    //             "password": password,
    //             "password2": password2,
    //         };

    //         const data = await fetcher('post', '/accounts/signup/', obj);
    //         console.log(data);
    //         if (data.message === "STUDENT_REGISTER_SUCCESS") {
    //             setStudents(prev => [{ ...obj, id: prev?.length + 1, student_register_date: getDate() }, ...prev]);
    //             setStudents(prev => {
    //                 return [{ ...obj, id: prev?.length + 1, student_register_date: getDate() }, ...prev]
    //             });
    //             resetAllInputs();
    //             router.reload();
    //             return alert('회원가입을 성공했습니다.');
    //         }
    //         if (data.data.message === 'USERNAME_DUPLICATE_EXIST') return alert('중복된 아이디입니다');
    //         if (data.message === 'PLEASE_LOGIN_FIRST') return alert('로그인 먼저 해주세요.');
    //         if (data.message === 'USER_DOES_NOT_EXIST') return alert('문제가 발생했습니다.');
    //         if (data.data.message === 'PLEASE_FILL_OUT_THE_FORM') return alert('모든 곳에 입력을 해주세요.');
    //         if (data.message === 'USERNAME_DUPLICATE_EXIST') return alert('중복된아이디가 존재합니다.');
    //         if (data.message === 'PASSWORD_CHECK_ERROR') return alert('비밀번호를 확인해주세요.');
    //         if (data.message === 'SCHOOL_NAME_DEOS_NOT_EXIST') return alert('존재하지 않는 학교 이름입니다.');
    //         if (data.message === 'CLASS_NAME_DEOS_NOT_EXIST') return alert('존재하지 않는 학급 이름입니다.');
    //         return alert('문제가 발생했습니다.');
    //     } catch (e) {
    //         console.log(e);
    //         alert('문제가 발생했습니다');
    //     }
    //     resetAllInputs();
    // };

    return (
        <div>
            <header>
                <LogoRed />
                <button className='signin-btn'>sign in</button>
            </header>
            <body>
                <div className='wrapper'>
                    <div className='signup'>
                        <div className='signup-text'>Share your mood.</div>
                        <div className='signup-components'>
                            <div className='text-box'>{Form(text[0])}</div>
                            <div className='text-box'>{Form(text[1])}</div>
                            <div className='text-box'>{Form(text[2])}</div>
                            <div className='text-box'>{Form(text[3])}</div>
                            <div className='btns'>
                                <button className='signup-btn'>SIGN UP</button>
                                <button><img className='google' src={google} /></button>
                            </div>
                        </div>
                    </div>
                    <div></div>
                    <div className='img-area'>
                        <img className='temp-img' src={tempimg} />
                    </div>
                </div>
            </body>
        </div>
    );
}

export default Signup;
