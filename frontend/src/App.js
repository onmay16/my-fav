// import './App.css';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Signup from "./pages/Signup/Signup.js";
import Splash from './pages/Splash/Splash.js';

function App() {
  return (
    <Router>
        {/* <Navbar /> */}
        <Routes>
        <Route path="/" element={<Splash />} />
        {/* <Route path="/home" element={<Home />} />*/}
        <Route path="/signup" element={<Signup />} /> 
      </Routes>
    </Router>
  );
}

export default App;
