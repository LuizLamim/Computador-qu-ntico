<!DOCTYPE html>
<html>
<head>
<title>Gráfico de ∫ x sen(x) dx</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
  <div id="grafico"></div>

  <script>
    // Função para calcular a integral indefinida de x * sen(x) dx
    // A integral de x * sen(x) dx é -x * cos(x) + sen(x) + C
    function calcularIntegral(x) {
      return -x * Math.cos(x) + Math.sin(x);
    }

    // Definir o intervalo de valores de x
    const inicioX = -10;
    const fimX = 10;
    const numeroPontos = 200; // Mais pontos para um gráfico mais suave
    const passo = (fimX - inicioX) / numeroPontos;

    // Criar arrays para armazenar os valores de x e y
    const xValores = [];
    const yValores = [];

    // Calcular os valores de y para cada valor de x
    for (let i = 0; i <= numeroPontos; i++) {
      const x = inicioX + i * passo;
      xValores.push(x);
      yValores.push(calcularIntegral(x));
    }

    // Dados para o Plotly
    const data = [{
      x: xValores,
      y: yValores,
      type: 'scatter',
      mode: 'lines',
      name: '∫ x sen(x) dx = -x cos(x) + sen(x)'
    }];

    // Layout do gráfico
    const layout = {
      title: 'Gráfico da Integral de x sen(x) dx',
      xaxis: {
        title: 'x'
      },
      yaxis: {
        title: 'y = -x cos(x) + sen(x)'
      }
    };

    // Plotar o gráfico usando Plotly
    Plotly.newPlot('grafico', data, layout);
  </script>
</body>
</html>