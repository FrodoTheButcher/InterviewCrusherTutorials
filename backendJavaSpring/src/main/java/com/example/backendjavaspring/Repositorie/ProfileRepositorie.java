package com.example.backendjavaspring.Repositorie;

import com.example.backendjavaspring.domain.Profile;
import com.example.backendjavaspring.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ProfileRepositorie  extends JpaRepository<Profile, Long> {
    Optional<Profile> findByUser(User user);
}
