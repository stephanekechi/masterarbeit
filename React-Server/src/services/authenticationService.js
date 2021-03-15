import {Component} from 'react';
import axios from 'axios';

class AuthenticationService extends Component {
    
    constructor(props){
        super(props);

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

    retrieveUserData(postedData){
        return axios.post('http://localhost:5000/api/user/auth',postedData);
    }

    logout(){
        sessionStorage.removeItem('authenticatedUser');
    }
}

export default new AuthenticationService();