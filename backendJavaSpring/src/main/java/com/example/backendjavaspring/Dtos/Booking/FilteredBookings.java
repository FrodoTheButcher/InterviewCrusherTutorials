package com.example.backendjavaspring.Dtos.Booking;

import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;

@Setter
@Getter
public class FilteredBookings {
    private List<BookingDto> rejecteds = new ArrayList<BookingDto>();
    private List<BookingDto> approveds = new ArrayList<>();
    private List<BookingDto> pendings = new ArrayList<>();
}
