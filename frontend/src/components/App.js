// import './App.css';
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from 'react-redux'

import Splash from '../pages/Splash/Splash.js';
import Main from "../pages/Main/Main.js";
import Start from "../pages/Start/Start.js"
import Profile from '../pages/Profile/Profile.js';
import AddSong from '../pages/AddSong/AddSong.js';
import Message from '../pages/Message/Message.js';
import Settings from '../pages/Settings/Settings.js';
import Edit from './Modals/Edit.js';
import PostDetail from './Modals/PostDetail.js'
import Followers from './Modals/Followers.js'
import Following from './Modals/Following.js'

function App() {

  return (
    // <Router basename={process.env.PUBLIC_URL}>
    <Router>
      <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/main" element={<Main />} />
        <Route path="/start" element={<Start />} />
        <Route path="/:nickname" element={<Profile />} />
        <Route path="/add" element={<AddSong />} />
        <Route path="/message" element={<Message />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/edit" element={<Edit />} />
        <Route path="/detail" element={<PostDetail />} />
        <Route path="/followers" element={<Followers />} />
        <Route path="/following" element={<Following />} />
      </Routes>
    </Router>
  );
}

export default App;
