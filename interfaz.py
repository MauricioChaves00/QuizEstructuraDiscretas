
import tkinter as tk
from tkinter import messagebox

from lista_circular_doble import ListaCircularDoble


class InterfazReproductor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Reproductor - Lista Circular Doble")
        self.ventana.geometry("850x550")

        self.reproductor = ListaCircularDoble()

        # Título
        tk.Label(
            ventana,
            text="Reproductor Musical",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        # Agregar canciones
        marco_agregar = tk.Frame(ventana)
        marco_agregar.pack(pady=10)

        self.entrada = tk.Entry(
            marco_agregar,
            font=("Arial", 13),
            width=30
        )
        self.entrada.pack(side=tk.LEFT, padx=5)

        tk.Button(
            marco_agregar,
            text="Agregar canción",
            command=self.agregar_cancion
        ).pack(side=tk.LEFT)

        # Canción actual
        self.etiqueta_actual = tk.Label(
            ventana,
            text="No hay canciones",
            font=("Arial", 16, "bold")
        )
        self.etiqueta_actual.pack(pady=15)

        # Controles
        marco_botones = tk.Frame(ventana)
        marco_botones.pack(pady=10)

        tk.Button(
            marco_botones,
            text="◀ Anterior",
            command=self.anterior,
            width=15
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            marco_botones,
            text="Siguiente ▶",
            command=self.siguiente,
            width=15
        ).pack(side=tk.LEFT, padx=10)

        # Área gráfica
        self.canvas = tk.Canvas(
            ventana,
            width=800,
            height=230,
            bg="white"
        )
        self.canvas.pack(pady=15)

        self.actualizar_visualizacion()

    def agregar_cancion(self):
        cancion = self.entrada.get().strip()

        if not cancion:
            messagebox.showwarning(
                "Atención",
                "Ingrese el nombre de una canción."
            )
            return

        self.reproductor.insertar(cancion)
        self.entrada.delete(0, tk.END)
        self.actualizar_visualizacion()

    def siguiente(self):
        self.reproductor.siguiente()
        self.actualizar_visualizacion()

    def anterior(self):
        self.reproductor.anterior()
        self.actualizar_visualizacion()

    def actualizar_visualizacion(self):
        self.canvas.delete("all")

        if self.reproductor.cabeza is None:
            self.etiqueta_actual.config(
                text="No hay canciones"
            )
            self.canvas.create_text(
                400, 110,
                text="Lista vacía",
                font=("Arial", 16)
            )
            return

        self.etiqueta_actual.config(
            text="Canción actual: "
                 + self.reproductor.actual.cancion
        )

        nodo = self.reproductor.cabeza
        nodos = []

        # Recorrer la lista circular
        while True:
            nodos.append(nodo)
            nodo = nodo.siguiente

            if nodo is self.reproductor.cabeza:
                break

        cantidad = len(nodos)
        separacion = 740 / max(cantidad, 1)

        for i, nodo in enumerate(nodos):
            x = 30 + i * separacion
            y = 75

            color = (
                "#90EE90"
                if nodo is self.reproductor.actual
                else "#ADD8E6"
            )

            self.canvas.create_rectangle(
                x, y, x + 100, y + 50,
                fill=color,
                outline="black"
            )

            self.canvas.create_text(
                x + 50,
                y + 25,
                text=nodo.cancion[:12],
                font=("Arial", 10)
            )

            if i < cantidad - 1:
                self.canvas.create_line(
                    x + 100, y + 15,
                    x + separacion, y + 15,
                    arrow=tk.LAST
                )

                self.canvas.create_line(
                    x + separacion, y + 35,
                    x + 100, y + 35,
                    arrow=tk.LAST
                )

        # Representación de circularidad
        self.canvas.create_text(
            400, 185,
            text="Último.siguiente → Primero"
                 "     |     Primero.anterior → Último",
            font=("Arial", 11),
            fill="blue"
        )