#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 0;
    
    // Casos especiales: n < 2 no es primo
    if (n < 2) {
        cout << "no primo";
        return 0;
    }
    // n = 2 es el único par primo
    if (n == 2) {
        cout << "primo";
        return 0;
    }
    // Todo número par mayor a 2 no es primo
    if (n % 2 == 0) {
        cout << "no primo";
        return 0;
    }
    
    bool es_primo = true;
    // Basta con verificar hasta la raíz cuadrada de n
    int limite = sqrt(n);
    for (int d = 3; d <= limite; d += 2) {
        if (n % d == 0) {
            es_primo = false;
            break;
        }
    }
    
    if (es_primo) cout << "primo";
    else cout << "no primo";
    
    return 0;
}
