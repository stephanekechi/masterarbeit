import React, {Component} from 'react';
import {BrowserRouter as Router} from 'react-router-dom';
//import logo from './logo.svg';
import RoutingCom from './components/routingCom';
import AuthenticationService from './services/authenticationService';
import HeaderCom from './components/layout_header';
import FooterCom from './components/layout_footer';
import './App.css';
import './bootstrap.css';

class App extends Component {

  constructor(props){
        super(props)

        this.state = {
            username: AuthenticationService.getLoggedUser(),
            isLoggedIn: AuthenticationService.isUserLoggedIn()
        };

        this.logout = this.logout.bind(this);
        //this.login = this.login.bind(this);
  }

  logout(){
      AuthenticationService.logout();
      this.setState({isLoggedIn: AuthenticationService.isUserLoggedIn()});
      //this.props.history.push('/login');
  }

  componentDidMount(){
    this.setState({isLoggedIn: AuthenticationService.isUserLoggedIn()});
  }

  render(){
    return (
      <div className="App">
        <Router>
          <>
            <HeaderCom
              isLoggedIn = {this.state.isLoggedIn}
              logout = {this.logout}
              />
              <RoutingCom />
            <FooterCom/>
          </>
        </Router>
      </div>
    );
  }
  
}

export default App;
