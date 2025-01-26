import React, { useState } from 'react';
import { Container, TextField, Button, Typography, InputAdornment, IconButton, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import PersonIcon from '@mui/icons-material/Person';
import EmailIcon from '@mui/icons-material/Email';
import LockIcon from '@mui/icons-material/Lock';
import AccountCircleIcon from '@mui/icons-material/AccountCircle'; // Icon for USER
import RoomServiceIcon from '@mui/icons-material/RoomService'; // Icon for HOUSEKEEPER
import BusinessCenterIcon from '@mui/icons-material/BusinessCenter'; // Icon for MANAGER
import FaceIcon from '@mui/icons-material/Face'; // Icon for RECEPTIONIST
import DeveloperModeIcon from '@mui/icons-material/DeveloperMode'; // Icon for DEVELOPER
import logo from "../../../assets/logo.webp";
import axios from 'axios';

const RegisterForm = () => {
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        role: ''
    });
    const [showPassword, setShowPassword] = useState(false);

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:8000/register_user/", formData);
            console.log("response", response);
        } catch (e) {
            console.log("error", e);
        }
    };

    return (
        <Container component="main" maxWidth="xs">
            <img style={{width:'10em', display: 'block', marginLeft: 'auto', marginRight: 'auto', marginBottom: '20px'}} src={logo} alt="Logo" />
            <Typography component="h1" variant="h5" textAlign="center">
                Sign Up
            </Typography>
            <form onSubmit={handleSubmit} noValidate>
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="first_name"
                    label="First Name"
                    name="first_name"
                    autoComplete="first_name"
                    autoFocus
                    value={formData.first_name}
                    onChange={handleChange}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="last_name"
                    label="Last Name"
                    name="last_name"
                    autoComplete="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="username"
                    label="Username"
                    name="username"
                    autoComplete="username"
                    value={formData.username}
                    onChange={handleChange}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <PersonIcon />
                            </InputAdornment>
                        ),
                    }}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    value={formData.email}
                    onChange={handleChange}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <EmailIcon />
                            </InputAdornment>
                        ),
                    }}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type={showPassword ? 'text' : 'password'}
                    id="password"
                    autoComplete="current-password"
                    value={formData.password}
                    onChange={handleChange}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <LockIcon />
                            </InputAdornment>
                        ),
                        endAdornment: (
                            <InputAdornment position="end">
                                <IconButton
                                    aria-label="toggle password visibility"
                                    onClick={togglePasswordVisibility}
                                    onMouseDown={handleMouseDownPassword}
                                >
                                    {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                        )
                    }}
                />
                <FormControl fullWidth variant="outlined" margin="normal">
                    <InputLabel id="role-label">Role</InputLabel>
                    <Select
                        labelId="role-label"
                        id="role"
                        name="role"
                        value={formData.role}
                        onChange={handleChange}
                        label="Role"
                    >
                        <MenuItem value="USER"><AccountCircleIcon /> User</MenuItem>
                        <MenuItem value="HOUSEKEEPER"><RoomServiceIcon /> Housekeeper</MenuItem>
                        <MenuItem value="MANAGER"><BusinessCenterIcon /> Manager</MenuItem>
                        <MenuItem value="RECEPTIONIST"><FaceIcon /> Receptionist</MenuItem>
                        <MenuItem value="DEVELOPER"><DeveloperModeIcon /> Developer</MenuItem>
                    </Select>
                </FormControl>
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    sx={{ mt: 3, mb: 2 }}
                >
                    Sign Up
                </Button>
            </form>
        </Container>
    );
};

export default RegisterForm;
