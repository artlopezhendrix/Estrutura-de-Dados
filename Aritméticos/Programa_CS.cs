using System;
class Program {

static void Main() {
        // Solicitação dos valores e conversão de string para inteiro
        Console.Write("\nDigite o primeiro número: ");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("\nDigite o segundo número (diferente de zero): ");
        int num2 = Convert.ToInt32(Console.ReadLine());

        // Declaração das variáveis para armazenar os resultados
        int soma, sub, mult;
        float div;

        // Realização dos cálculos dos dois números
        soma = num1 + num2;
        sub = num1 - num2;
        mult = num1 * num2;
        div = (float)num1 / (float)num2;

        // Exibe dos resultados das operações ao final
        Console.WriteLine("\nResultados:");
        Console.WriteLine("Soma: " + soma);
        Console.WriteLine("Subtração: " + sub);
        Console.WriteLine("Multiplicação: " + mult);
        Console.WriteLine("Divisão: " + div);
    }
}

