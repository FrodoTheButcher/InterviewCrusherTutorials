package com.example.backendjavaspring.Dtos.Booking.Register;


import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class RegisterBookingRequest {
    private String email;
    private String start_date;
    private String end_date;
    private Long room_id;
}
