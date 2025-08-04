#include <iostream>
#include <fstream>
#include <string>

void criar_quadrado_svg() {
    // Definir o nome do arquivo
    std::string nome_arquivo = "quadrado_cpp.svg";
    
    // Abrir o arquivo para escrita
    std::ofstream arquivo_svg(nome_arquivo);
    
    // Verificar se o arquivo foi aberto com sucesso
    if (!arquivo_svg.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << nome_arquivo << " para escrita." << std::endl;
        return;
    }
    
    // Escrever o cabeçalho do arquivo SVG
    arquivo_svg << "<?xml version=\"1.0\" standalone=\"no\"?>\n";
    arquivo_svg << "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n";
    arquivo_svg << "<svg width=\"200\" height=\"200\" viewBox=\"-10 -10 120 120\" xmlns=\"http://www.w3.org/2000/svg\">\n";

    // Escrever o quadrado usando a tag <polyline>
    // As coordenadas são escalonadas (de 0 a 100) para melhor visualização
    arquivo_svg << "  <polyline points=\"0,0 100,0 100,100 0,100 0,0\" \n";
    arquivo_svg << "    style=\"fill:none;stroke:red;stroke-width:2\" />\n";
    
    // Escrever o rótulo (título)
    arquivo_svg << "  <text x=\"50\" y=\"-5\" font-size=\"12\" text-anchor=\"middle\">Quadrado de Lado 1 (C++)</text>\n";

    // Escrever o rodapé do arquivo SVG
    arquivo_svg << "</svg>\n";

    // O destrutor de std::ofstream fecha o arquivo automaticamente
    
    std::cout << "Arquivo '" << nome_arquivo << "' criado com sucesso. Abra-o no seu navegador para ver o gráfico." << std::endl;
}

int main() {
    criar_quadrado_svg();
    return 0;
}