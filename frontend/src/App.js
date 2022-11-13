import React from "react";
import axios from "axios";
// import logo from './logo.svg';
import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
import Footer from './components/Footer';
import Navbar from './components/Menu';
// import './App.css';
import NameList from './components/Name.js';


/* eslint-disable max-len */
const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            navbarItems: [
                {name: 'Names', href: '/'},
            ],
            'names': []
        };
    }

    componentDidMount() {
        // const names = [{
        //     'first_name': 'Лунь',
        //     'last_name': 'Цай',
        //     'birthday_year': 50,
        //     'place_of_birth': 'империи Хань(Китай)',
        // }, {
        //     'first_name': 'Карл',
        //     'last_name': 'Маркс',
        //     'birthday_year': 1818,
        //     'place_of_birth': 'Трир, Рейнская провинция, королевство Пруссия',
        // }]

        axios.get(get_url('names/'))
            .then(response => {
                // const names = response.data
                this.setState({names: response.data})
            }).catch(error => console.log(error))

    }

    render() {
        return (
            <div>
                <header>
                    <Navbar navbarItems={this.state.navbarItems}/>
                </header>
                <main role="main" class="flex-shrink-0">
                    <div className="container">
                        <NameList names={this.state.names}/>
                    </div>
                </main>
                <Footer/>
            </div>
        );
    }
}

export default App;
