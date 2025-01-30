import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom'; // Corrected import from 'react-router' to 'react-router-dom'
import axios from 'axios';
import Register from './pages/register';
import Login from './pages/login';
import TokenRefresher from './components/TokenRefresher';
import Home from './pages/home';
import Header from './pages/components/Header';

function App() {
  return (
    <Router>
      <TokenRefresher /> 
     {

     // <Header/>
     }
      <Routes>
        <Route path='/register' element={<Register />} />
        <Route path='/login' element={<Login />} />
        <Route path='/' element={<Home/>}/>
      </Routes>
    </Router>
  );
}
export default App