package com.exemplo.api.controller;

import com.exemplo.api.model.Usuario;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController // Indica que esta classe controla endpoints REST
@RequestMapping("/usuarios") // Define a rota base como http://localhost:8080/usuarios
public class UsuarioController {

    private List<Usuario> bancoDeDados = new ArrayList<>();

    // Inicializa com um dado fictício
    public UsuarioController() {
        bancoDeDados.add(new Usuario(1L, "Maria Silva", "maria@email.com"));
    }

    // Endpoint GET: Retorna todos os usuários
    @GetMapping
    public List<Usuario> listarUsuarios() {
        return bancoDeDados;
    }

    // Endpoint POST: Adiciona um novo usuário
    @PostMapping
    public Usuario criarUsuario(@RequestBody Usuario novoUsuario) {
        bancoDeDados.add(novoUsuario);
        return novoUsuario;
    }
}