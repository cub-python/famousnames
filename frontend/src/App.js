import React from "react";
import axios from "axios";
import logo from './logo.svg';

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
// import Footer from './components/Footer';
// import Navbar from './components/Menu';
import './App.css';
import NameList from './components/Name.js';
import What_is_famousList from './components/What_is_famous.js';
import NotFound404 from "./components/NotFound404";
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from "react-router-dom";


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
            'names': [],
            'What_is_famous': []

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

        axios.get('http://127.0.0.1:8000/api/names/')
            .then(response => {
                // const names = response.data
                this.setState({names: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/What_is_famous/')
            .then(response => {
                // const names = response.data
                this.setState({What_is_famous: response.data})
            }).catch(error => console.log(error))

    }

    render() {
        return (
            <div>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'> Names </Link>
                            </li>
                            <li>
                                <Link to='/What_is_famous'> What_is_famous </Link>
                            </li>
                        </ul>
                    </nav>
                    {/*<header>*/}
                    {/*    <Navbar navbarItems={this.state.navbarItems}/>*/}
                    {/*</header>*/}
                    {/*<main role="main" class="flex-shrink-0">*/}
                    {/*    <div className="container">*/}
                    <Switch>
                        <Route exact path='/' component={() => <NameList names={this.state.names}/>}/>
                        <Route exact path='/What_is_famousList'
                               component={() => < What_is_famousList What_is_famous={this.state.What_is_famous}/>}/>
                        <Redirect from='/names1' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
                {/*</div>*/}
                {/*    // </main>*/}
                {/*    // <Footer/>*/}
            </div>
        );
    }
}

export default App;
