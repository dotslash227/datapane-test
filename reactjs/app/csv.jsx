import React from 'react';
import ReactDOM from 'react-dom';
import Papa from 'papaparse';

class CSVReader extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            csvfile: undefined,
            data: undefined
        }
        this.handleFile = this.handleFile.bind(this);      
        this.importCSV = this.importCSV.bind(this);        
    }

    handleFile(event){
        // Function to handle the file upload event and store it in the state
        this.setState({csvfile:event.target.files[0]});        
    };

    importCSV(){        
        // Importing CSV and storing the data into state using Papaparse
        const {csvfile} = this.state;        
        console.log("importsing csv", csvfile);
        Papa.parse(csvfile, {
            complete: (result)=>{                
                let data = result.data;
                this.setState({data})
                console.log(this.state.data);
            },            
        })        
    };    

    renderTable(){
        // Method to render table from the data array
        const {data} = this.state;
        if (data){
            return(
                <table className="table-data table table-striped table-responsive">
                    {data.map((parentList, i)=>{
                        return(
                            <tr key={i}>
                                {parentList.map((item, j)=>{
                                    return <td key={j}>{item}</td>
                                })}
                            </tr>
                        )
                    })}
                </table>                
            )
        }                
    }

    render(){
        return(
            <div>
                <div className="reader">
                    <form name="csv">
                        <p>Select csv file: </p><input type="file" name="file" onChange={this.handleFile} />
                    </form>
                    <button onClick={this.importCSV}>Upload Now</button>
                </div>            
                <div className="data">
                    {this.renderTable()}                    
                </div>
            </div>            
        )
    }
}

ReactDOM.render(<CSVReader />, document.getElementById("csv"))