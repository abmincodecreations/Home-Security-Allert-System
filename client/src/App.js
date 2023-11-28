import React from 'react';
import "./app-Styles.scss";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
//import {Login, Signup} from './components/LoginSignup.js'
import LandingPage from './components/LandingPage/LandingPage.js';
import Register from './components/Resister/Register.js';
import {Routes, Route} from 'react-router-dom';
import Chats from './components/Chats/Chats.js'

const App = () =>{

  return (
    
    <main className='App body'>
      <Routes>
          <Route path="/Register" element={<Registerr />} />
          <Route path="/" element={<LandingPagee/>} />
          <Route path="/Chats" element={<Chatss/>} />
      </Routes>

    </main>
  );
}
function Registerr() {
  return <Register/>;
}

function LandingPagee() {
  return <LandingPage/>;
}
 function Chatss(){
  return <Chats/>;
 }

export default App
