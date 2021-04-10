# Se quiere seleccionar un algoritmo de ordenamiento que va a ser usado para ordenar varias listas de elementos. Teniendo en cuenta que se sospecha que cada lista está muy próxima a estar ordenada en sentido inverso, se proponen dos alternativas: (1) usar mergesort, (2) invertir el arreglo in-place y usar inserción. Justificar cuáles son las ventajas y desventajas de cada caso.

# 1 - usar mergesort
"""
Mergesort es que tiene un resultado estable, para todas las listas pasadas mergesort va a ser N log N. El promedio de este algoritmo es mas rapido y el peor caso de mergesort son mejores que insercion.
La ventaja es que te da un resultado predesible, la desventaja es que no existe mejor caso, donde mergesort pueda ser mas rapido y que al no ser in-place ocupa mas memoria
"""

# 2 - invetir el arreglo in-place y usar insercion
"""
Primer ventaja es que los dos algoritmos son in-place
Segundo al estar casi ordenadas las listas podemos oprovechar del mejor caso de insercion, pero por el otro lado en necesario invertir la lista para poder hacerlo.
Como invertir la lista in-place es un algoritmo minimamente O(n) ahora estamos hablando que este algortmo es igual a uno O(n) mas otro que en el mejor de los caso tambien es O(n).
Esto termina haciendo con que este algoritmo empiece a ser ventajoso ante mergesort en menos casos
Otra desventaja es que el algoritmo no es estable ya que depende de como se encuentra la lista pasada. Lo que puede terminar llevando a un algoritmo mucho mas lento para ciertos casos
"""
