import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router'
import Register from './pages/register'

function App() {

  return (
    <Router>
      <Routes>
        <Route path='/register' Component={Register} />
      </Routes>
    </Router>
  )
}

export default App
