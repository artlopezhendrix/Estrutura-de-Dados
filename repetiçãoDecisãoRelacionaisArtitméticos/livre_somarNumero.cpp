#include <iostream>
using namespace std;

int main() {
    int numero, soma = 0;
    
    cout << "Digite 5 numeros para somar:" << endl;
    
    for(int i = 1; i <= 5; i++) {
        cout << "Numero " << i << ": ";
        cin >> numero;
        
        if(numero > 0) {
            soma += numero;
        } else {
            cout << "Numero negativo" << endl;
        }
    }
    
    cout << "Soma total: " << soma << endl;
    
    return 0;
}