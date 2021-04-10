# Dada la lista [1,2,3,4,5,6,7,8,9,2], mostrar los pasos para ordenarla mediante inserción y mergesort.

# Desarrollar, en no más de 5 renglones, cuál es mejor de entre esos métodos para la lista dada y por qué.

# Mergesort
"""
- [1,2,3,4,5,6,7,8,9,2]
- [1,2,3,4,5][6,7,8,9,2]
- [1,2,3][4,5][6,7,8][9,2]
- [1,2][3][4][5][6,7][8][9][2]
- [1][2][3][4][5][6][7][8][9][2]
- [1,2][3][4][5][6,7][8][9][2]
- [1,2,3][4,5][6,7,8][2,9]
- [1,2,3,4,5][2,6,7,8,9]
- [1,2,2,3,4,5,6,7,8,9]
"""

# Insercion
"""
- [1,2,3,4,5,6,7,8,9,2]
- [1,2,2,3,4,5,6,7,8,9]
"""

"""
Para casos donde tenemos una lista casi ordenada es mejor utilizar insercion ya que en estos casos el algoritmo es lineal o casi lineal, su mejor caso es t(n)
Mergesort por el otro lado es un algoritmo t(nlog2n) para todos sus casos.
"""
