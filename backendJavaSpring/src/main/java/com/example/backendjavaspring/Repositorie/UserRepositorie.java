package com.example.backendjavaspring.Repositorie;

import com.example.backendjavaspring.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepositorie extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
}
