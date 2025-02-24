package com.example.backendjavaspring.Dtos.Auth;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class GenerateAccessTokenRequestDto {
    private String email ;
    private String password ;
}
