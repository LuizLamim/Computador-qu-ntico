#include <iostream>
#include <vector>
#include <cmath>
#include <fstream> // Para salvar os dados em um arquivo

// Constantes físicas
const double G = 6.67430e-11; // Constante gravitacional (m^3 kg^-1 s^-2)
const double MASSA_SOL = 1.989e30; // Massa do Sol (kg)
const double MASSA_TERRA = 5.972e24; // Massa da Terra (kg)

// Distância média Terra-Sol (unidade astronômica em metros)
const double AU = 1.496e11; // 1 UA em metros

// Estrutura para representar um corpo celestial
struct CorpoCelestial {
    double massa;
    double x, y; // Posição (m)
    double vx, vy; // Velocidade (m/s)
    double fx, fy; // Força (N)
};

// Função para calcular a força gravitacional entre dois corpos
void calcularForca(CorpoCelestial& corpo1, const CorpoCelestial& corpo2) {
    double dx = corpo2.x - corpo1.x;
    double dy = corpo2.y - corpo1.y;
    double distancia = std::sqrt(dx * dx + dy * dy);

    // Evitar divisão por zero se os corpos estiverem na mesma posição (improvável em órbita)
    if (distancia < 1e3) { // Pequeno valor para evitar instabilidade
        corpo1.fx = 0.0;
        corpo1.fy = 0.0;
        return;
    }

    double forcaMagnitude = (G * corpo1.massa * corpo2.massa) / (distancia * distancia);

    // Componentes da força
    corpo1.fx = forcaMagnitude * (dx / distancia);
    corpo1.fy = forcaMagnitude * (dy / distancia);
}

int main() {
    // Inicialização do Sol (no centro do sistema de coordenadas)
    CorpoCelestial sol;
    sol.massa = MASSA_SOL;
    sol.x = 0.0;
    sol.y = 0.0;
    sol.vx = 0.0;
    sol.vy = 0.0;

    // Inicialização da Terra
    CorpoCelestial terra;
    terra.massa = MASSA_TERRA;
    terra.x = AU; // Começa a 1 UA do Sol no eixo X
    terra.y = 0.0;

    // Velocidade inicial da Terra para uma órbita aproximadamente circular
    // A velocidade orbital (v) para uma órbita circular é sqrt(G * M_sol / r)
    terra.vx = 0.0;
    terra.vy = std::sqrt(G * MASSA_SOL / AU); // Velocidade inicial no eixo Y

    // Parâmetros da simulação
    double dt = 3600.0; // Passo de tempo em segundos (1 hora)
    double tempoTotal = 365.25 * 24.0 * 3600.0; // Um ano terrestre em segundos
    int numPassos = static_cast<int>(tempoTotal / dt);

    // Abrir arquivo para salvar os dados da órbita
    std::ofstream arquivoSaida("orbita_terra.txt");
    if (!arquivoSaida.is_open()) {
        std::cerr << "Erro ao abrir o arquivo de saída!" << std::endl;
        return 1;
    }

    // Cabeçalho do arquivo de saída
    arquivoSaida << "Tempo(s)\tTerra_X(m)\tTerra_Y(m)\n";

    // Loop de simulação
    for (int i = 0; i < numPassos; ++i) {
        // Calcular a força do Sol sobre a Terra
        calcularForca(terra, sol);

        // Atualizar a velocidade da Terra usando a Segunda Lei de Newton (F = ma => a = F/m)
        terra.vx += (terra.fx / terra.massa) * dt;
        terra.vy += (terra.fy / terra.massa) * dt;

        // Atualizar a posição da Terra (método de Euler)
        terra.x += terra.vx * dt;
        terra.y += terra.vy * dt;

        // Salvar os dados (convertendo para AU para melhor visualização)
        arquivoSaida << i * dt << "\t" << terra.x / AU << "\t" << terra.y / AU << "\n";

        // Opcional: imprimir progresso
        if (i % (numPassos / 10) == 0) {
            std::cout << "Progresso: " << (double)i / numPassos * 100.0 << "%\n";
        }
    }

    arquivoSaida.close();
    std::cout << "Simulação concluída. Dados salvos em 'orbita_terra.txt'\n";
    std::cout << "Você pode plotar os dados (Terra_X vs Terra_Y) usando ferramentas como Gnuplot, Matplotlib (Python) ou Excel." << std::endl;

    return 0;
}