import "./App.css";
import Footer from "./components/Footer";
import Display from "./components/Display";
import "bootstrap/dist/css/bootstrap.min.css";
import React, { Component } from "react";
import Signals from "./components/Signals";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
} from "react-router-dom";

class App extends Component {



  render() {


    return (
      <Router>
        <div className="App">
          <div className="Content">
            <div>
              <Link to='/' style={{ color: '#000', textDecoration: 0 }}>
                <h1 style={{ paddingTop: 4, textAlign: 'center' }}>TradeTryHard</h1>
              </Link>
              <Switch>
                <Route path="/signal">
                  <Signals />
                </Route>
                <Route path="/">
                  <Display />
                </Route>
              </Switch>
            </div>
          </div>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;
