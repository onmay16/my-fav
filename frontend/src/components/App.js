// import './App.css';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Signup from "../pages/Signup/Signup.js";
import Splash from '../pages/Splash/Splash.js';
import Signin from "./Modals/Signin.js";

function App() {
  return (
    <Router>
        <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/signup" element={<Signup />} /> 
        <Route path="/signin" element={<Signin />} />
      </Routes>
    </Router>
  );
}

export default App;
