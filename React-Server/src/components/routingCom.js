import React, {Component} from 'react';
import {Switch, Route, Redirect} from 'react-router-dom';
import LoginCom from './login';
import SearchCom from './search';
import ErrorCom from './error';
import WelcomeCom from './welcome';
import AuthenticatedRoute from './authenticatedRoute';

class RoutingCom extends Component{

    render(){
        return (
            <Switch>
                <AuthenticatedRoute path="/" exact component={WelcomeCom}></AuthenticatedRoute>
                <Route path="/login" component={LoginCom}></Route>
                <Route path="/logout">
                    <Redirect to="/login"/>
                </Route>
                <AuthenticatedRoute path="/welcome"
                    component={()=> <WelcomeCom />}>
                </AuthenticatedRoute>
                <AuthenticatedRoute path="/welcome/:username" component={WelcomeCom}></AuthenticatedRoute>
                <AuthenticatedRoute path="/factcheck" component={SearchCom}></AuthenticatedRoute>
                <Route component={ErrorCom}></Route>
            </Switch>
        );
    }
}

export default RoutingCom;
