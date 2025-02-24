package com.example.backendjavaspring.Dtos.Task;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class AssignTaskRequest {
    private String name;
    private String description;
    private Long user;
    private Long room;
}
