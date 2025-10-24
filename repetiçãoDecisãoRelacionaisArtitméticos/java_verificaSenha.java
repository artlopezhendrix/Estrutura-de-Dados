import java.util.Scanner;

public class VerificaSenha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String senhaCorreta = "1234";
        String senhaDigitada;
        
        System.out.print("Digite a senha: ");
        senhaDigitada = scanner.nextLine();
        
        while(!senhaDigitada.equals(senhaCorreta)) {
            System.out.println("❌ Senha incorreta!");
            System.out.print("Digite a senha novamente: ");
            senhaDigitada = scanner.nextLine();
        }
        
        System.out.println("✅ Senha correta!");
        scanner.close();
    }
}