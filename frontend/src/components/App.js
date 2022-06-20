// import './App.css';
import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Signup from "../pages/Signup/Signup.js";
import Splash from '../pages/Splash/Splash.js';
import Signin from "./Modals/Signin.js";
import Main from "../pages/Main/Main.js";
import Start from "../pages/Start/Start.js"
import Profile from '../pages/Profile/Profile.js';
import AddSong from '../pages/AddSong/AddSong.js';
import Message from '../pages/Message/Message.js';
import Settings from '../pages/Settings/Settings.js';

function App() {

  return (
    <Router basename={process.env.PUBLIC_URL}>
      <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/main" element={<Main />} />
        <Route path="/start" element={<Start />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/add" element={<AddSong />} />
        <Route path="/message" element={<Message />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
}

export default App;
