import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Typography, IconButton, Box } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios'; // You might need to install axios if not already available
import { jwtDecode } from 'jwt-decode';
import Avatar from '@mui/material/Avatar'; // Import at the top of your file


function UsersTable() {
  const [users, setUsers] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [userConnected, setUserConnected] = useState(
        localStorage.getItem("access") ? jwtDecode(localStorage.getItem("access")) : ""
      );
  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/get_users/');
      
      setUsers(response.data);
    } catch (error) {
      setError(error.message);
    }
    setIsLoading(false);
  };

  const deleteUser = async (userId) => {
    try {
      const response = await axios.delete(`http://localhost:8000/users/delete/${userId}/${userConnected.user_id}/`);

      if (response.status === 200) {
        fetchUsers(); // Refresh the list after deletion
      }
    } catch (error) {
      console.error('Failed to delete user:', error);
      setError('Failed to delete user');
    }
  };

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">{`Error: ${error}`}</Typography>;

  return (
    <TableContainer component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Email</TableCell>
            <TableCell>First Name</TableCell>
            <TableCell>Last Name</TableCell>
            <TableCell>ID</TableCell>
            <TableCell>Role</TableCell>
            <TableCell>Actions</TableCell>
          </TableRow>
        </TableHead>

   <TableBody>
     {users.map((user) => (
       <TableRow key={user.id}>
         <TableCell>
           <Box display="flex" alignItems="center">
             {user.profile && user.profile.image ? (
               <img 
                 src={`http://localhost:8000${user.profile.image}`} 
                 alt="User"
                 style={{ width: 50, height: 50, marginRight: 8, borderRadius: '50%' }}
               />
             ) : (
               <Avatar style={{ marginRight: 8 }}>
                 {user.email ? user.email.charAt(0).toUpperCase() : '?'}
               </Avatar>
             )}
             {user.email}
           </Box>
         </TableCell>
         <TableCell>{user.first_name || 'N/A'}</TableCell>
         <TableCell>{user.last_name || 'N/A'}</TableCell>
         <TableCell>{user.id}</TableCell>
         <TableCell>{user.profile ? user.profile.role : 'No Profile'}</TableCell>
         <TableCell>
           <IconButton onClick={() => deleteUser(user.id)} color="error">
             <DeleteIcon />
           </IconButton>
         </TableCell>
       </TableRow>
     ))}
   </TableBody>

      </Table>
    </TableContainer>
  );
}

export default UsersTable;
