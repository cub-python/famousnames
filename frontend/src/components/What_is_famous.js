import React from "react";

const What_is_famousItem = ({What_is_famous}) => {
    return (
        <tr>
            <td>{What_is_famous.id}</td>
            <td>{What_is_famous.name}</td>
            <td>{What_is_famous.names}</td>

        </tr>
    )
}

const What_is_famousList = ({What_is_famous}) => {

    return (
        <table>
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Names</th>
            </tr>
            {What_is_famous.map((What_is_famous) => <What_is_famousItem What_is_famous={What_is_famous}/>)}
        </table>
    )
}

export default What_is_famousList;