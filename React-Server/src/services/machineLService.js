import {Component} from 'react'
import axios from 'axios';

class MLService extends Component{

    getClassifications(postedData){
        return axios.post('http://localhost:5000/api/classify', postedData);
    }
}

export default new MLService();