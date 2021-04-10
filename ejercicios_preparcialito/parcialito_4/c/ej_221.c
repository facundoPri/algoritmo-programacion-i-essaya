/* Implementar en C una función que reciba una cadena e imprima la cantidad de
 * letras, números y espacios presentes en la misma. Usar las funciones de la
 * biblioteca: int isalpha(char), int isdigit(char), isspace(char). */
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void imprimir_string(char string[], int len) {
  int letras = 0;
  int numeros = 0;
  int espacios = 0;
  for (int i = 0; i < len; i++) {
    if (isalpha(string[i])) {
      letras++;
    } else if (isdigit(string[i])) {
      numeros++;
    } else if (isspace(string[i])) {
      espacios++;
    }
  }
  printf("letras: %d, numeros: %d, espacios: %d", letras, numeros, espacios);
}

int main() {
  char string[] = "hola soy facu y tengo 19 anos";
  imprimir_string(string, strlen(string));
  return 0;
}
