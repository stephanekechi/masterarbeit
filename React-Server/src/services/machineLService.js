import React, {Component} from 'react'
import axios from 'axios';

class MLService extends Component{

    constructor(props){
        super(props);
    }

    getClassifications(postedData){
        return axios.post('http://localhost:5000/api/classify', postedData);
    }
}

export default new MLService();