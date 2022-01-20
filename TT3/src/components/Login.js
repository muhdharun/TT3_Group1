import React from 'react';

//form input
export default function Login() {
  return(
    
    <form className ='add-form' >
            <div className ='form-control'>
                <label>Username</label>
                <input type ='text' placeholder ='Username' 
                />
            </div>

            <div className ='form-control'>
                <label>Password</label>
                <input 
                type ='text' 
                placeholder ='Type password'
                />
            </div>
      <input type='submit' value ='Login' className ='btn btn-block' />
    </form>
  )
}