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