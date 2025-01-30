import React, { useEffect, useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  IconButton,
  Tooltip,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Button,
  Typography
} from '@mui/material';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import axios from 'axios';

const UserTable = () => {
    const [open, setOpen] = useState(false);
    const [currentUser, setCurrentUser] = useState(null);
    const [actionType, setActionType] = useState('');

    const [users,setUsers] = useState([])

    const fetchRequests = async () => {
        try {
            const response = await axios.get("http://localhost:8000/register_user/");
            setUsers(response.data);
        } catch (e) {
            console.error('Failed to fetch users', e);
        }
    };

    useEffect(() => {
        fetchRequests();
    }, []);
    const handleClickOpen = (user, action) => {
        setCurrentUser(user);
        setActionType(action);
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const handleConfirm = () => {
        console.log(`${actionType}d user:`, currentUser.email);
        setOpen(false);
    };
    if(!users?.length)
    {
        return <></>
    }

    const actionIcon = actionType === 'approve' ? <CheckCircleOutlineIcon sx={{ color: 'green', mr: 1 }} /> : <HighlightOffIcon sx={{ color: 'red', mr: 1 }} />;

    return (
        <React.Fragment>
            <Typography variant="h4" component="h2" sx={{ textAlign: 'center' }}>
                User Management Table
            </Typography>
            <TableContainer component={Paper} sx={{ margin: 'auto',  }}>
                <Table sx={{ }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Email</TableCell>
                            <TableCell>First Name</TableCell>
                            <TableCell>Last Name</TableCell>
                            <TableCell>Username</TableCell>
                            <TableCell>Image</TableCell>
                            <TableCell>Role</TableCell>
                            <TableCell align="center">Approve</TableCell>
                            <TableCell align="center">Reject</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {users.map((user, index) => (
                            <TableRow key={index}>
                                <TableCell>{user.email}</TableCell>
                                <TableCell>{user.first_name}</TableCell>
                                <TableCell>{user.last_name}</TableCell>
                                <TableCell>{user.username}</TableCell>
                                <TableCell>{user.image}</TableCell>
                                <TableCell>{user.role}</TableCell>
                                <TableCell align="center">
                                    <Tooltip title="Approve">
                                        <IconButton onClick={() => handleClickOpen(user, 'approve')} color="success">
                                            <CheckCircleIcon />
                                        </IconButton>
                                    </Tooltip>
                                </TableCell>
                                <TableCell align="center">
                                    <Tooltip title="Reject">
                                        <IconButton onClick={() => handleClickOpen(user, 'reject')} color="error">
                                            <CancelIcon />
                                        </IconButton>
                                    </Tooltip>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
                sx={{ '& .MuiDialog-container': { alignItems: 'flex-start' } }}  // Custom style for the dialog position
            >
                <DialogTitle id="alert-dialog-title">
                    {"Confirm Action"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        <Typography variant="body1" component="span">
                            {actionIcon}
                            Are you sure you want to {actionType} for {currentUser?.email}?
                        </Typography>
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Cancel
                    </Button>
                    <Button onClick={handleConfirm} color="primary" autoFocus>
                        Confirm
                    </Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
};

export default UserTable;
