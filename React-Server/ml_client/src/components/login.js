import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import AuthenticationService from '../services/authenticationService';

class LoginCom extends Component {

    constructor(props){
        super(props)

        this.state = {
            username: '"enter username"',
            password: '',
            hasLoginFailed: false
        };

        this.handlerInputChange = this.handlerInputChange.bind(this);
        this.loginClicked = this.loginClicked.bind(this);
    }

    handleSuccessfullLogin(username){
        sessionStorage.setItem('authenticatedUser', username);
        this.props.history.push(`/welcome/${username}`);
    }

    handleFailLogin(username){
        this.setState({hasLoginFailed: true});
    }

    handlerInputChange(event){
        this.setState(
            {
                [event.target.name]:
                    event.target.value
            }
        )
    }

    loginClicked(){
        this.logMessage(this.state.username + ' ' + this.state.password);
        AuthenticationService.retrieveUserData(this.state.username, this.state.password)
            .then(response => this.handleSuccessfullLogin(response.data.username))
            .catch(err => {
                if(err) this.logMessage(err);
            });
    }

    logMessage(message){
        console.log(message);
    }

    render() {
        return (
            <div>
                <h1>Login</h1>
                <div className="container">
                    {this.state.hasLoginFailed && <div className="alert alert-warning">Invalid Credentials</div>}
                    User Name: <input type="text" name="username" value={this.state.username}
                        onChange={this.handlerInputChange}/>
                    Password: <input type="password" name="password" value={this.state.password}
                        onChange={this.handlerInputChange}/>
                    <button className="btn btn-success" onClick={this.loginClicked}>Login</button>
                </div>
            </div>
        )
    }
}

export default LoginCom;