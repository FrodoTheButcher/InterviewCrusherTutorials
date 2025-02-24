package com.example.backendjavaspring.Dtos.Auth;


import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class PairsOfAuthTokensDto {
    private String accessToken;
    private String refreshToken;
}
