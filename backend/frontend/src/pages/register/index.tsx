import React, { useState } from 'react';
import { Container, TextField, Button, Typography, InputAdornment, IconButton } from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import PersonIcon from '@mui/icons-material/Person';
import EmailIcon from '@mui/icons-material/Email';
import LockIcon from '@mui/icons-material/Lock';
import logo from "../../assets/logo.webp";
import RegisterForm from './components/RegisterForm';

export const Register = () => {


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
            <RegisterForm />
          </div>
        </div>
      );
}

export default Register;
