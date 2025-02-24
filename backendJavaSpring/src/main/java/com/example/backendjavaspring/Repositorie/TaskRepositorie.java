package com.example.backendjavaspring.Repositorie;

import com.example.backendjavaspring.domain.Task;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TaskRepositorie extends JpaRepository<Task, Long> {
}
