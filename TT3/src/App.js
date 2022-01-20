import Homepage from './components/Homepage.js';
import Preferences from './components/Preferences.js';
import Login from './components/Login.js';

import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React, { useState } from 'react';


function App() {
  const [token, setToken] = useState();
  if(!token) {
    return <Login setToken={setToken} />
  }
  return (
    <div className="wrapper">
      <h1>DBS WORKSPACE</h1>
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
  );
}

export default App;
