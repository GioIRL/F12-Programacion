#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int busqueda_dos_en_dos(const vector<int>& lista, int n, int objetivo) {
    int i = 0;
    
    // Avanzar de 2 en 2 mientras el elemento sea menor al objetivo
    while (i < n && lista[i] < objetivo) {
        i += 2;
    }
    
    // Retroceder 1 posicion (el objetivo puede estar en i-1 o i)
    i = i - 1;
    
    // Revisar hasta 2 posiciones a partir de i
    for (int j = max(0, i); j <= min(i + 1, n - 1); ++j) {
        if (lista[j] == objetivo) {
            return j;
        }
    }
    
    return -1; // no encontrado
}

int main() {
    int n, objetivo;
    if (!(cin >> n)) return 0;
    vector<int> lista(n);
    for (int i = 0; i < n; ++i) cin >> lista[i];
    cin >> objetivo;
    
    cout << busqueda_dos_en_dos(lista, n, objetivo) << endl;
    return 0;
}