// --- 1. Função Básica: Soma de Dois Números ---
function somarNumeros(num1, num2) {
  // O 'return' especifica o valor que a função deve produzir.
  return num1 + num2;
}

// --- 2. Função Condicional: Verifica Par ou Ímpar ---
function verificarParImpar(numero) {
  // O operador de módulo (%) retorna o resto da divisão.
  if (numero % 2 === 0) {
    return "O número " + numero + " é Par.";
  } else {
    return "O número " + numero + " é Ímpar.";
  }
}

function converterParaMaiusculas(texto) {
  // O método .toUpperCase() é um método embutido (built-in) de strings em JS.
  return texto.toUpperCase();
}

// ==========================================================
// --- Exemplos de Uso das Funções ---

// 1. Chamando a função de soma
let resultadoSoma = somarNumeros(15, 7);
console.log("Resultado da Soma (15 + 7):", resultadoSoma); // Saída: 22