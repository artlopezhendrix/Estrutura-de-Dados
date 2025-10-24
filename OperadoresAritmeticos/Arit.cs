using System;

class Program {
    static void Main() {
        int a = 25, b = 7;
        double resultado;
        
        Console.WriteLine("=== OPERADORES ARITMÉTICOS EM C# ===");
        Console.WriteLine($"Valores: a = {a}, b = {b}\n");
        
        Console.WriteLine($"Soma: {a} + {b} = {a + b}");
        Console.WriteLine($"Subtração: {a} - {b} = {a - b}");
        Console.WriteLine($"Multiplicação: {a} * {b} = {a * b}");
        
        Console.WriteLine($"Divisão inteira: {a} / {b} = {a / b}");
        resultado = (double)a / b;
        Console.WriteLine($"Divisão real: {a} / {b} = {resultado:F2}");
        
        Console.WriteLine($"Módulo: {a} % {b} = {a % b}");
        
        int x = 10;
        Console.WriteLine($"\nIncremento: x = {x}, ++x = {++x}");
        Console.WriteLine($"Decremento: x = {x}, --x = {--x}");
    }
}