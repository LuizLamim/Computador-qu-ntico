import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class FuncoesUsuais {

    public static void main(String[] args) {
        // 1. Entrada de dados (Scanner)
        Scanner leitor = new Scanner(System.in);

        System.out.println("--- Bem-vindo ao Demo Java ---");
        System.out.print("Digite seu nome: ");
        String nome = leitor.nextLine();

        // 2. Condicionais (if/else)
        System.out.print("Digite sua idade: ");
        int idade = leitor.nextInt();

        if (idade >= 18) {
            System.out.println(nome + ", você é maior de idade.");
        } else {
            System.out.println(nome + ", você é menor de idade.");
        }

        // 3. Estruturas de Repetição (for) e Listas (ArrayList)
        System.out.println("\n--- Trabalhando com Listas ---");
        List<String> linguagens = new ArrayList<>();
        linguagens.add("Java");
        linguagens.add("Python");
        linguagens.add("JavaScript");

        System.out.println("Linguagens populares:");
        for (int i = 0; i < linguagens.size(); i++) {
            System.out.println((i + 1) + "º: " + linguagens.get(i));
        }