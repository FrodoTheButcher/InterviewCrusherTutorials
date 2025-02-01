import React, { useState, useEffect } from 'react';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,
  CircularProgress, Typography, Button, Container, Box
} from '@mui/material';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

function HousekeeperView() {
  const [tasks, setTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [userConnected, setUserConnected] = useState(
    localStorage.getItem("access") ? jwtDecode(localStorage.getItem("access")) : ""
  );

  useEffect(() => {
    fetchTasks();
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

  const handleStatusChange = async (taskId, status) => {
    setIsLoading(true);
    try {
      const endpoint = status === 'DONE' ? `http://localhost:8000/task/${taskId}/done` : `http://localhost:8000/task/${taskId}/working`;
      await axios.patch(endpoint);
      fetchTasks(); // Refresh the task list after the status update
    } catch (error) {
      setError(`Failed to update task status: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">{`Error: ${error}`}</Typography>;

  return (
    <Container maxWidth="lg">
      <Typography variant="h4" sx={{ my: 4 }}>Tasks Assigned to Me</Typography>
      <TableContainer component={Paper}>
        <Table aria-label="tasks table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Room Image</TableCell>
              <TableCell>Room Details</TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Change Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {tasks.map((task) => (
              <TableRow key={task.id}>
                <TableCell>{task.id}</TableCell>
                <TableCell>
                  <Box
                    component="img"
                    sx={{
                      height: 100, // Adjust size as needed
                      width: 'auto',
                      maxWidth: '100%'
                    }}
                    alt={`Room ${task.room.id}`}
                    src={`http://localhost:8000${task.room.image}`}
                  />
                </TableCell>
                <TableCell>{`Floor ${task.room.floor} - Type ${task.room.type}`}</TableCell>
                <TableCell>{task.name}</TableCell>
                <TableCell>{task.description}</TableCell>
                <TableCell>{task.status}</TableCell>
                <TableCell>
                  {task.status !== 'DONE' && (
                    <Button variant="contained" color="primary" onClick={() => handleStatusChange(task.id, 'DONE')} sx={{ mr: 1 }}>
                      Set Done
                    </Button>
                  )}
                  {task.status !== 'WORKING' && (
                    <Button variant="contained" color="secondary" onClick={() => handleStatusChange(task.id, 'WORKING')}>
                      Set Working
                    </Button>
                  )}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default HousekeeperView;
