import React, { useState } from 'react';
import PropTypes from 'prop-types';

async function loginUser(credentials) { //takes in credentials as an argument
    return fetch('http://localhost:8080/login', { //brings you to the login
      method: 'POST', //fetches the data
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(credentials)
    })
      .then(data => data.json())
   }

export default function Login({ setToken }) {
    const [username, setUserName] = useState(); //to capture user and pass
    const [password, setPassword] = useState();

    //on submit, runs this function
    const handleSubmit = async e => { 
        e.preventDefault();
        const token = await loginUser({ //logs in after calling username and password
          username,
          password
        });
        setToken(token);
      }
  return(

    <form className ='add-form' onSubmit={handleSubmit} >
            <h1>DBS WORKSPACE
                <p>Login</p>
            </h1>

            <div className ='form-control'>
                <label>Username</label>
                <input type ='text' 
                placeholder ='Username' 
                onChange={e => setUserName(e.target.value)}
                />
            </div>

            <div className ='form-control'>
                <label>Password</label>
                <input 
                type ='password' 
                placeholder ='Type password'
                onChange={e => setPassword(e.target.value)}
                />
            </div>
      <input type='submit' value ='Login' className ='btn btn-block' />
    </form>
  )
}

Login.propTypes ={
    setToken: PropTypes.func.isRequired //must press to work
}