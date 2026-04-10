#include <iostream>

using namespace std;

int main() {
    long long n;
    if (!(cin >> n)) return 0;
    
    long long suma = 0;
    // Repita mientras n > 0
    while (n > 0) {
        suma += n % 10; // obtener el último dígito
        n /= 10;        // eliminar el último dígito
    }
    
    cout << suma << endl;
    return 0;
}
