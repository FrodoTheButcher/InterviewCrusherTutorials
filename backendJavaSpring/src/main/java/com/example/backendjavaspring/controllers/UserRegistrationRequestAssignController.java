package com.example.backendjavaspring.controllers;

import com.example.backendjavaspring.Dtos.Response;
import com.example.backendjavaspring.Repositorie.UserRegistrationRequestAssignRepositorie;
import com.example.backendjavaspring.domain.UserRegistrationRequestAssign;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping
public class UserRegistrationRequestAssignController {

    @Autowired
    private UserRegistrationRequestAssignRepositorie userRegistrationRequestAssignRepositorie;

    @PostMapping("api/insert/")
    public ResponseEntity<Response<Long>> Insert(@RequestBody UserRegistrationRequestAssign userRegistrationRequestAssign) {
        this.userRegistrationRequestAssignRepositorie.save(userRegistrationRequestAssign);
        return new ResponseEntity<>(new Response("Successfully registered",userRegistrationRequestAssign.getId()), HttpStatus.OK);
    }

    @DeleteMapping("api/delete/")
    public ResponseEntity<Response> Reject(@RequestBody UserRegistrationRequestAssign userRegistrationRequestAssign) {
        this.userRegistrationRequestAssignRepositorie.delete(userRegistrationRequestAssign);
        return new ResponseEntity<>(new Response("Successfully deleted",null), HttpStatus.OK);
    }

    @GetMapping()
    public ResponseEntity<Response<List<UserRegistrationRequestAssign>>> GetAll() {
        List<UserRegistrationRequestAssign> userRegistrationRequestAssigns = this.userRegistrationRequestAssignRepositorie.findAll();
        return new ResponseEntity<>(new Response("Successfully retrieved",userRegistrationRequestAssigns), HttpStatus.OK);
    }

}
