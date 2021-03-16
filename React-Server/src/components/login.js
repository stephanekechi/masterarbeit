import React, {Component} from 'react';
import AuthenticationService from '../services/authenticationService';

class LoginCom extends Component {

    constructor(props){
        super(props)

        this.state = {
            username: 'Enter Username',
            password: 'Enter Password',
            hasLoginFailed: false,
            alertMessage: '',
            alertMessageClass: ''
        };

        this.handlerInputChange = this.handlerInputChange.bind(this);
        this.loginClicked = this.loginClicked.bind(this);
    }

    handleSuccessfullLogin(username){
        if(username === ''){
            this.handleFailLogin();
        }else{
            this.setState({hasLoginFailed: false});
            sessionStorage.setItem('authenticatedUser', username);
            this.props.history.push(`/welcome/${username}`);
        }
    }

    handleFailLogin(){
        this.setState(
            {
                hasLoginFailed: true,
                alertMessage: 'Invalid Credentials',
                alertMessageClass: 'alert alert-warning'
            });
    }

    handleError(){
        this.setState(
            {
                hasLoginFailed: true,
                alertMessage: 'An error occured while processing your request',
                alertMessageClass: 'alert alert-danger'
            });
    }

    handlerInputChange(event){
        this.setState(
            {
                [event.target.name]:
                    event.target.value
            }
        )
    }

    async loginClicked(){
        this.logMessage(this.state.username + ' ' + this.state.password);
        await AuthenticationService.retrieveUserData({
                username: this.state.username,
                password: this.state.password
            })
            .then(response => this.handleSuccessfullLogin(response.data.username))
            .catch(err => {
                if(err) {
                    this.handleError();
                    this.logMessage(err);
                }
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
                    {this.state.hasLoginFailed && <div className={this.state.alertMessageClass}>{this.state.alertMessage}</div>}
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