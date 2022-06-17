import React from 'react'
import { useNavigate } from 'react-router-dom';

import './AddSong.css'

import Header from '../../components/Header/Header';

import confirm from '../../svg/add-confirm-btn.svg'
import search from '../../svg/search.svg'
import japanPop from '../../image/japanPop.jpeg'

function AddSong() {

    let navigate = useNavigate();
    const toProfile = () => {
        navigate("/profile")
    }

    function ByteCheck(maxByte) {
        const text_val = document.getElementsByClassName("caption-input")[0].value
        const text_len = text_val.length
        var totalByte = 0
        for (let i= 0; i < text_len; i++) {
            totalByte += 1;
            console.log(totalByte)
        }

        if (totalByte > maxByte) {
            alert('Only maximum 100 Byte.')
            document.getElementById("nowByte").innerText = totalByte;
            document.getElementById("nowByte").style.color = "red";
        } else {
            document.getElementById("nowByte").innerText = totalByte;
            document.getElementById("nowByte").style.color = "green";
        }
    }

    return (
        <div className="entire-addsong-page">
            <Header />
            <div className="addsong-body">
                <div className="search-bar">
                    <div className="icon-background">
                        <img src={search} alt="" className="search-icon" />
                    </div>
                    <input type="text" className="search-input" placeholder='Search songs by track title or artist name...' />
                </div>
                <div className="cover-caption-section">
                    <img src={japanPop} alt="" className="sample-cover" />
                    <div className="caption-section">
                        <textarea name="" id="" cols="30" rows="10" className="caption-input" placeholder='Write a caption about your curation...' onKeyUp={() => ByteCheck(100)} onKeyDown={() => ByteCheck(100)} />
                        <div className="byte-btn-section">
                            <div className="byte-check">
                            <span id="nowByte">0</span> / 100 bytes
                            </div>
                            <img src={confirm} alt="" className="add-confirm-btn" onClick={toProfile} />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AddSong;