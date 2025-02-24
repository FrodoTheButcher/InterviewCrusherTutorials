package com.example.backendjavaspring.controllers;

import com.example.backendjavaspring.Dtos.Response;
import com.example.backendjavaspring.Repositorie.UserRegistrationRequestAssignRepositorie;
import com.example.backendjavaspring.Repositorie.UserRepositorie;
import com.example.backendjavaspring.domain.User;
import com.example.backendjavaspring.domain.UserRegistrationRequestAssign;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping
public class UserController {
    @Autowired
    UserRegistrationRequestAssignRepositorie userRegistrationRequestAssignRepositorie;

    @Autowired
    UserRepositorie userRepositorie;

    @PostMapping("create/{id}")
    public Response<Long> createUser(@PathVariable Long id) {
        UserRegistrationRequestAssign userRegistrationRequestAssign = this.userRegistrationRequestAssignRepositorie.getById(id);
        User user = new User();
        user.setEmail(userRegistrationRequestAssign.getEmail());
        user.setPassword(userRegistrationRequestAssign.getPassword());
        user.setLast_name(userRegistrationRequestAssign.getLast_name());
        user.setFirst_name(userRegistrationRequestAssign.getFirst_name());
        this.userRepositorie.save(user);
        this.userRegistrationRequestAssignRepositorie.deleteById(id);
        return new Response<>("Successfully created user",user.getId());
    }

    @DeleteMapping("delete/{id}")
    public ResponseEntity<Response> deleteUser(@PathVariable Long id) {
        UserRegistrationRequestAssign userRegistrationRequestAssign = this.userRegistrationRequestAssignRepositorie.getById(id);
        this.userRegistrationRequestAssignRepositorie.deleteById(id);
        return new ResponseEntity<>(new Response<>("Successfully deleted user",null), HttpStatus.OK);
    }

}
