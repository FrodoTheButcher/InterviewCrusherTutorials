package com.example.backendjavaspring.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "profiles")
public class Profile extends BaseEntity {

    private String image;
    private String role;

    @OneToOne
    @JoinColumn(name = "user_id")
    private User user;

    public Profile() {}

    public Profile(String image, String role, User user) {
        this.image = image;
        this.role = role;
        this.user = user;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
}
