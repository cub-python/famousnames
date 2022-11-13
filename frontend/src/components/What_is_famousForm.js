import React from "react";

class What_is_famousForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', names: 0}
    }

    handleUserChange(event){
        if(!event.target.selectedOptions){
            this.setState({
                'name':[]
            })
            return;
        }

        let  names = []
        for (let i = 0; i < event.target.selectedOptions.length;i++){
            names.push(event.target.selectedOptions.item(i).value)

        }
        this.setState({
            'name': names
        })
    }


    handleChange(event){
        this.setState(
            {
                [event.target.name]:event.target.value

            }

        )
         // console.log(event.target.nik ,event.target.value)
         // console.log(this.state.nik)
         // console.log(this.state.name)
    }


    handleSubmit(event){
        this.props.createWhat_is_famous(this.state.nik,this.state.name)
        // console.log(this.state.nik)
        // console.log(this.state.name)
        event.preventDefault()
    }



    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label for="login">nik</label>
                    <input type="text" className="form-control" nik="nik" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="nik">name</label>

                    <input type="number" className="form-control" nik="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>

                </div>

                <select name="name" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.names.map((item) => <option value={item.id}> {item.first_name} </option>)}

                </select>


                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );

    }

}

export default What_is_famousForm;