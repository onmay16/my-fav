import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import spotifyWebApi from "spotify-web-api-js";
import axios from 'axios';
import qs from 'qs';

import './AddSong.css'

import Header from '../../components/Header/Header';
import { clientId, clientSecret } from '../../spotifyClientSecret';

import confirm from '../../svg/add-confirm-btn.svg'
import search from '../../svg/search.svg'
import nullImage from '../../svg/null.svg'

function AddSong() {

    const [showModal, setShowModal] = useState(false);

    const [selectedTitle, setSelectedTitle] = useState('');
    const [selectedArtist, setSelectedArtist] = useState('');
    const [selectedCover, setSelectedCover] = useState(nullImage);
    const [child, setChild] = useState([]);

    // const userHandler = (user) => {
    //     setUser(user);
    // }

    let navigate = useNavigate();
    const toProfile = () => {
        axios.get("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/user/")
        // axios.get("http://localhost:8000/playlist/user/")
        .then((response) => {
            console.log(response.data);
            navigate("/"+ response.data.profile.nickname);
        }).catch((error) => {
            console.log(error);
        })
    }

    function parentModalHanlder(e) {
        setShowModal(false);
    }
    function childModalHanlder(e) {
        e.stopPropagation();
        if (document.getElementsByClassName('search-input')[0].value.length === 0) {
            const searchResultList = document.getElementsByClassName('search-result-list');
            searchResultList[0].innerHTML = `<div className="empty-list-text" style="padding-top: 20px; margin: auto; font-size: medium; color: #222222;"> ----- 🎧 ♩ ♫ ♪ ♪ ♬ ----- <br />&nbsp;</div>`
        }
        setShowModal(true);
    }

    function ByteCheck(maxByte) {
        const text_val = document.getElementsByClassName("caption-input")[0].value;
        const text_len = text_val.length
        var totalByte = 0
        for (let i = 0; i < text_len; i++) {
            totalByte += 1;
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

    var spotifyApi = new spotifyWebApi({});

    function getToken() {
        const data = {
            grant_type: 'client_credentials',
        };

        const headers = {
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            auth: {
                username: clientId,
                password: clientSecret,
            },
        };

        axios.post(
            'https://accounts.spotify.com/api/token',
            qs.stringify(data),
            headers
        ).then(function (response) {
            // console.log(response.data)
            spotifyApi.setAccessToken(response.data.access_token)
            // setExpirationTime(expirationTime + response.data.expires_in)
            // console.log(expirationTime)
        }).catch(function (error) {
            console.log(error)
        })
    }

    function selectTrack(e) {
        let id = this.id;
        setSelectedTitle(document.getElementsByClassName('track'+id)[0].innerText);
        setSelectedArtist(document.getElementsByClassName('artist'+id)[0].innerText);
        setSelectedCover(document.getElementsByClassName('album-art'+id)[0].src);
        console.log(selectedTitle + " " + selectedArtist + " " + selectedCover);

        setShowModal(false);
    }

    function getMusicHtml(art, title, artist, number) {

        const searchResultList = document.getElementsByClassName('search-result-list');

        const child = document.createElement('div')
        child.setAttribute('id', number)
        child.setAttribute('class', 'individual')
        child.addEventListener('click', selectTrack)

        child.innerHTML =
                `<img src=${art} alt="" class="album-art album-art${number}" />
                <div class="individual-info individual-info${number}">
                    <div class="track track${number}">${title}</div>
                    <div class="artist artist${number}">${artist}</div>
                </div>`
        if (art !== null) {
            searchResultList[0].appendChild(child);
        } else {
            return
        }
    }

    function addMusicList() {

        setShowModal(true);

        const searchResultList = document.getElementsByClassName('search-result-list');
        while (searchResultList[0].firstChild) {
            searchResultList[0].removeChild(searchResultList[0].firstChild)
        }
        var word = document.getElementsByClassName('search-input')[0].value;

        spotifyApi.searchTracks(word)
            .then(function (response) {
                let musicList = response.tracks.items;
                for (let i = 0; i < musicList.length; i++) {
                    let albumTitle = musicList[i]["name"]
                    let albumArtist = musicList[i]["artists"][0]["name"]
                    let albumCover = musicList[i]["album"]["images"][0]["url"]
                    getMusicHtml(albumCover, albumTitle, albumArtist, i)
                }
            }).catch(function (error) {
                console.log(error)
            })

        if (word.length === 0) {
            setShowModal(false);
            const searchResultList = document.getElementsByClassName('search-result-list');
            searchResultList.innerHTML = `<div className="empty-list-text"> ----- 🎧 ♩ ♫ ♪ ♪ ♬ ----- <br />&nbsp;</div>`
        }
    }

    function submitPost() {
        axios.post("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/post/", {
        // axios.post("http://localhost:8000/playlist/post/", {
            "track": selectedTitle,
            "artist": selectedArtist,
            "jacket": selectedCover,
            "content": document.getElementsByClassName("caption-input")[0].value
        }).then(function (response) {
            console.log(response);
            toProfile();
        }).catch(function (error) {
            console.log(error);
            alert(error);
        })
    }

    useEffect(() => {

        getToken();

    }, [])

    return (
        <div className="entire-addsong-page" onClick={parentModalHanlder}>
            <Header />
            <div className="addsong-body">
                <div className="search-section">
                    <div className="search-bar">
                        <div className="icon-background">
                            <img src={search} alt="" className="search-icon" />
                        </div>
                        <input type="text" className="search-input" placeholder='Search songs by track title or artist name...' onKeyUp={addMusicList} onKeyDown={addMusicList} onChange={addMusicList} autoComplete='off' onClick={childModalHanlder} />
                    </div>
                    <div className="search-result-list" style={{display: showModal? 'flex':'none'}}>
                        <div className="empty-list-text"> ----- 🎧 ♩ ♫ ♪ ♪ ♬ ----- <br />&nbsp;</div>
                        {child}
                    </div>
                </div>
                <div className="cover-caption-section">
                    <img className="sample-cover" src={selectedCover}/>
                    <div className="caption-section">
                        <div className="selected-song-info">
                            <div className="selected-song-title">{selectedTitle}</div>
                            <div className="selected-song-artist">{selectedArtist}</div>
                        </div>
                        <textarea name="" id="" cols="30" rows="10" className="caption-input" placeholder='Write a caption about your curation...' onKeyUp={() => ByteCheck(100)} onKeyDown={() => ByteCheck(100)} />
                        <div className="byte-btn-section">
                            <div className="byte-check">
                                <span id="nowByte">0</span> / 100 bytes
                            </div>
                            <img src={confirm} alt="" className="add-confirm-btn" onClick={submitPost} />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AddSong;