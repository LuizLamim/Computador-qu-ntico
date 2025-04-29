function calcularGradiente(funcao, x, y, delta = 1e-6) {
    // Calcula as derivadas parciais numericamente usando a definição de limite
  
    // Derivada parcial em relação a x
    const dfdx = (funcao(x + delta, y) - funcao(x - delta, y)) / (2 * delta);
  
    // Derivada parcial em relação a y
    const dfdy = (funcao(x, y + delta) - funcao(x, y - delta)) / (2 * delta);
  
    return [dfdx, dfdy];
  }
  
  // Exemplo de função escalar: f(x, y) = x^2 + y^2
  function minhaFuncao(x, y) {
    return Math.pow(x, 2) + Math.pow(y, 2);
  }
  
  // Ponto no qual queremos calcular o gradiente
  const pontoX = 2;
  const pontoY = 3;
  
  // Calcula o vetor gradiente
  const gradiente = calcularGradiente(minhaFuncao, pontoX, pontoY);
  
  console.log(`O vetor gradiente de f(x, y) em (${pontoX}, ${pontoY}) é: [${gradiente[0]}, ${gradiente[1]}]`);