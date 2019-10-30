import React from 'react';  
import ReactDOM from 'react-dom';  
import { Route, Link, BrowserRouter as Router } from 'react-router-dom'  
import './index.css';  
import App from './App';  
import Login from './login'  
import Register from './register'  

const routing = (  
  <Router>  
    <div>  
      <h1>React Router Example</h1>  
      <Route exact path="/" component={App} />  
      <Route path="/register" component={Register} />  
      <Route path="/login" component={Login} />  
    </div>  
  </Router>  
)  
ReactDOM.render(routing, document.getElementById('root')); 