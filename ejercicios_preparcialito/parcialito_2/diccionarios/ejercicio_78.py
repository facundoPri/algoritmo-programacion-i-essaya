"""
Dado un diccionario cuyas claves son strings y sus valores son listas de enteros, escribir una función que invierta dicho diccionario de la siguiente forma: cada valor de cada lista pasará a ser una clave del diccionario resultante, que tendrá como valor una lista de todas las claves en las que era un valor. Por ejemplo, d = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]} dara como resultado {1: ["clave_1", "clave_3"], 2: ["clave_1"], 3: ["clave_1"], 4: ["clave_2", "clave_3"], 6: ["clave_2"]}.
"""

dicc = {"clave_1": [1, 2, 3], "clave_2": [4, 6], "clave_3": [1, 4]}


def invertir_dicc(diccionario):
    """
    Recibe un diccionarion conde las clase son cadenas y los valores una lista de enteros
    Devuelve un diccionario donde cada uno de los enteros en una clave y sus valores son sus antiguas claves
    """
    resultado = {}
    for clave, valores in diccionario.items():
        for valor in valores:
            if valor in resultado:
                resultado[valor].append(clave)
            else:
                resultado[valor] = [clave]
    return resultado


print(invertir_dicc(dicc))
