import React from 'react';
import { useParams, } from "react-router-dom";


const What_is_famousItem = ({What_is_famous,names}) => {
    return (
        <tr>
            <td>
                {What_is_famous.id}
            </td>
            <td>
                {What_is_famous.name}
            </td>
            <td>
                {What_is_famous.names.map((nameID) =>{
                    let name = names.find((names) => names.id == nameID)

                    if(name) {
                        return name.first_name
                    }
                })}
            </td>
        </tr>
    )
}

const What_is_famousListNames = ({What_is_famous,names}) => {

    let {id} = useParams()
    console.log(id)

    let filtered_item = What_is_famous.filter((What_is_famous => What_is_famous.names.includes(parseInt(id))))

    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Nik
            </th>
            <th>
                Name
            </th>
            {filtered_item.map((name) => <What_is_famousItem name={name}  names={names}/>)}
        </table>
    )
}

export default What_is_famousListNames;