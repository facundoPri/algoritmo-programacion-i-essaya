/* Ej_3 - Escribir una función en C que le pida al usuario que ingrese números
 * del 0 al 9. Repetir este proceso hasta que el usuario ingresa -1. */
/* Luego, mostrar por pantalla cuantas veces ingresó cada número. */
/* Ayuda: usar un arreglo con las posiciones del 0 al 9 como diccionario */

#include <stdio.h>

void pedir_numero(int numeros[]) {
  int n;
  do {
    printf("Ingresar numero del 0 a 9. -1 para salir: ");
    scanf("%d", &n);
    if (n < -1 || n > 9) {
      printf("Numero no es valido\n");
      continue;
    }
    numeros[n]++;
    printf("Numero agregado\n");
  } while (n != -1);
}

void mostrar_numeros(int numeros[], int numeros_len) {
  for (int i = 0; i < numeros_len; i++) {
    if (numeros[i] <= 0) {
      continue;
    }
    printf("Se ingreso %d, %d veces\n", i, numeros[i]);
  }
}

int main() {
  int numeros[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  pedir_numero(numeros);
  mostrar_numeros(numeros, 10);
  return 0;
}
