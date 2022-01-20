import Homepage from './components/Homepage.js';
import Preferences from './components/Preferences.js';
import Login from './components/Login.js';
import Header from './components/Header.js';


import { BrowserRouter, Route, Routes, Router } from 'react-router-dom';
import React, { useState } from 'react';


function App() {
  const [token, setToken] = useState();
  // if no token, will reload login page
  if(!token) {
    return <Login setToken={setToken} />
  }
  return (
    <Router>
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/homepage">
            <Homepage />
          </Route>
          <Route path="/preferences">
            <Preferences />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
    </Router>
  );
}

export default App;
