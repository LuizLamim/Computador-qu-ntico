#include <iostream>
#include <vector>
#include <cmath>
#include <fstream> // Para salvar os dados em um arquivo

// Constantes físicas
const double G = 6.67430e-11; // Constante gravitacional (m^3 kg^-1 s^-2)
const double MASSA_SOL = 1.989e30; // Massa do Sol (kg)

// --- Constantes específicas de Júpiter ---
const double MASSA_JUPITER = 1.898e27; // Massa de Júpiter (kg)
// Distância média Júpiter-Sol (unidade astronômica em metros)
const double AU_JUPITER = 5.204 * 1.496e11; // 5.204 UA em metros (aproximadamente)

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

    // Inicialização de Júpiter
    CorpoCelestial jupiter;
    jupiter.massa = MASSA_JUPITER;
    jupiter.x = AU_JUPITER; // Começa a 5.204 UA do Sol no eixo X
    jupiter.y = 0.0;

    // Velocidade inicial de Júpiter para uma órbita aproximadamente circular
    // A velocidade orbital (v) para uma órbita circular é sqrt(G * M_sol / r)
    jupiter.vx = 0.0;
    jupiter.vy = std::sqrt(G * MASSA_SOL / AU_JUPITER); // Velocidade inicial no eixo Y

    // Parâmetros da simulação
    // O período orbital de Júpiter é de aproximadamente 11.86 anos terrestres
    double dt = 3600.0 * 24; // Passo de tempo em segundos (1 dia) - Aumentado para Júpiter
    double tempoTotal = 11.86 * 365.25 * 24.0 * 3600.0; // Um período orbital de Júpiter em segundos
    int numPassos = static_cast<int>(tempoTotal / dt);

    // Abrir arquivo para salvar os dados da órbita
    std::ofstream arquivoSaida("orbita_jupiter.txt");
    if (!arquivoSaida.is_open()) {
        std::cerr << "Erro ao abrir o arquivo de saída!" << std::endl;
        return 1;
    }

    // Cabeçalho do arquivo de saída
    arquivoSaida << "Tempo(s)\tJupiter_X(UA)\tJupiter_Y(UA)\n";

    // Loop de simulação
    for (int i = 0; i < numPassos; ++i) {
        // Calcular a força do Sol sobre Júpiter
        calcularForca(jupiter, sol);

        // Atualizar a velocidade de Júpiter usando a Segunda Lei de Newton (F = ma => a = F/m)
        jupiter.vx += (jupiter.fx / jupiter.massa) * dt;
        jupiter.vy += (jupiter.fy / jupiter.massa) * dt;

        // Atualizar a posição de Júpiter (método de Euler)
        jupiter.x += jupiter.vx * dt;
        jupiter.y += jupiter.vy * dt;

        // Salvar os dados (convertendo para AU para melhor visualização)
        arquivoSaida << i * dt << "\t" << jupiter.x / (1.496e11) << "\t" << jupiter.y / (1.496e11) << "\n";

        // Opcional: imprimir progresso
        if (i % (numPassos / 10) == 0) {
            std::cout << "Progresso: " << (double)i / numPassos * 100.0 << "%\n";
        }
    }

    arquivoSaida.close();
    std::cout << "Simulação de Júpiter concluída. Dados salvos em 'orbita_jupiter.txt'\n";
    std::cout << "Você pode plotar os dados (Jupiter_X vs Jupiter_Y) usando ferramentas como Gnuplot, Matplotlib (Python) ou Excel." << std::endl;

    return 0;
}