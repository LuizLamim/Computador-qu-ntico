
public class SomaTresNumeros {
    public static void main(String[] args) {

        canner leitor = new Scanner(System.in);
        
        System.out.println("--- Calculadora de Soma de 3 Números ---");

        // 2. Pede e lê o primeiro número
        System.out.print("Digite o primeiro número: ");
        int numero1 = leitor.nextInt();

        // 3. Pede e lê o segundo número
        System.out.print("Digite o segundo número: ");
        int numero2 = leitor.nextInt();

        // 4. Pede e lê o terceiro número
        System.out.print("Digite o terceiro número: ");
        int numero3 = leitor.nextInt();

        // 5. Realiza a soma
        int soma = numero1 + numero2 + numero3;