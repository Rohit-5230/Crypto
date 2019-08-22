import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Home from './Home';
import wallet from './wallet';

export default class App extends Component {
  render() {
    return (

      <div className="container">
        <nav className="navbar navbar-default" id="colorful-nav">
          <div >
            <Router>
              <div className="collapse navbar-collapse" id="myNavbar">
                <ul className="nav navbar-nav">
                  <li className="home"><Link to={'/Home'}><span className="glyphicon glyphicon-home"></span><h5>HOME</h5></Link></li>
                  <li className="about"><Link to={'/about'}><span className="glyphicon glyphicon-info-sign"></span><h5>ABOUT</h5></Link></li>
                  <li className="profile"><Link to={'/name'}><span className="glyphicon glyphicon-user"></span><h5>NAME</h5></Link></li>
                  <li className="statistics"><Link to={'/wallet'}><span className="glyphicon glyphicon-stats"></span><h5>MY WALLET</h5></Link></li>
                </ul>
                <br />
                <Switch>
                  <Route exact path='/Home' component={Home} />
                  <Route exact path='/wallet' component={wallet} />

                </Switch>
              </div>
            </Router>
          </div>
        </nav>
      </div>
    );

  }
}
