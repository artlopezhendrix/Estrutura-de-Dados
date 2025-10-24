#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a = 20, b = 6;
    double resultado;
    
    cout << "=== OPERADORES ARITMÉTICOS EM C++ ===" << endl;
    cout << "Valores: a = " << a << ", b = " << b << endl << endl;
    
    cout << "Soma: " << a << " + " << b << " = " << (a + b) << endl;
    cout << "Subtração: " << a << " - " << b << " = " << (a - b) << endl;
    cout << "Multiplicação: " << a << " * " << b << " = " << (a * b) << endl;
    
    cout << "Divisão inteira: " << a << " / " << b << " = " << (a / b) << endl;
    resultado = static_cast<double>(a) / b;
    cout << fixed << setprecision(2);
    cout << "Divisão real: " << a << " / " << b << " = " << resultado << endl;
    
    cout << "Módulo: " << a << " % " << b << " = " << (a % b) << endl;
    
    return 0;
}