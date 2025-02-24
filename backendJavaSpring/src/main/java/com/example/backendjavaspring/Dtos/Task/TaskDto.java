package com.example.backendjavaspring.Dtos.Task;

import com.example.backendjavaspring.Dtos.User.GetAllUsers.UserDto;
import com.example.backendjavaspring.domain.Room;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class TaskDto {
    private UserDto user;
    private Room room;
    private String title;
    private String description;

}
