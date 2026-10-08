
import tkinter as tk
from interfaz import InterfazReproductor


def main():
    ventana = tk.Tk()
    InterfazReproductor(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()