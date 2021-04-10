# Explicar los pasos del ordenamiento de la lista [6,1,44,5,17,23,29,10] usando el algoritmo de MergeSort

"""
- [6,1,44,5,17,23,29,10] pasamos la lista a mergesort
- [6,1,44,5][17,23,29,10] dividimos la lista en dos y se pasa cada lista a mergesort
- [6,1][44,5][17,23][29,10] cada lista se vuelve a didivir en dos y se pasa a mergesort de vuelta
- [6][1][44][5][17][23][29][10] como el tamaño de cada lista es uno se devuelve la misma lista a la llamada anterior
- [1,6][5,44][17,23][10,29] se empieza a aplicar la funcion merge ordenando las dos listas pasadas
- [1,5,6,44][10,17,23,29] merge recibe dos listas ordenadas y las ordenas entre si
- [1,5,6,10,17,23,29,44] lista ordenada
"""
