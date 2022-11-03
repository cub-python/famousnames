import React from "react";
import axios from "axios";
import logo from './logo.svg';

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
import Footer from './components/Footer';
import Navbar from './components/Menu';
import './App.css';
import NameList from './components/Name.js';
import What_is_famousList from './components/What_is_famous.js';
import NotFound404 from "./components/NotFound404";
import LoginForm from "./components/Auth.js";
import Cookies from "universal-cookie";
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
                {name: 'Projects', href: '/projects'},
                {name: 'TODOs', href: '/todos'},
            ],
            names: [],
            What_is_famous: [],
            token: '',
            project: {},
            projects: [],
            auth: {username: '', is_login: false}

        };
    }

    logout() {
        this.set_token('')
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/names/', {headers}).then(response => {
            // const names = response.data
            this.setState({names: response.data})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/What_is_famous/', {headers}).then(response => {
            // const names = response.data
            this.setState({What_is_famous: response.data})
        }).catch(error => console.log(error))
    }

    is_aut() {
        return !!this.state.token
    }


    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
        console.log(this.state.token)
        // localStorage.setItem('token',token)
        // let token_ = localStorage.getItem('token')
        //
        // document.cookie = `token=${token},username=nikola, password=password`
    }

    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())

    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username, password: password
        }).then(response => {
            this.set_token(response.data['token'])
            // const names = response.data
            // this.setState({names: response.data})
        }).catch(error => console.log(error))

        // console.log('APP'+username+' '+password)
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        console.log(this.is_aut())
        if (this.is_aut()) {
            console.log('Token ${this.state.token}')
            headers['Authorization'] = 'Token ${this.state.token}'
        }
        return headers
    }


    componentDidMount() {
        this.get_token_from_cookies()
        // this.load_data()
    }

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

    // axios.get('http://127.0.0.1:8000/api/names/')
    //     .then(response => {
    //         // const names = response.data
    //         this.setState({names: response.data})
    //     }).catch(error => console.log(error))

    // axios.get('http://127.0.0.1:8000/api/What_is_famous/')
    //     .then(response => {
    //         // const names = response.data
    //         this.setState({What_is_famous: response.data})
    //     }).catch(error => console.log(error))


    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'> Names </Link>
                            </li>
                            <li>
                                <Link to='/What_is_famous'> What_is_famous </Link>
                            </li>
                            <li>{this.is_aut() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'> Login </Link>}
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
                        <Route exact path='/What_is_famous'
                               component={() => <What_is_famousList What_is_famous={this.state.What_is_famous}/>}/>
                        <Route path='/names/:id'>

                            {/*<What_is_famousListNames what_is_famous={this.state.what_is_famous} names={this.state.names}/>*/}
                        </Route>
                        <Route exact path='/login'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Redirect from='/names1' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                {/*</div>*/}
                {/*    // </main>*/}
                {/*    // <Footer/>*/}
            </div>
        );
    }
}

export default App;
