"""
Se tiene un archivo CSV de tres columnas llamado operaciones.csv. Las columnas son: Cuenta (nombre de la cuenta, cadena), Operacion (tipo de la operación: "extraccion" o "deposito") y Monto (valor de la operación, un entero positivo). El archivo está ordenado por el campo “Cuenta”.

Se pide escribir un programa que imprima por pantalla el balance de cada cuenta tras procesar las operaciones presentes en el archivo. Se debe asumir un balance inicial de 0. (Nota: las extracciones restan al valor del balance y los depósitos suman al mismo.)

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv


def hacer_balance_cuentas(ruta_archivo):
    """
    Recibe la ruta de un archivo csv donde estan los depositos y las extracciones de distintas cuentas
    Imprime en pantalla el balance de cada cuenta
    """
    with open(ruta_archivo) as f:
        operaciones = csv.DictReader(f)
        cuenta = None
        balance = 0
        for operacion in operaciones:
            if cuenta and not cuenta == operacion["Cuenta"]:
                nl = "\n"
                print(f"Cuenta: {cuenta}{nl}Balance: {balance}")
                balance = 0
            cuenta = operacion["Cuenta"]
            if operacion["Operacion"] == "d":
                balance += int(operacion["Monto"])
            elif operacion["Operacion"] == "e":
                balance -= int(operacion["Monto"])
        print(f"Cuenta: {cuenta}{nl}Balance: {balance}")


print(hacer_balance_cuentas("operaciones.csv"))
