package com.example.backendjavaspring.controllers;

import com.example.backendjavaspring.Dtos.Booking.BookingDto;
import com.example.backendjavaspring.Dtos.Booking.FilteredBookings;
import com.example.backendjavaspring.Dtos.Booking.Register.RegisterBookingRequest;
import com.example.backendjavaspring.Dtos.Response;
import com.example.backendjavaspring.Dtos.User.GetAllUsers.UserDto;
import com.example.backendjavaspring.Repositorie.BookingRepositorie;
import com.example.backendjavaspring.Repositorie.ProfileRepositorie;
import com.example.backendjavaspring.Repositorie.RoomRepositorie;
import com.example.backendjavaspring.Repositorie.UserRepositorie;
import com.example.backendjavaspring.domain.Booking;
import com.example.backendjavaspring.domain.Profile;
import com.example.backendjavaspring.domain.Room;
import com.example.backendjavaspring.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.awt.print.Book;
import java.time.LocalDate;
import java.util.List;

@RestController
@RequestMapping
public class BookingController {

    @Autowired
    BookingRepositorie bookingRepositorie;

    @Autowired
    ProfileRepositorie profileRepositorie;
    @Autowired
    RoomRepositorie roomRepositorie;

    @Autowired
    UserRepositorie userRepositorie;
    @PostMapping
    public ResponseEntity<Response<Long>> createBooking(@RequestBody RegisterBookingRequest request) {
        User user = this.userRepositorie.findByEmail(request.getEmail()).orElse(null);
        if (user == null) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        Room room = this.roomRepositorie.findById(request.getRoom_id()).orElse(null);
        if(room == null)
        {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }

        Booking booking = new Booking();
        booking.setUser(user);
        booking.setRoom(room);
        booking.setStart_date(request.getStart_date());
        booking.setEnd_date(request.getEnd_date());

        String startDate = request.getStart_date();//format yyyy-mm-dd
        String endDate = request.getEnd_date();//format yyyy-mm-dd
        LocalDate start = LocalDate.parse(startDate);
        LocalDate end = LocalDate.parse(endDate);

        long totalDays = java.time.temporal.ChronoUnit.DAYS.between(start, end);
        long costForRoomPerDay = room.getType().getCost();
        booking.setCost(costForRoomPerDay*totalDays);
        booking.setStatus("PENDING");
        this.bookingRepositorie.save(booking);
        return  new ResponseEntity<>(new Response<>("Booking requested successfully", booking.getId()), HttpStatus.CREATED);
    }
    @PutMapping("approve/{booking_id}")
    public ResponseEntity<Response<Long>> approveBooking(@PathVariable Long booking_id) {
        Booking booking = this.bookingRepositorie.findById(booking_id).orElse(null);
        if(booking == null)
        {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        booking.setStatus("APPROVED");
        this.bookingRepositorie.save(booking);
        Room room = this.roomRepositorie.findById(booking.getRoom().getId()).orElse(null);
        room.setAvailable(false);
        this.roomRepositorie.save(room);
        return new ResponseEntity<>(new Response<>("Booking approved successfully", booking.getId()), HttpStatus.OK);
    }
    @DeleteMapping("reject/{booking_id}")
    public ResponseEntity<Response<Long>> rejectBooking(@PathVariable Long booking_id) {
        Booking booking = this.bookingRepositorie.findById(booking_id).orElse(null);
        if(booking == null)
        {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        booking.setStatus("REJECTED");
        this.bookingRepositorie.save(booking);
        Room room = this.roomRepositorie.findById(booking.getRoom().getId()).orElse(null);
        room.setAvailable(true);
        this.roomRepositorie.save(room);
        return new ResponseEntity<>(new Response<>("Booking rejected", booking.getId()), HttpStatus.OK);
    }

    @GetMapping("get_filtered")
    public ResponseEntity<Response<FilteredBookings>> QueryFilteredBookings()
    {
        FilteredBookings filteredBookings = new FilteredBookings();
        List<Booking> pendingBookings = this.bookingRepositorie.findByStatus("PENDING");
        List<Booking> approvedBookings = this.bookingRepositorie.findByStatus("APPROVED");
        List<Booking> rejectedBookings = this.bookingRepositorie.findByStatus("REJECTED");

        for(Booking booking : pendingBookings)
        {
            BookingDto bookingDto = new BookingDto();
            bookingDto.setStatus(booking.getStatus());
            bookingDto.setStart_date(booking.getStart_date());
            bookingDto.setEnd_date(booking.getEnd_date());
            UserDto userDto = new UserDto();
            userDto.setEmail(booking.getUser().getEmail());
            userDto.setId(booking.getUser().getId());
            userDto.setFirst_name(bookingDto.getUser().getFirst_name());
            userDto.setLast_name(bookingDto.getUser().getLast_name());
            Profile profile = this.profileRepositorie.findByUser(booking.getUser()).orElse(null);
            userDto.setProfile(profile);
            bookingDto.setUser(userDto);
            filteredBookings.getApproveds().add(new BookingDto());
        }
        for(Booking booking : rejectedBookings)
        {
            BookingDto bookingDto = new BookingDto();
            bookingDto.setStatus(booking.getStatus());
            bookingDto.setStart_date(booking.getStart_date());
            bookingDto.setEnd_date(booking.getEnd_date());
            UserDto userDto = new UserDto();
            userDto.setEmail(booking.getUser().getEmail());
            userDto.setId(booking.getUser().getId());
            userDto.setFirst_name(booking.getUser().getFirst_name());
            userDto.setLast_name(booking.getUser().getLast_name());
            Profile profile = this.profileRepositorie.findByUser(booking.getUser()).orElse(null);
            userDto.setProfile(profile);
            bookingDto.setUser(userDto);
            filteredBookings.getRejecteds().add(new BookingDto());
        }
        for(Booking booking : pendingBookings)
        {
            BookingDto bookingDto = new BookingDto();
            bookingDto.setStatus(booking.getStatus());
            bookingDto.setStart_date(booking.getStart_date());
            bookingDto.setEnd_date(booking.getEnd_date());
            UserDto userDto = new UserDto();
            userDto.setEmail(booking.getUser().getEmail());
            userDto.setId(booking.getUser().getId());
            userDto.setFirst_name(bookingDto.getUser().getFirst_name());
            userDto.setLast_name(bookingDto.getUser().getLast_name());
            Profile profile = this.profileRepositorie.findByUser(booking.getUser()).orElse(null);
            userDto.setProfile(profile);
            bookingDto.setUser(userDto);
            filteredBookings.getPendings().add(new BookingDto());
        }
        return new ResponseEntity<>(new Response<>("Booking requested successfully", filteredBookings), HttpStatus.OK);
    }

}
