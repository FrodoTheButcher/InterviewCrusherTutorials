package com.example.backendjavaspring.Repositorie;

import com.example.backendjavaspring.domain.Room;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RoomRepositorie extends JpaRepository<Room, Long> {
}
