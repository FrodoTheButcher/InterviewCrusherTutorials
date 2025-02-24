package com.example.backendjavaspring.Repositorie;

import com.example.backendjavaspring.domain.Booking;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BookingRepositorie extends JpaRepository<Booking, Long> {
    public List<Booking> findByStatus(String status);
}
