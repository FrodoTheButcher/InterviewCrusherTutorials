package com.example.backendjavaspring.Dtos.User.GetAllUsers;

import com.example.backendjavaspring.domain.Profile;
import com.example.backendjavaspring.domain.Room;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class UserDto {
    private String email;
    private String first_name;
    private String last_name;
    private Long id;
    private Profile profile;
}
