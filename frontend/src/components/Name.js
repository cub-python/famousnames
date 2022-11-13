import React from "react";

const NameItem = ({name}) => {
    return (
        <tr>
            <td>{name.first_name}</td>
            <td>{name.last_name}</td>
            <td>{name.birthday_year}</td>
            <td>{name.place_of_birth}</td>
        </tr>
    )
}

const NameList = ({names}) => {

    return (
        <table>
            <tr>
                <th>First name</th>
                <th>Last name</th>
                <th>Birthday Year</th>
                <th>Place of Birth</th>
            </tr>
            {names.map((name) => <NameItem name={name}/>)}
        </table>
    )
}

export default NameList;