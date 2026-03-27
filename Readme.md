Mateo Jiménez

Descripción:
Mi algoritmo lo que hace es que primero crea una lista en blanco, después se pregunta al usuario que tengo elementos desea en la lista y en base a eso se crea un variable.
Esa variable se usa para definir el rango del primer lazo for. Uso enumerate para no tener que trabajar con una variable por separado para enlistar.
después un lista.append para agregar los números del usuario.
Entonces se imprime la lista original del usuario.

Luego para ordenarlo que hace es recorrer la lista por el número de elementos que tiene y luego se crea un segundo lazo que recorre la lista por todos los elementos que tiene la lista menos uno para que pueda comparar dos elementos a la vez con la subvariable j por eso si fuera el mismo número de elementos llegaría un momento en el que j+1 saldría de la lista y marcaría error. porque si hay 5 elementos solo puedes hacer 4 comparaciones entre pares.
Con un if compara un elemento con el que tiene a la derecha y si es mayor se intercambian.

Complejidad Computacional:
¿Cuál es la complejidad Big O de su solución?
Es n al cuadrado.
¿Por qué tiene esa complejidad? (Justifique en base a los loops utilizados)
Como usé dos loops uno que hace un número de operaciones igual a la longitud de la lista y otro que hace un número de operaciones igual a un elemento menos que el número de elementos en la lista. 
¿Qué pasa con el tiempo de ejecución si la lista tiene 10 elementos vs 100 elementos?
Si mi lista tiene 10 elementos hará 10 operaciones en el primer loop pero en cada operación del primer loop hay 9 operaciones de comparación de elementos. Con 10 números hace 90 operaciones y con 100 hace 9900 operaciones.
