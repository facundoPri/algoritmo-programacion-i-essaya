/* Escribir en C la función int obtener_valor(const int vector[], int len, int
 * pos). La función debe devolver el valor que se encuentra en vector[pos],
 * interpretando pos como en Python. Es decir, pos puede tomar valores entre
 * -len y len - 1; y para los valores negativos busca los elementos comenzando
 * desde la última posición del vector. Si pos no es válida, devolver la
 * constante INT_MIN (asumir que la constante ya fue declarada). */

#include <stdio.h>
#define INT_MIN 0

int obtener_valor(const int vector[], int len, int pos) {
  if (pos < -len || pos > len - 1) {
    return INT_MIN;
  }
  if (pos < 0) {
    printf("pos: %d\n", pos);
    return vector[pos + len];
  }
  return vector[pos];
}

int main() {
  int resultado;
  int vector[] = {1, 2, 3, 4};

  resultado = obtener_valor(vector, 4, -4);

  printf("Resultado = %d", resultado);

  return 0;
}
