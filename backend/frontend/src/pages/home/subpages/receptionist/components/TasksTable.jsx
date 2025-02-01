import React, { useState, useEffect } from 'react';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,
  CircularProgress, Typography, IconButton, Button, Dialog, DialogActions,
  DialogContent, DialogTitle, TextField, Box, Container
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

function TasksTable() {
  const [tasks, setTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [open, setOpen] = useState(false);
  const [newTask, setNewTask] = useState({ user: '', room: '', name: '', description: '', status: 'PENDING' });
  const [users, setUsers] = useState([]);
  const [rooms, setRooms] = useState([]);
  const [userConnected, setUserConnected] = useState(
    localStorage.getItem("access") ? jwtDecode(localStorage.getItem("access")) : ""
  );

  useEffect(() => {
    fetchTasks();
    fetchUsers();
    fetchRooms();
  }, []);

  const fetchTasks = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get(`http://localhost:8000/task/${userConnected?.user_id}`);
      setTasks(response.data);
    } catch (error) {
      setError('Failed to fetch tasks: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchUsers = async () => {
    try {
      const response = await axios.get('http://localhost:8000/get_users/');
      const filteredUsers = response.data.filter(user => user.profile?.role === "HOUSEKEEPER");
      console.log("filteredUsers",response?.data)
      setUsers(filteredUsers);
    } catch (error) {
      console.error('Failed to fetch users:', error.message);
    }
  };

  const fetchRooms = async () => {
    try {
      const response = await axios.get('http://localhost:8000/register_room/');
      setRooms(response.data);
    } catch (error) {
      console.error('Failed to fetch rooms:', error.message);
    }
  };

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewTask(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async () => {
    try {
      await axios.post('http://localhost:8000/tasks/', newTask);
      fetchTasks();
      handleClose();
    } catch (error) {
      console.error('Failed to add task:', error);
      setError('Failed to add task');
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await axios.delete(`http://localhost:8000/tasks/${taskId}`);
      setTasks(tasks.filter(task => task.id !== taskId)); 
    } catch (error) {
      console.error('Failed to delete task:', error);
      setError('Failed to delete task');
    }
  };

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">{`Error: ${error}`}</Typography>;

  return (
    <Container maxWidth="lg">
      <Box my={4} sx={{ position: 'relative' }}>
        <Button variant="contained" startIcon={<AddCircleOutlineIcon />} onClick={handleOpen} sx={{ mb: 2 }}>
          Add Task
        </Button>
        <Dialog open={open} onClose={handleClose}>
          <DialogTitle>Add a New Task</DialogTitle>
          <DialogContent>
            <TextField
              select
              autoFocus
              margin="dense"
              name="user"
              label="User"
              type="text"
              fullWidth
              variant="standard"
              value={newTask.user}
              onChange={handleChange}
              SelectProps={{ native: true }}
            >
              {users.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.username ?? option.email}
                </option>
              ))}
            </TextField>
            <TextField
              select
              margin="dense"
              name="room"
              label="Room"
              type="text"
              fullWidth
              variant="standard"
              value={newTask.room}
              onChange={handleChange}
              SelectProps={{ native: true }}
            >
              {rooms.map((option) => (
                <option key={option.id} value={option.id}>
                  {`Floor ${option.floor} - Type ${option.type}`}
                </option>
              ))}
            </TextField>
            <TextField
              margin="dense"
              name="name"
              label="Task Name"
              type="text"
              fullWidth
              variant="standard"
              value={newTask.name}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="description"
              label="Description"
              type="text"
              fullWidth
              variant="standard"
              value={newTask.description}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="status"
              label="Status"
              type="text"
              fullWidth
              variant="standard"
              value={newTask.status}
              onChange={handleChange}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>Cancel</Button>
            <Button onClick={handleSubmit}>Add</Button>
          </DialogActions>
        </Dialog>
        <TableContainer component={Paper}>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>User</TableCell>
                <TableCell>Room</TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
  {tasks.map((task) => (
    <TableRow key={task.id}>
      <TableCell>{task.id}</TableCell>
      <TableCell>{task.user.email || 'No Email'}</TableCell>
      <TableCell>
        <Box display="flex" alignItems="center">
          {task.room.image && (
            <img 
              src={`http://localhost:8000${task.room.image}`} 
              alt="Room" 
              style={{ width: 50, height: 50, marginRight: 8, borderRadius: 4 }}
            />
          )}
          {`Floor ${task.room.floor} - Type ${task.room.type}`}
        </Box>
      </TableCell>
      <TableCell>{task.name}</TableCell>
      <TableCell>{task.description}</TableCell>
      <TableCell>{task.status}</TableCell>
      <TableCell>
        <IconButton onClick={() => handleDelete(task.id)} color="error">
          <DeleteIcon />
        </IconButton>
      </TableCell>
    </TableRow>
  ))}
</TableBody>


          </Table>
        </TableContainer>
      </Box>
    </Container>
  );
}

export default TasksTable;
