/* Escribir en C un programa que pide al usuario un número n >= 1 (repitiendo */
/* hasta que el número ingresado sea válido), y luego imprime un triángulo de */
/* altura n. Ejemplo: */
/* Ingrese la altura del triangulo: 3 */
/* * */
/* ** */
/* *** */

#include <stdio.h>

int pedir_altura() {
  int n;
  do {
    printf("Ingrese la altura del triangulo: ");
    scanf("%d", &n);
    if (n < 1) {
      printf("Altura Invalida\n");
    }
  } while (n < 1);
  return n;
}

void dibujar_triangulo(int altura) {
  for (int i = 1; i <= altura; i++) {
    /* printf("%d", i); */
    for (int x = 0; x < i; x++) {
      printf("*");
    }
    printf("\n");
  }
}

int main() {
  int altura;
  altura = pedir_altura();
  dibujar_triangulo(altura);
  return 0;
}
