import React, { useEffect } from 'react'
import LoginForm from './components/LoginForm';
import { useNavigate } from 'react-router';

const Login = () => {


   const navigate = useNavigate()

   useEffect(()=>{
    const access = localStorage.getItem("access")
    if(access)
    {
      navigate("/") 
    }

   },[])

    const backgroundStyle = {
        height: '100vh',
        width:'100vw',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        background: 'linear-gradient(45deg, #6a11cb 30%, #2575fc 90%)', 
      };
    
      const formContainerStyle = {
        backgroundColor: 'rgba(255, 255, 255, 0.8)', 
        padding: '20px',
        borderRadius: '10px',
        boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
        width: '100%', 
        maxWidth: '450px' 
      };
    
      return (
        <div style={backgroundStyle}>
          <div style={formContainerStyle}>
            <LoginForm />
          </div>
        </div>
      );
}

export default Login
