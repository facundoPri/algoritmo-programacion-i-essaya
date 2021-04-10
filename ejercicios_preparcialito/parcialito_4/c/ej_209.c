/*
** Escribir en C una función que reciba un número secreto n (de tipo int) y le
*pregunte un número al usuario. Si el número ingresado es distinto a n, debe
*indicarle si es mayor o menor y volver a pedirle otro número. Si es igual, debe
*felicitar al usuario y mostrar en cuántos intentos adivinó.
**
*/
#include <stdio.h>

void pedir_numero(int numero_secreto) {
  int n;
  do {
    printf("Enter an integer : ");
    scanf("%d", &n);

    if (n > numero_secreto) {
      printf("Numero secreto es menor\n");
    } else if (n < numero_secreto) {
      printf("Numero secreto es mayor\n");
    }

  } while (n != numero_secreto);
  printf("Adivinaste el numero!\n");
}

int main() {
  pedir_numero(10);

  return 0;
}
