import React from 'react';
import './styles.scss'
import 'bootstrap/dist/css/bootstrap.min.css';
import Chat from '../Chat/chat';
import HomeSecuraLogoMobile from "../Resister/assets/HomeSecuraLogoMobile.svg"
import MoreOption from "./assets/MoreOption.svg"
import Button from '../Buttons/Button';
import SendMessage from "./assets/SendMessage.svg"

const Chats = () => {
  return(
    <div className='Chats container mt-2'>
      <nav className='d-inline-flex container topBar align-content-around navbar sticky-top '>
          <div className='d-flex flex-row align-self-start'>
                <img src={HomeSecuraLogoMobile} alt='HomeSecura Logo' className='m-2' />
                <h2>HomeSecura</h2>
          </div>
          <div className='d-flex flex-row-reverse '>
            <div className='MoreOption'>
                <img src={MoreOption} alt=' MoreOption' />
             </div>
          </div>
      </nav>
      <div className='d-flex flex-column'>
          <Chat/>
          <Chat/>
      </div>
      <div className="FixSendMsgForm">
        <form className='MessageTypingBar'>
              <div className='d-inline-flex container'>
                  <textarea autocorrect="on" id="story" name="story" rows="5" cols="100">Start typing to interact with HomeSecura...</textarea>
                  <Button text="Send" AfterLogo={SendMessage} AfterLogoAlt={"Send Message Logo"} className="logoType" />
              </div>
        </form>
      </div>
    </div>
  );
}


export default Chats