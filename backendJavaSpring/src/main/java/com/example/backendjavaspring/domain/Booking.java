package com.example.backendjavaspring.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
public class Booking extends BaseEntity{

    @OneToOne
    @JoinColumn(name = "room_id")
    private Room room;

    private String start_date;

    private String end_date;

    @OneToOne
    @JoinColumn(name = "user_id")
    private User user;

    private float cost;

    private String status; //PENDING  APPROVED REJECTED

}
