import React from "react";
import {Link} from "react-router-dom";

const What_is_famousItem = ({What_is_famous,deleteWhat_is_famous}) => {
    return (
        <tr>
            <td>{What_is_famous.id}</td>
            <td>{What_is_famous.name}</td>
            <td>{What_is_famous.names}</td>
            <td><button onClick={()=>deleteWhat_is_famous(What_is_famous.id)} type="button">Delete</button> </td>
        </tr>
    )
}

const What_is_famousList = ({What_is_famous, deleteWhat_is_famous}) => {

    return (
        <div>
            <table>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Names</th>
                    {What_is_famous.map((What_is_famous) => <What_is_famousItem What_is_famous={What_is_famous}
                                                                            deleteWhat_is_famous={deleteWhat_is_famous}/>)}
            </table>
            <Link to='/What_is_famous/create'>Create></Link>
        </div>
    )
}

export default What_is_famousList;