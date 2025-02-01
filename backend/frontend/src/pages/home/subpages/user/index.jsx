import React, { useState, useEffect } from 'react';
import {
  Button, CircularProgress, Typography, Paper, Grid, Box, TextField, MenuItem,
  Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle
} from '@mui/material';
import BedIcon from '@mui/icons-material/Bed';
import StarRateIcon from '@mui/icons-material/StarRate';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import axios from 'axios';

function AvailableRooms() {
  const [rooms, setRooms] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [typeFilter, setTypeFilter] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [bookingData, setBookingData] = useState({
    email: '',
    start_date: '',
    end_date: '',
    room_id: null
  });

  useEffect(() => {
    fetchRooms();
  }, []);

  const fetchRooms = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/register_room/');
      const availableRooms = response.data.filter(room => room.available);
      setRooms(availableRooms);
    } catch (error) {
      setError(`Failed to fetch rooms: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleOpenBookingDialog = (roomId) => {
    setBookingData(prev => ({ ...prev, room_id: roomId }));
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
  };

  const handleBookingChange = (prop) => (event) => {
    setBookingData({ ...bookingData, [prop]: event.target.value });
  };

  const submitBooking = async () => {
    try {
      console.log('Booking data:', bookingData);
      // Here you would call the API to submit the booking data
      alert(`Booking confirmed for room ID: ${bookingData.room_id}`);
      setOpenDialog(false);
    } catch (error) {
      console.error('Failed to submit booking:', error);
    }
  };

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">{error}</Typography>;

  const filteredRooms = rooms.filter(room =>
    typeFilter ? room.type === typeFilter : true
  );

  return (
    <Box sx={{ flexGrow: 1, padding: 3 }}>
      <Typography variant="h4" gutterBottom>Available Rooms</Typography>
      <TextField
        select
        label="Filter by Room Type"
        value={typeFilter}
        onChange={e => setTypeFilter(e.target.value)}
        helperText="Select a room type to filter"
        sx={{ mb: 2 }}
      >
        <MenuItem value="">All Types</MenuItem>
        <MenuItem value="STANDARD">Standard</MenuItem>
        <MenuItem value="DELUXE">Deluxe</MenuItem>
        <MenuItem value="SUITE">Suite</MenuItem>
        <MenuItem value="FAMILY">Family Room</MenuItem>
      </TextField>
      <Grid container spacing={3}>
        {filteredRooms.map((room) => (
          <Grid item xs={12} sm={6} md={4} key={room.id}>
            <Paper elevation={3} sx={{ padding: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <img src={`http://localhost:8000${room.image}`} alt="Room" style={{ width: '100%', height: 'auto', borderRadius: 5 }} />
              <Typography variant="h6" gutterBottom>{`Room ID: ${room.id}`}</Typography>
              <Typography variant="body1" color="textSecondary">{room.name || 'No specific name'}</Typography>
              <Typography variant="body1" color="textSecondary">{room.description || 'No specific description'}</Typography>

              <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, mb: 1 }}>
                <BedIcon />
                <Typography sx={{ ml: 1 }}>{room.type}</Typography>
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center' }}>
                <StarRateIcon color="warning" />
                <Typography sx={{ ml: 1 }}>{room.rating ? `${room.rating}/5` : "Not Rated"}</Typography>
              </Box>
              <Button startIcon={<AddShoppingCartIcon />} variant="contained" color="primary" onClick={() => handleOpenBookingDialog(room.id)} sx={{ mt: 2 }}>
                Book Now
              </Button>
            </Paper>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={handleCloseDialog}>
        <DialogTitle>Book a Room</DialogTitle>
        <DialogContent>
          <DialogContentText>To book a room, please enter your email address and select your stay dates.</DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="email"
            label="Email Address"
            type="email"
            fullWidth
            variant="standard"
            value={bookingData.email}
            onChange={handleBookingChange('email')}
            required
          />
          <TextField
            margin="dense"
            id="start_date"
            label="Start Date"
            type="date"
            fullWidth
            variant="standard"
            InputLabelProps={{ shrink: true }}
            value={bookingData.start_date}
            onChange={handleBookingChange('start_date')}
            required
          />
          <TextField
            margin="dense"
            id="end_date"
            label="End Date"
            type="date"
            fullWidth
            variant="standard"
            InputLabelProps={{ shrink: true }}
            value={bookingData.end_date}
            onChange={handleBookingChange('end_date')}
            required
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancel</Button>
          <Button onClick={submitBooking} color="primary">Confirm Booking</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default AvailableRooms;
