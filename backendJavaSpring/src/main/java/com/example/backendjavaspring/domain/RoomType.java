package com.example.backendjavaspring.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "room_types")
@Getter
@Setter
public class RoomType extends BaseEntity {
    @Column(nullable = false, length = 50)
    private String type;

    @Column(nullable = false)
    private int cost; // Corectat numele atributului
}
