import React from 'react'
import './styles.scss'
// import {useState} from 'react';
// import Register from "../Resister/Register.js"
import {useNavigate} from 'react-router-dom'

function Button({color , text , functionName , BeforeLogo ,BeforeLogoAlt, AfterLogo , AfterLogoAlt , IconExists}) {
  const navigate= useNavigate();


  const StartNow = (e) =>{
    console.log(e.target.innerText);
    switch(e.target.innerText) {
      case "Start Now":
        navigate("/Register");
        break;
      case "Close":
        navigate("/");
        break;
      default:
        // code block
    }
 
  }

  return (
    <button className={color} onClick={(e)=>StartNow(e)}>
      <img className='buttonIcon' src={BeforeLogo} alt={BeforeLogoAlt}/>
       {text}
      <img className='buttonIcon' src={AfterLogo} alt={AfterLogoAlt}/>
    </button>
  )
}

export default Button