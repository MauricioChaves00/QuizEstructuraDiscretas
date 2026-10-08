# Quiz 1 — Reproductor Musical

**Caso seleccionado:** Caso 2 — Reproductor en modo "repetir todo".

**Estructura utilizada:** Lista Circular Doble.

### Justificación

Se seleccionó una Lista Circular Doble porque permite representar adecuadamente el funcionamiento de un reproductor musical en modo "repetir todo", donde el usuario puede avanzar y retroceder entre canciones de manera continua.

Esta estructura utiliza nodos que almacenan una canción y dos referencias: una al nodo siguiente y otra al anterior. Además, al ser circular, el último nodo se conecta con el primero y viceversa, permitiendo que la reproducción continúe sin interrupciones al llegar a los extremos.

En comparación con una Lista Simple o Circular Simple, la Lista Circular Doble permite retroceder directamente entre canciones. Una Lista Doble convencional también permite avanzar y retroceder, pero no mantiene la conexión circular entre los extremos. Las Listas de Listas y Salteadas están orientadas a otras necesidades, como la agrupación de elementos y la búsqueda eficiente.

Por estas razones, la Lista Circular Doble es la opción más adecuada para el caso seleccionado, ya que permite realizar las operaciones necesarias de forma sencilla, sin recorrer toda la lista para cambiar de canción.
