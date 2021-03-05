import React, {Component} from 'react';
import {Route, Redirect} from 'react-router-dom';
import AuthenticationService from '../services/authenticationService';

class AuthenticatedRoute extends Component{
    render(){
        return AuthenticationService.isUserLoggedIn ? (
            <Route {...this.props}/>
        ) : (
            <Redirect to="/login"/>
        );
    }
}

export default AuthenticatedRoute;