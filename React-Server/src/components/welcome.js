import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class WelcomeCom extends Component{

    render(){
        return (
            <div>
                <div className="container">
                    Welcome {!this.props && this.props.match.params.name}
                    <p>Here the Menu</p>
                    <Link to="/factcheck">Fact chech information</Link>
                </div>
            </div>
        );
    }
}

export default WelcomeCom;