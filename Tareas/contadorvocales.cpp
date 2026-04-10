#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string linea;
    // Leer la línea completa de texto
    if (!getline(cin, linea)) return 0;
    
    int conteo = 0;
    // Recorrer la cadena carácter a carácter
    for (char c : linea) {
        char minuscula = tolower(c); // convertir a minúscula
        if (minuscula == 'a' || minuscula == 'e' || minuscula == 'i' || 
            minuscula == 'o' || minuscula == 'u') {
            conteo++;
        }
    }
    
    cout << conteo << endl;
    return 0;
}
