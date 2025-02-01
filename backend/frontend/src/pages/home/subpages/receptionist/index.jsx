import React from 'react';
import TasksTable from './components/TasksTable';
import { Typography, Container, Paper, Box } from '@mui/material';
import UsersTable from '../admin/components/UsersList';
import RoomsTable from '../admin/components/RoomsTable';

const Receptionist = () => {
  return (
    <Container sx={{overflow:'scroll'}}>
      <Typography variant="h4" component="h2" sx={{ textAlign: 'center' }}>
        Task Management
      </Typography>
      <TasksTable />
      <Box >
        <Typography variant="h4" component="h2" sx={{ textAlign: 'center'}}>
          Users Management Table
        </Typography>
        <Paper elevation={3} sx={{ p: 2 }}>
          <UsersTable/>
        </Paper>
      </Box>

      <Box >
        <Typography variant="h4" component="h2" sx={{ textAlign: 'center'}}>
          Rooms Management Table
        </Typography>
        <Paper elevation={3} sx={{ p: 2, position: 'relative' }}>
          <RoomsTable />
        </Paper>
      </Box>
    </Container>
  );
}

export default Receptionist;
