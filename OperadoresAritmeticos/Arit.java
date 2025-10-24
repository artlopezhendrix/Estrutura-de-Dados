public class OperadoresAritmeticos {
    public static void main(String[] args) {
        int a = 35, b = 9;
        double resultado;
        
        System.out.println("=== OPERADORES ARITMÉTICOS EM JAVA ===");
        System.out.println("Valores: a = " + a + ", b = " + b + "\n");
        
        // Operações básicas
        System.out.println("Soma: " + a + " + " + b + " = " + (a + b));
        System.out.println("Subtração: " + a + " - " + b + " = " + (a - b));
        System.out.println("Multiplicação: " + a + " * " + b + " = " + (a * b));
        
        // Divisão inteira e real
        System.out.println("Divisão inteira: " + a + " / " + b + " = " + (a / b));
        resultado = (double)a / b;
        System.out.printf("Divisão real: %d / %d = %.2f\n", a, b, resultado);
        
        // Módulo
        System.out.println("Módulo: " + a + " % " + b + " = " + (a % b));
        
        // Operadores unários
        int x = 5;
        System.out.println("\nIncremento: x = " + x + ", ++x = " + (++x));
        System.out.println("Decremento: x = " + x + ", --x = " + (--x));
    }
}