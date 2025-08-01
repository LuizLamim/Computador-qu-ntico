#include <SFML/Graphics.hpp>
#include <cmath>

int main() {
    // 1. Configurações da Janela
    const int windowWidth = 800;
    const int windowHeight = 600;
    sf::RenderWindow window(sf::VideoMode(windowWidth, windowHeight), "Grafico de cos(x) + 3x");
    window.setFramerateLimit(60);

    // 2. Configurações do Grafico
    const double xMin = -10.0;
    const double xMax = 10.0;
    const double yMin = -30.0;
    const double yMax = 30.0;
    
    const double xRange = xMax - xMin;
    const double yRange = yMax - yMin;

    // Fatores de escala para mapear do sistema de coordenadas para a janela
    const double xScale = windowWidth / xRange;
    const double yScale = windowHeight / yRange;

    // 3. Desenha os Eixos
    sf::Vertex xAxis[] = {
        sf::Vertex(sf::Vector2f(0, windowHeight - (0 - yMin) * yScale)),
        sf::Vertex(sf::Vector2f(windowWidth, windowHeight - (0 - yMin) * yScale))
    };
    sf::Vertex yAxis[] = {
        sf::Vertex(sf::Vector2f((0 - xMin) * xScale, 0)),
        sf::Vertex(sf::Vector2f((0 - xMin) * xScale, windowHeight))
    };

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::White);

        // Desenha os eixos
        window.draw(xAxis, 2, sf::Lines);
        window.draw(yAxis, 2, sf::Lines);

        // 4. Desenha a Funcao
        sf::VertexArray functionPlot(sf::LinesStrip, windowWidth);
        for (int i = 0; i < windowWidth; ++i) {
            // Mapeia o pixel 'i' para um valor de x
            double x = xMin + (double)i / windowWidth * xRange;
            
            // Calcula o valor da funcao para este x
            double y = std::cos(x) + 3 * x;

            // Mapeia o valor de x e y para as coordenadas da janela
            float screenX = (x - xMin) * xScale;
            float screenY = windowHeight - (y - yMin) * yScale;
            
            functionPlot[i].position = sf::Vector2f(screenX, screenY);
            functionPlot[i].color = sf::Color::Red;
        }

        window.draw(functionPlot);
        window.display();
    }

    return 0;
}