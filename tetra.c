#include <GL/glut.h> // Inclui as bibliotecas OpenGL e GLUT
#include <stdio.h>   // Para printf (opcional)

// Vértices do tetraedro
// Cada vértice é um array de 3 floats (x, y, z)
GLfloat vertices[4][3] = {
    {0.0, 0.0, 1.0},    // Vértice 0 (topo, para cima no Z)
    {-0.816, -0.471, -0.333}, // Vértice 1
    {0.816, -0.471, -0.333},  // Vértice 2
    {0.0, 0.943, -0.333}    // Vértice 3
};

// Cores para as faces (para visualização melhor)
GLfloat colors[4][3] = {
    {1.0, 0.0, 0.0}, // Vermelho
    {0.0, 1.0, 0.0}, // Verde
    {0.0, 0.0, 1.0}, // Azul
    {1.0, 1.0, 0.0}  // Amarelo
};

// Função para desenhar uma face triangular
void triangle(int a, int b, int c) {
    glBegin(GL_TRIANGLES); // Inicia a definição de um triângulo
        glColor3fv(colors[a]); // Define a cor do vértice a
        glVertex3fv(vertices[a]); // Define o vértice a
        glColor33fv(colors[b]); // Define a cor do vértice b
        glVertex3fv(vertices[b]); // Define o vértice b
        glColor3fv(colors[c]); // Define a cor do vértice c
        glVertex3fv(vertices[c]); // Define o vértice c
    glEnd(); // Finaliza a definição do triângulo
}

// Função para desenhar o tetraedro completo
void tetrahedron() {
    // Desenha as 4 faces do tetraedro
    triangle(0, 1, 2); // Face 1
    triangle(0, 1, 3); // Face 2
    triangle(0, 2, 3); // Face 3
    triangle(1, 2, 3); // Face 4 (base)
}

// Função de display que será chamada para redesenhar a cena
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // Limpa o buffer de cor e profundidade
    glLoadIdentity(); // Reseta a matriz de transformação do modelo
    gluLookAt(2.0, 2.0, 2.0, // Posição da câmera (olho)
              0.0, 0.0, 0.0, // Ponto para onde a câmera está olhando
              0.0, 0.0, 1.0); // Vetor "up" da câmera

    glPushMatrix(); // Salva a matriz atual
    // Adicionar rotação para ver o tetraedro em movimento (opcional)
    // static GLfloat rotate_y = 0.0;
    // glRotatef(rotate_y, 0.0, 1.0, 0.0);
    // rotate_y += 0.5; // Incrementa a rotação

    tetrahedron(); // Chama a função para desenhar o tetraedro
    glPopMatrix(); // Restaura a matriz salva

    glutSwapBuffers(); // Troca os buffers (exibe o que foi desenhado)
}

// Função para ajustar o viewport quando a janela é redimensionada
void reshape(int w, int h) {
    glViewport(0, 0, w, h); // Define o viewport para o tamanho da janela
    glMatrixMode(GL_PROJECTION); // Seleciona a matriz de projeção
    glLoadIdentity(); // Reseta a matriz de projeção
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 1.0, 100.0); // Define a projeção em perspectiva
    glMatrixMode(GL_MODELVIEW); // Seleciona a matriz de visualização do modelo
}

// Função para lidar com teclas (opcional)
void keyboard(unsigned char key, int x, int y) {
    if (key == 27) { // Pressione ESC para sair
        exit(0);
    }
}

int main(int argc, char** argv) {
    glutInit(&argc, argv); // Inicializa o GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); // Define o modo de exibição (double buffer, RGB, profundidade)
    glutInitWindowSize(600, 600); // Define o tamanho da janela
    glutCreateWindow("Tetraedro em C (OpenGL)"); // Cria a janela com um título

    glEnable(GL_DEPTH_TEST); // Habilita o teste de profundidade (para objetos 3D)
    glEnable(GL_CULL_FACE); // Habilita o culling de faces (melhora o desempenho)
    glCullFace(GL_BACK); // Culling de faces traseiras

    // Define as funções de callback
    glutDisplayFunc(display); // Função de desenho
    glutReshapeFunc(reshape); // Função de redimensionamento
    glutKeyboardFunc(keyboard); // Função de teclado
    // glutIdleFunc(display); // Descomente para animação contínua

    glutMainLoop(); // Inicia o loop principal do GLUT

    return 0;
}