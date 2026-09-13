# vistas/menu_principal.py

import tkinter as tk

from vistas.biseccion_view import VentanaBiseccion
from vistas.falsa_posicion_view import VentanaFalsaPosicion
from vistas.Newton_Raphson_view import VentanaNewtonRaphson
from vistas.Newton_view import VentanaNewton
from vistas.Interpolación_Cuadrática_view import VentanaInterpolacionCuadratica
from vistas.Búsqueda_Aleatoria_view import VentanaBusquedaAleatoria
from vistas.Razon_Dorada_view import VentanaRazonDorada
from vistas.Maxima_Inclinacion_view import VentanaMaximaInclinacion


class MenuPrincipal:

    COLOR_FONDO = "#FFE4E1"
    COLOR_PANEL = "#FFD1DC"
    COLOR_PANEL_2 = "#FFF0F0"

    COLOR_BOTON = "#E88B9E"
    COLOR_HOVER = "#D47A8D"

    COLOR_TEXTO = "#B34B6E"
    COLOR_TEXTO_SECUNDARIO = "#8B3A52"

    COLOR_EXITO = "#B34B6E"
    COLOR_ERROR = "#C94C70"

    COLOR_ENTRADA = "#FFF5F5"
    COLOR_ENTRADA_TEXTO = "#8B3A52"

    def __init__(self, root):

        self.root = root

        self.root.title("Métodos Numéricos")
        self.root.state("zoomed")
        self.root.configure(bg=self.COLOR_FONDO)

        titulo = tk.Label(
            root,
            text="MÉTODOS NUMÉRICOS",
            font=("Segoe UI", 28, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_FONDO
        )

        titulo.pack(pady=(40, 10))

        subtitulo = tk.Label(
            root,
            text="Seleccione el método que desea utilizar",
            font=("Segoe UI", 12),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_FONDO
        )

        subtitulo.pack(pady=(0, 30))

        panel = tk.Frame(
            root,
            bg=self.COLOR_PANEL,
            padx=40,
            pady=40,
            relief="flat",
            bd=0
        )

        panel.pack(expand=True)

        botones = [

            ("Bisección", self.abrir_biseccion),

            ("Falsa Posición", self.abrir_falsa_posicion),

            ("Newton-Raphson", self.abrir_newton_raphson),

            ("Método de Newton", self.abrir_newton),

            ("Interpolación Cuadrática", self.abrir_interpolacion),

            ("Búsqueda Aleatoria", self.abrir_busqueda_aleatoria),

            ("Razón Dorada", self.abrir_razon_dorada),

            ("Máxima Inclinación", self.maxima_inclinacion)
        ]

        fila = 0
        columna = 0

        for texto, comando in botones:

            boton = self.crear_boton(
                panel,
                texto,
                comando
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=15,
                pady=15
            )

            columna += 1

            if columna > 1:
                columna = 0
                fila += 1

        btn_salir = tk.Button(
            root,
            text="Salir",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_ERROR,
            fg="white",
            activebackground="#A83D5D",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=15,
            height=2,
            cursor="hand2",
            command=root.destroy
        )

        btn_salir.pack(pady=25)

        btn_salir.bind(
            "<Enter>",
            lambda e: btn_salir.config(
                bg="#A83D5D"
            )
        )

        btn_salir.bind(
            "<Leave>",
            lambda e: btn_salir.config(
                bg=self.COLOR_ERROR
            )
        )

    def crear_boton(self, contenedor, texto, comando):

        boton = tk.Button(
            contenedor,
            text=texto,
            font=("Segoe UI", 12, "bold"),
            bg=self.COLOR_BOTON,
            fg="white",
            activebackground=self.COLOR_HOVER,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=25,
            height=2,
            cursor="hand2",
            command=comando
        )

        boton.bind(
            "<Enter>",
            lambda e: boton.config(
                bg=self.COLOR_HOVER
            )
        )

        boton.bind(
            "<Leave>",
            lambda e: boton.config(
                bg=self.COLOR_BOTON
            )
        )

        return boton

    def abrir_biseccion(self):

        ventana = tk.Toplevel(self.root)
        VentanaBiseccion(ventana)

    def abrir_falsa_posicion(self):

        ventana = tk.Toplevel(self.root)
        VentanaFalsaPosicion(ventana)

    def abrir_newton_raphson(self):

        ventana = tk.Toplevel(self.root)
        VentanaNewtonRaphson(ventana)

    def abrir_newton(self):

        ventana = tk.Toplevel(self.root)
        VentanaNewton(ventana)

    def abrir_interpolacion(self):

        ventana = tk.Toplevel(self.root)
        VentanaInterpolacionCuadratica(ventana)

    def abrir_busqueda_aleatoria(self):

        ventana = tk.Toplevel(self.root)
        VentanaBusquedaAleatoria(ventana)

    def abrir_razon_dorada(self):

        ventana = tk.Toplevel(self.root)
        VentanaRazonDorada(ventana)

    def maxima_inclinacion(self):

        ventana = tk.Toplevel(self.root)
        VentanaMaximaInclinacion(ventana)
