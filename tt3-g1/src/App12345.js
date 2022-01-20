import Header from './components/Header'
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'
import { useEffect, useState } from 'react'
import api from './api/posts'
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

const App = () => {
  const [posts, setPosts] = useState([])
  const [showAddTask, setShowAddTask] = useState(true)
  const [tasks, setTasks] = useState([
    {
      id: 1,
      text: 'Doctors Appointment',
      day: 'Feb 5th at 2.30pm',
      reminder: true,
    }
  ]
  )  
  useEffect(() => {
    const fetchPosts = async () => {
      try{
        const response = await api.get('/getAllPosts')
        setPosts(response.data)
      } catch (err) {
        if (err.response) {
          // Not in the 200 response range
          console.log(err.response.data)
          console.log(err.response.status)
          console.log(err.response.headers)
        } else {
          console.log(`Error: $(err.message)`);
        }
  
      }
    }
  
    fetchPosts()
  
  })
  // add the database of entries here (in btwn useState() brackets) for now

  // Add Task
  const addTask = (task) => {
    const id = Math.floor(Math.random() * 10000) +1
    const newTask = { id, ...task }
    setTasks([...tasks, newTask])
  }


  //Delete Task
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !==id))
  }

  return (
    <div className='container'>
      <Header title='DBS Workspace' />
      {/* <Header onAdd={() => setShowAddTask (!showAddTask)} /> */}
      {showAddTask && <AddTask onAdd={addTask} />}
      {/* <AddTask onAdd={addTask} /> */}
      {tasks.length > 0 ? (
        <Tasks tasks={tasks} onDelete={deleteTask} />
      ) : ('No Feed') }
    </div>
  )
}

export default App;
