import React from 'react';
import UserRequestsTable from './components/UserRequests';
import UsersTable from './components/UsersList';
import RoomsTable from './components/RoomsTable';
import { Typography, Container, Paper, Box, Button } from '@mui/material';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

const Manager = () => {
  return (
    <Container maxWidth="lg">
      <Box my={4}>
        <Typography variant="h4" component="h2" sx={{ textAlign: 'center', mb: 3 }}>
          User Requests Management Table
        </Typography>
        <Paper elevation={3} sx={{ p: 2 }}>
          <UserRequestsTable />
        </Paper>
      </Box>

      <Box my={4}>
        <Typography variant="h4" component="h2" sx={{ textAlign: 'center', mb: 3 }}>
          Users Management Table
        </Typography>
        <Paper elevation={3} sx={{ p: 2 }}>
          <UsersTable />
        </Paper>
      </Box>

      <Box my={4}>
        <Typography variant="h4" component="h2" sx={{ textAlign: 'center', mb: 3 }}>
          Rooms Management Table
        </Typography>
        <Paper elevation={3} sx={{ p: 2, position: 'relative' }}>
          <Button variant="contained" startIcon={<AddCircleOutlineIcon />} sx={{ position: 'absolute', top: -28, right: 20 }}>
            Add Room
          </Button>
          <RoomsTable />
        </Paper>
      </Box>
    </Container>
  );
}

export default Manager;
