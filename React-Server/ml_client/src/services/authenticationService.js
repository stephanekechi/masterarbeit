import {Component} from 'react';
import axios from 'axios';

class AuthenticationService extends Component {
    
    constructor(props){
        super(props);

    }

    makeServerRequest(username, password){
        let user = axios.get()
    }

    isUserLoggedIn(){

        let loggedUser = sessionStorage.getItem('authenticatedUser');
        if(loggedUser === null){
            return false;
        }else{
            return true;
        }
    }

    getLoggedUser(){
        return sessionStorage.getItem('authenticatedUser');
    }

    retrieveUserData(username, password){
        return axios.get('http://localhost:5000/test');
    }

    logout(){
        sessionStorage.removeItem('authenticatedUser');
    }
}

export default new AuthenticationService();