#include <stdio.h>

void criar_quadrado_svg() {
    // Abrir o arquivo para escrita
    FILE *arquivo_svg = fopen("quadrado.svg", "w");
    if (arquivo_svg == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return;
    }

    // Escrever o cabeçalho do arquivo SVG
    fprintf(arquivo_svg, "<?xml version=\"1.0\" standalone=\"no\"?>\n");
    fprintf(arquivo_svg, "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n");
    fprintf(arquivo_svg, "<svg width=\"200\" height=\"200\" viewBox=\"-10 -10 120 120\" xmlns=\"http://www.w3.org/2000/svg\">\n");

    // Escrever o quadrado usando a tag <polyline>
    // As coordenadas são escalonadas (de 0 a 100) para melhor visualização
    // A tag <polyline> desenha uma série de segmentos de linha
    fprintf(arquivo_svg, "  <polyline points=\"0,0 100,0 100,100 0,100 0,0\" \n");
    fprintf(arquivo_svg, "    style=\"fill:none;stroke:blue;stroke-width:2\" />\n");
    
    // Escrever o rótulo (título)
    fprintf(arquivo_svg, "  <text x=\"50\" y=\"-5\" font-size=\"12\" text-anchor=\"middle\">Quadrado de Lado 1</text>\n");

    // Escrever o rodapé do arquivo SVG
    fprintf(arquivo_svg, "</svg>\n");

    // Fechar o arquivo
    fclose(arquivo_svg);

    printf("Arquivo 'quadrado.svg' criado com sucesso. Abra-o no seu navegador para ver o gráfico.\n");
}

int main() {
    criar_quadrado_svg();
    return 0;
}