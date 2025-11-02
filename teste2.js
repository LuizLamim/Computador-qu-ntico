function imprimirDezPrimeirosPositivos() {
    // Definimos o limite (quantos números queremos imprimir)
    const limite = 10;

    console.log("Os 10 primeiros números positivos são:")

    for (let i = 1; i <= limite; i++) {
        console.log(i);
    }
}

// Chamamos a função para executar o programa
imprimirDezPrimeirosPositivos();