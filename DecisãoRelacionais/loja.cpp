#include <iostream>
using namespace std;

int main() {
    float valorCompra;
    cout << "Digite o valor da compra: ";
    cin >> valorCompra;

    if (valorCompra >= 100) {
        cout << "Frete Grátis" << endl;
    } else {
        float total = valorCompra + 15;
        cout << "Valor total com frete: " << total << " reais" << endl;
    }

    return 0;
}