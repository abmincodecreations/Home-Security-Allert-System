import React from "react"
import HomeSecuraLogo from './images/HomeSecuraLogo.png'
import HeroImg from './images/HeroImg.png'
//*import Form from './components/Form/form.js';
//import Chats from './components/Chats/Chats.js';
import Button from '../Buttons/Button';
import "./LandingPage.scss"
// import  Register from '../Resister/Register.js'

function LandingPage() {

  return (
    <div id="LandingPage">
      <div className='body'>
            <div class="container">
            <img className='HomeSecuraLogo1' src={HomeSecuraLogo} alt={HomeSecuraLogo} />
                <div className="row">
                      <div class="col-9 col-md-6 m-1">
                      <h1 className='Bold-Hero-Text'>Bringing Security Of Your Home to Your Figure Tips With 
                        <span className='boldText'> HomeSecura</span><br/>
                          <div className="row justify-content-start">
                              <div class="col-12">
                              <Button color="primary"  text="Start Now"  />
                              </div>
                          </div>
                      </h1>
                      </div>
                      <div class="col-10 col-lg-4 m-1 justify-content-end">
                      <img className='img-fluid hero-img d-sm-flex d-md-flex flex-md-row-reverse' src={HeroImg} alt={HeroImg} style={{zIndex:1}} />
                      </div>
                 </div>
             </div>
       </div>
          <footer class="page-footer footer-landing " >
            <div class="footer-copyright text-center py-3">© 2020 Copyright:
              <a href="/"> HomeScecura</a>
            </div>
          </footer>
    </div>
  )
}

export default LandingPage