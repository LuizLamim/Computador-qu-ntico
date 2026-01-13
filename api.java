package com.exemplo.api.model;

public class Usuario {
    private Long id;
    private String nome;
    private String email;

    // Construtores
    public Usuario(Long id, String nome, String email) {
        this.id = id;
        this.nome = nome;
        this.email = email;
    }