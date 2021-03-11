import React, {Component} from 'react'

class ErrorCom extends Component{

    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className="error">
                An Error Occured. Please double check the path
            </div>
        );
    }
}

export default ErrorCom;