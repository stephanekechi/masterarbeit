import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class HeaderCom extends Component{
    constructor(props){
          super(props)
          console.log(props.isLoggedIn);

    }

    render(){
        return (
            <header>
                <nav className="navbar navbar-expand-md navbar-dark bg-dark">
                    <div><a href="/welcome" className="navbar-brand">Fact check App</a></div>
                    <ul className="navbar-nav navbar-collapse justify-content-end">
                        {!this.props.isLoggedIn && <li><Link className="nav-link" to="/login">Login</Link></li>}
                        {this.props.isLoggedIn && <li><Link className="nav-link" to="/logout" onClick={this.props.logout}>Logout</Link></li>}
                    </ul>
                </nav>
            </header>
        );
    }
}

export default HeaderCom;