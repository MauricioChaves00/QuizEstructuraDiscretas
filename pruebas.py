
from lista_circular_doble import ListaCircularDoble


def probar_lista_vacia():
    lista = ListaCircularDoble()

    assert lista.cabeza is None
    assert lista.actual is None
    assert lista.siguiente() is None
    assert lista.anterior() is None

    print("OK - Lista vacía")


def probar_una_cancion():
    lista = ListaCircularDoble()
    lista.insertar("Believer")

    assert lista.cabeza is lista.actual
    assert lista.cabeza.siguiente is lista.cabeza
    assert lista.cabeza.anterior is lista.cabeza

    assert lista.siguiente() == "Believer"
    assert lista.anterior() == "Believer"

    print("OK - Una canción")


def probar_varias_canciones():
    lista = ListaCircularDoble()

    lista.insertar("Believer")
    lista.insertar("Thunder")
    lista.insertar("Demons")

    assert lista.cabeza.cancion == "Believer"
    assert lista.cabeza.siguiente.cancion == "Thunder"
    assert lista.cabeza.anterior.cancion == "Demons"

    print("OK - Inserción de varias canciones")


def probar_circularidad():
    lista = ListaCircularDoble()

    lista.insertar("Believer")
    lista.insertar("Thunder")
    lista.insertar("Demons")

    primero = lista.cabeza
    ultimo = primero.anterior

    assert ultimo.siguiente is primero
    assert primero.anterior is ultimo

    # Comprobar enlaces en ambas direcciones
    nodo = primero

    for _ in range(3):
        assert nodo.siguiente.anterior is nodo
        assert nodo.anterior.siguiente is nodo
        nodo = nodo.siguiente

    assert nodo is primero

    print("OK - Circularidad doble")


def probar_navegacion():
    lista = ListaCircularDoble()

    lista.insertar("Believer")
    lista.insertar("Thunder")
    lista.insertar("Demons")

    assert lista.siguiente() == "Thunder"
    assert lista.siguiente() == "Demons"
    assert lista.siguiente() == "Believer"

    assert lista.anterior() == "Demons"
    assert lista.anterior() == "Thunder"
    assert lista.anterior() == "Believer"

    print("OK - Navegación hacia adelante y atrás")


def ejecutar_pruebas():
    probar_lista_vacia()
    probar_una_cancion()
    probar_varias_canciones()
    probar_circularidad()
    probar_navegacion()

    print("\nTodas las pruebas fueron superadas.")


if __name__ == "__main__":
    ejecutar_pruebas()