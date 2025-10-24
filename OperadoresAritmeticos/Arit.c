#include <stdio.h>

int main() {
    int a = 15, b = 4;
    float resultado;
    
    printf("=== OPERADORES ARITMÉTICOS EM C ===\n");
    printf("Valores: a = %d, b = %d\n\n", a, b);
    
    printf("Soma: %d + %d = %d\n", a, b, a + b);
    printf("Subtração: %d - %d = %d\n", a, b, a - b);
    printf("Multiplicação: %d * %d = %d\n", a, b, a * b);
    
    printf("Divisão inteira: %d / %d = %d\n", a, b, a / b);
    resultado = (float)a / b;
    printf("Divisão real: %d / %d = %.2f\n", a, b, resultado);
    
    printf("Módulo: %d %% %d = %d\n", a, b, a % b);
    
    return 0;
}