import Homepage from './components/Homepage';
import Preferences from './components/Preferences';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="wrapper">
      <h1>DBS WORKSPACE</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/homepage">
            <Dashboard />
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
