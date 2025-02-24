package com.example.backendjavaspring.Dtos.Booking;

import com.example.backendjavaspring.Dtos.User.GetAllUsers.UserDto;
import com.example.backendjavaspring.domain.Room;
import com.example.backendjavaspring.domain.User;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class BookingDto {
    private Room room;
    private String start_date;
    private String end_date;
    private UserDto user;
    private Long cost;
    private String status;
}
