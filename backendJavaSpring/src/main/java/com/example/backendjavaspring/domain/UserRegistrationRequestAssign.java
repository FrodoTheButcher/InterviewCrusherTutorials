package com.example.backendjavaspring.domain;


import jakarta.persistence.Entity;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
public class UserRegistrationRequestAssign extends BaseEntity{
  private String first_name;
  private String last_name;
  private String email;
  private String password;
  private String role;
}
