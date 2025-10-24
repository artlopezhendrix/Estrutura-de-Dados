#include <stdio.h>

int main() {
    int numero;
    
    printf("Digite um número para ver sua tabuada: ");
    scanf("%d", &numero);
    
    printf("\nTabuada do %d:\n", numero);
    printf("----------------\n");
    
    for(int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }
    
    return 0;
}