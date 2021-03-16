import React, {Component} from 'react';
import MLService from '../services/machineLService.js';

class SearchCom extends Component{

    constructor(props){
        super(props);

        this.state = {
            text: "WASHINGTON (Reuters) - The special counsel investigation of links between Russia and President Trump’s 2016 election campaign " +
                "should continue without interference in 2018, despite calls from some Trump administration allies and Republican lawmakers to shut it down, a " +
                "prominent Republican senator said on Sunday.",
            date: '',
            title: "Senior U.S. Republican senator: 'Let Mr. Mueller do his job'",
            hasRequestFailed: false,
            isRequestLoading: false,
            classificationObj: null
        };

        this.handlerInputChange = this.handlerInputChange.bind(this);
        this.handelClassificationCall = this.handelClassificationCall.bind(this);
        this.convertStrToPercent = this.convertStrToPercent.bind(this);
    }

    async handelClassificationCall(){
        if(this.state.text === '' || this.state.title === ''){
            this.setState({hasRequestFailed: true});
        }else{
            this.setState({isRequestLoading: true});
            let requestResponse = await MLService.getClassifications({
                    title: this.state.title,
                    text: this.state.text,
                    date: this.state.date
                })
                .then(response => {
                    return response.data;
                })
                .catch(err => {
                    this.setState({hasRequestFailed: true});
                    if(err) this.logMessage(err);
                });
            
            console.log(requestResponse);
            this.setState({
                classificationObj: requestResponse,
                isRequestLoading: false
            });
            
        }
    }

    handlerInputChange(event){
        this.logMessage(event.target.value);
        this.setState(
            {
                [event.target.name]:
                    event.target.value
            }
        )
    }

    convertStrToPercent(strFloatNumber){
        if(strFloatNumber === ''){
            return '0 %';
        }else{
            let percentNumber = parseFloat(strFloatNumber) * 100
            if(isNaN(percentNumber)){
                return '0 %';
            }else{
                return percentNumber.toString() + ' %';
            }
        }
    }

    logMessage(message){
        console.log(message);
    }

    render(){
        return (
            <div>
                <h1>Fact Checking Page</h1>
                <div className="container">
                    <br/>
                    <br/>

                    {this.state.hasRequestFailed && <div className="alert alert-warning">The Submittion of the form failed</div>}
                    Article Date: <input type="date" name="date" value={this.state.date}
                        onChange={this.handlerInputChange}/>
                    <br/>
                    <br/>

                    Article Title: <input type="text" name="title" value={this.state.title}
                        onChange={this.handlerInputChange}/>
                    <br/>
                    <br/>

                    <label>
                        Article Text:
                        <textarea value={this.state.text} name="text" rows="6" cols="60"
                            onChange={this.handlerInputChange} />
                    </label>
                    <br/>
                    <br/>
                    <button className="btn btn-success" onClick={this.handelClassificationCall}>Submit</button>
                </div>
                <br/>
                <br/>
                {this.state.isRequestLoading &&
                    <div>
                        The server is still processing your request ...
                        It could take up to 4 Minutes!
                    </div>
                }
                {this.state.classificationObj &&
                    <div>
                        <table className="table">
                            <thead>
                                <tr>
                                    <th>Algorithm</th>
                                    <th>Classification Result</th>
                                    <th>Accuracy</th>
                                </tr>
                            </thead>
                            <tbody>
                                {this.state.classificationObj.map((obj, index) => 
                                    <tr key={index}>
                                        <td>{obj.description}</td>
                                        <td>{obj.prediction}</td>
                                        <td>{this.convertStrToPercent(
                                                obj.report.substring(
                                                    obj.report.length-20,
                                                    obj.report.length-7
                                                )
                                            )
                                        }</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                }
            </div>
        );
    }
}

export default SearchCom;