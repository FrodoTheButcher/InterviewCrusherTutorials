import React, { useState, useEffect } from 'react';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,
  CircularProgress, Typography, IconButton, Button, Dialog, DialogActions,
  DialogContent, DialogTitle, TextField, Select, MenuItem, FormControl, InputLabel, Avatar
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import axios from 'axios';

function RoomsTable() {
  const [rooms, setRooms] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [open, setOpen] = useState(false);
  const [newRoom, setNewRoom] = useState({ floor: '', type: 'STANDARD', image: null });

  const ROOM_TYPE_CHOICES = [
    { key: 'STANDARD', value: 'Standard' },
    { key: 'DELUXE', value: 'Deluxe' },
    { key: 'SUITE', value: 'Suite' },
    { key: 'FAMILY', value: 'Family Room' },
  ];

  useEffect(() => {
    fetchRooms();
  }, []);

  const fetchRooms = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/register_room/');
      setRooms(response.data);
    } catch (error) {
      setError('Failed to fetch rooms: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleChange = (event) => {
    const { name, value, files } = event.target;
    if (files) {
      setNewRoom(prev => ({ ...prev, image: files[0] }));
    } else {
      setNewRoom(prev => ({ ...prev, [name]: value }));
    }
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('floor', newRoom.floor);
    formData.append('type', newRoom.type);
    if (newRoom.image) {
      formData.append('image', newRoom.image);
    }

    try {
      await axios.post('http://localhost:8000/register_room/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      fetchRooms();
      handleClose();
    } catch (error) {
      console.error('Failed to add room:', error);
      setError('Failed to add room');
    }
  };

  const deleteRoom = async (roomId) => {
    try {
      await axios.delete(`http://localhost:8000/register_room/${roomId}`);
      setRooms(rooms.filter(room => room.id !== roomId)); // Optimistic update
    } catch (error) {
      console.error('Failed to delete room:', error);
      setError('Failed to delete room');
    }
  };

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">{`Error: ${error}`}</Typography>;

  return (
    <div>
      <Button startIcon={<AddIcon />} onClick={handleOpen}>
        Add Room
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Add a New Room</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            name="floor"
            label="Floor"
            type="number"
            fullWidth
            variant="standard"
            value={newRoom.floor}
            onChange={handleChange}
          />
          <FormControl fullWidth margin="dense" variant="standard">
            <InputLabel>Type</InputLabel>
            <Select
              name="type"
              value={newRoom.type}
              label="Type"
              onChange={handleChange}
            >
              {ROOM_TYPE_CHOICES.map(option => (
                <MenuItem key={option.key} value={option.key}>{option.value}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <Button variant="contained" component="label" fullWidth>
            Upload Image
            <input
              type="file"
              name="image"
              hidden
              onChange={handleChange}
            />
          </Button>
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
              <TableCell>Floor</TableCell>
              <TableCell>Type</TableCell>
              <TableCell>Image</TableCell>
              <TableCell>Available</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rooms.map((room) => (
              <TableRow key={room.id}>
                <TableCell>{room.id}</TableCell>
                <TableCell>{room.floor}</TableCell>
                <TableCell>{room.type}</TableCell>
                <TableCell>
                  {room.image ? (
                    <img src={`http://localhost:8000${room.image}`} alt="Room" style={{ width: 100, height: "auto" }} />
                  ) : (
                    <Avatar>{room.type.charAt(0)}</Avatar>
                  )}
                </TableCell>
                <TableCell>{room.available ? 'Yes' : 'No'}</TableCell>
                <TableCell>
                  <IconButton onClick={() => deleteRoom(room.id)} color="error">
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default RoomsTable;
