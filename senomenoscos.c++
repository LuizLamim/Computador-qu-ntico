#include <SFML/Graphics.hpp>
#include <cmath>

int main() {
    // Configurações da janela
    const int windowWidth = 800;
    const int windowHeight = 600;
    sf::RenderWindow window(sf::VideoMode(windowWidth, windowHeight), "Plot de sen(x) - cos(x)");

    // Configurações da curva
    const float scaleX = 80.0f; // Escala do eixo X
    const float scaleY = 80.0f; // Escala do eixo Y
    const float xOffset = windowWidth / 2.0f; // Deslocamento para o centro (eixo X)
    const float yOffset = windowHeight / 2.0f; // Deslocamento para o centro (eixo Y)
    const float pi = M_PI;

    // Vértices para a curva
    sf::VertexArray curve(sf::LineStrip);

    // Loop para calcular os pontos da curva de -2*pi a 2*pi
    for (float x = -2.0f * pi; x <= 2.0f * pi; x += 0.01f) {
        // AQUI ESTÁ A ÚNICA MUDANÇA: a função é sen(x) - cos(x)
        float y = std::sin(x) - std::cos(x);

        // Converte as coordenadas matemáticas para coordenadas de tela
        float screenX = x * scaleX + xOffset;
        float screenY = -y * scaleY + yOffset; // O eixo Y da SFML é invertido

        curve.append(sf::Vertex(sf::Vector2f(screenX, screenY), sf::Color::Cyan));
    }

    // Configurações dos eixos (opcional, para visualização)
    sf::VertexArray xAxis(sf::Lines, 2);
    xAxis[0].position = sf::Vector2f(0, yOffset);
    xAxis[1].position = sf::Vector2f(windowWidth, yOffset);
    xAxis[0].color = sf::Color::White;
    xAxis[1].color = sf::Color::White;

    sf::VertexArray yAxis(sf::Lines, 2);
    yAxis[0].position = sf::Vector2f(xOffset, 0);
    yAxis[1].position = sf::Vector2f(xOffset, windowHeight);
    yAxis[0].color = sf::Color::White;
    yAxis[1].color = sf::Color::White;

    // Loop principal da aplicação
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::Black);
        window.draw(xAxis);
        window.draw(yAxis);
        window.draw(curve);
        window.display();
    }

    return 0;
}