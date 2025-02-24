package com.example.backendjavaspring.controllers;

import com.example.backendjavaspring.Dtos.Response;
import com.example.backendjavaspring.Dtos.Task.AssignTaskRequest;
import com.example.backendjavaspring.Dtos.Task.TaskDto;
import com.example.backendjavaspring.Dtos.User.GetAllUsers.UserDto;
import com.example.backendjavaspring.Repositorie.ProfileRepositorie;
import com.example.backendjavaspring.Repositorie.RoomRepositorie;
import com.example.backendjavaspring.Repositorie.TaskRepositorie;
import com.example.backendjavaspring.Repositorie.UserRepositorie;
import com.example.backendjavaspring.domain.Profile;
import com.example.backendjavaspring.domain.Room;
import com.example.backendjavaspring.domain.Task;
import com.example.backendjavaspring.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping
public class TaskController {
    @Autowired
    UserRepositorie userRepositorie;

    @Autowired
    ProfileRepositorie profileRepositorie;

    @Autowired
    TaskRepositorie taskRepositorie;

    @Autowired
    RoomRepositorie roomRepositorie;

    @PostMapping("/assign/")
    public ResponseEntity<Response<Long>> AssignTaskToUser(AssignTaskRequest request) {
        User user = this.userRepositorie.findById(request.getUser()).orElse(null);
        Room room = this.roomRepositorie.findById(request.getRoom()).orElse(null);

        Task task = new Task();
        task.setUser(user);
        task.setRoom(room);
        task.setDescription(request.getDescription());
        task.setName(request.getName());
        task.setStatus("PENDING");
        this.taskRepositorie.save(task);
        return new ResponseEntity<>(new Response<>("Task assigned successfully", task.getId()), HttpStatus.OK);
    }

    @PutMapping("swapToProgress/{id}")
    public ResponseEntity<Response<Long>> UpdateTaskProgress(@RequestParam Long id) {
        Task task = this.taskRepositorie.findById(id).orElse(null);
        if(task == null)
        {
            return new ResponseEntity<>(new Response<>("Task not found", id), HttpStatus.NOT_FOUND);
        }
        task.setStatus("IN_PROGRESS");
        this.taskRepositorie.save(task);
        return new ResponseEntity<>(new Response<>("Task updated successfully", task.getId()), HttpStatus.OK);
    }

    @GetMapping("getAll")
    public ResponseEntity<Response<List<TaskDto>>> getAllTasks() {
        List<Task> tasks = this.taskRepositorie.findAll();
        List<TaskDto> taskDtos = new ArrayList<>();
        for (Task task : tasks) {
            TaskDto taskDto = new TaskDto();
            UserDto userDto = new UserDto();
            userDto.setId(task.getUser().getId());
            Profile profile = this.profileRepositorie.findByUser(task.getUser()).orElse(null);
            if(profile == null){
                return new ResponseEntity<>(new Response<>("Task updated successfully",null),HttpStatus.NOT_FOUND);
            }
            userDto.setProfile(profile);
            userDto.setEmail(task.getUser().getEmail());
            userDto.setFirst_name(task.getUser().getFirst_name());
            userDto.setLast_name(task.getUser().getLast_name());
            taskDto.setUser(userDto);
            taskDtos.add(taskDto);
        }
        return new ResponseEntity<>(new Response<>("Get All Success",taskDtos), HttpStatus.OK);
    }

    @DeleteMapping("{id}")
    public ResponseEntity<Response<Long>> deleteTask(@PathVariable Long id) {
        this.taskRepositorie.deleteById(id);
        return new ResponseEntity<>(new Response<>("Task deleted successfully", id), HttpStatus.OK);
    }
}
