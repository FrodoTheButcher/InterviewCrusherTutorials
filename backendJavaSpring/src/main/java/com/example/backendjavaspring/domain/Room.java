package com.example.backendjavaspring.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
@Table(name = "rooms")
public class Room {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Corectat accesul

    @Column(unique = true, nullable = false, length = 50)
    private String name;

    @Column(nullable = true)
    private String description;

    @ManyToOne
    @JoinColumn(name = "roomType_id")
    private RoomType type;

    private String image;

    private int floor;

    private float rating;

    private boolean available;
}
