package com.example.backendjavaspring.controllers;

import com.example.backendjavaspring.Dtos.Auth.GenerateAccessTokenRequestDto;
import com.example.backendjavaspring.Dtos.Auth.PairsOfAuthTokensDto;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping
public class AuthController {

    @PostMapping("GenerateAuthBearerTokens")
    public ResponseEntity<PairsOfAuthTokensDto> GenerateAuthBearerTokens(@RequestBody GenerateAccessTokenRequestDto token) {

    }


    private PairsOfAuthTokensDto GenerateTokens(String userEmail)
    {
        
    }

}
