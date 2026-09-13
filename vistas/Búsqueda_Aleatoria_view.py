# vistas/busqueda_aleatoria_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.busqueda_aleatoria import (
    busqueda_aleatoria
)


class VentanaBusquedaAleatoria:

    # ==========================================================
    # COLORES - ESTILO ROSA PASTEL
    # ==========================================================

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

    # ==========================================================
    # CONFIGURACIÓN
    # ==========================================================

    MAX_ITERACIONES = 10000

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Búsqueda Aleatoria"
        )

        self.root.geometry(
            "1200x750"
        )

        self.root.minsize(
            1000,
            650
        )

        self.root.configure(
            bg=self.COLOR_FONDO
        )

        self.crear_estilos()

        self.crear_interfaz()

    # ==========================================================
    # ESTILOS
    # ==========================================================

    def crear_estilos(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except tk.TclError:

            pass

        # ------------------------------------------------------
        # TABLA
        # ------------------------------------------------------

        estilo.configure(
            "Treeview",
            background=self.COLOR_PANEL_2,
            foreground=self.COLOR_TEXTO,
            fieldbackground=self.COLOR_PANEL_2,
            rowheight=27,
            borderwidth=0,
            font=("Segoe UI", 9)
        )

        estilo.configure(
            "Treeview.Heading",
            background="#E8A0B0",
            foreground="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat"
        )

        estilo.map(
            "Treeview",
            background=[
                (
                    "selected",
                    self.COLOR_BOTON
                )
            ],
            foreground=[
                (
                    "selected",
                    "white"
                )
            ]
        )

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def crear_interfaz(self):

        # ======================================================
        # TÍTULO
        # ======================================================

        titulo = tk.Label(
            self.root,
            text="BÚSQUEDA ALEATORIA",
            font=("Segoe UI", 22, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_FONDO
        )

        titulo.pack(
            pady=(15, 2)
        )

        subtitulo = tk.Label(
            self.root,
            text=(
                "Encuentra el máximo de una función "
                "evaluando puntos seleccionados aleatoriamente"
            ),
            font=("Segoe UI", 10),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_FONDO
        )

        subtitulo.pack(
            pady=(0, 10)
        )

        # ======================================================
        # PANEL DE ENTRADA
        # ======================================================

        panel_entrada = tk.Frame(
            self.root,
            bg=self.COLOR_PANEL,
            padx=20,
            pady=12
        )

        panel_entrada.pack(
            fill="x",
            padx=20,
            pady=(0, 8)
        )

        # ======================================================
        # FUNCIÓN
        # ======================================================

        tk.Label(
            panel_entrada,
            text="Función f(x,y):",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=5
        )

        self.entrada_funcion = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=32,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_funcion.grid(
            row=0,
            column=1,
            padx=8,
            pady=5
        )

        self.entrada_funcion.insert(
            0,
            "y - x - 2*x**2 - 2*x*y - y**2"
        )

        # ======================================================
        # X INFERIOR
        # ======================================================

        tk.Label(
            panel_entrada,
            text="xₗ:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.entrada_xl = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=8,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_xl.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_xl.insert(
            0,
            "-2"
        )

        # ======================================================
        # X SUPERIOR
        # ======================================================

        tk.Label(
            panel_entrada,
            text="xᵤ:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        self.entrada_xu = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=8,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_xu.grid(
            row=0,
            column=5,
            padx=5
        )

        self.entrada_xu.insert(
            0,
            "2"
        )

        # ======================================================
        # Y INFERIOR
        # ======================================================

        tk.Label(
            panel_entrada,
            text="yₗ:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=10
        )

        self.entrada_yl = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=8,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_yl.grid(
            row=1,
            column=1,
            padx=8,
            pady=10,
            sticky="w"
        )

        self.entrada_yl.insert(
            0,
            "1"
        )

        # ======================================================
        # Y SUPERIOR
        # ======================================================

        tk.Label(
            panel_entrada,
            text="yᵤ:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=2,
            padx=5
        )

        self.entrada_yu = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=8,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_yu.grid(
            row=1,
            column=3,
            padx=5
        )

        self.entrada_yu.insert(
            0,
            "3"
        )

        # ======================================================
        # ITERACIONES
        # ======================================================

        tk.Label(
            panel_entrada,
            text="Máx. iteraciones:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=4,
            padx=5
        )

        self.entrada_iteraciones = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_iteraciones.grid(
            row=1,
            column=5,
            padx=5
        )

        self.entrada_iteraciones.insert(
            0,
            "10000"
        )

        # ======================================================
        # BOTÓN
        # ======================================================

        self.boton_calcular = tk.Button(
            panel_entrada,
            text="CALCULAR",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BOTON,
            fg="white",
            activebackground=self.COLOR_HOVER,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=13,
            height=2,
            cursor="hand2",
            command=self.calcular
        )

        self.boton_calcular.grid(
            row=1,
            column=6,
            padx=10
        )

        # ------------------------------------------------------
        # EFECTO HOVER
        # ------------------------------------------------------

        self.boton_calcular.bind(
            "<Enter>",
            lambda e: self.boton_calcular.config(
                bg=self.COLOR_HOVER
            )
        )

        self.boton_calcular.bind(
            "<Leave>",
            lambda e: self.boton_calcular.config(
                bg=self.COLOR_BOTON
            )
        )

        # ======================================================
        # RESULTADO
        # ======================================================

        self.label_resultado = tk.Label(
            self.root,
            text="Resultado: --",
            font=("Segoe UI", 12, "bold"),
            fg=self.COLOR_EXITO,
            bg=self.COLOR_FONDO
        )

        self.label_resultado.pack(
            pady=8
        )

        # ======================================================
        # ZONA INFERIOR
        # ======================================================

        panel_inferior = tk.Frame(
            self.root,
            bg=self.COLOR_FONDO
        )

        panel_inferior.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        # ======================================================
        # TABLA
        # ======================================================

        panel_tabla = tk.Frame(
            panel_inferior,
            bg=self.COLOR_PANEL
        )

        panel_tabla.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            panel_tabla,
            text="TABLA DE ITERACIONES",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).pack(
            pady=8
        )

        frame_tree = tk.Frame(
            panel_tabla,
            bg=self.COLOR_PANEL
        )

        frame_tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8)
        )

        # ======================================================
        # COLUMNAS
        # ======================================================

        columnas = (
            "iteracion",
            "x",
            "y",
            "fx"
        )

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings"
        )

        nombres = {

            "iteracion": "Iteraciones",

            "x": "x",

            "y": "y",

            "fx": "f(x,y)"

        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=110,
                anchor="center"
            )

        # ======================================================
        # SCROLLBAR
        # ======================================================

        scrollbar = ttk.Scrollbar(
            frame_tree,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ======================================================
        # GRÁFICA
        # ======================================================

        panel_grafica = tk.Frame(
            panel_inferior,
            bg=self.COLOR_PANEL,
            width=400
        )

        panel_grafica.pack(
            side="right",
            fill="both",
            padx=(8, 0)
        )

        panel_grafica.pack_propagate(
            False
        )

        tk.Label(
            panel_grafica,
            text="FUNCIÓN Y MÁXIMO",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).pack(
            pady=8
        )

        self.figura = Figure(
            figsize=(5, 5),
            dpi=90,
            facecolor=self.COLOR_PANEL
        )

        self.ax = self.figura.add_subplot(
            111
        )

        self.canvas = FigureCanvasTkAgg(
            self.figura,
            master=panel_grafica
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ======================================================
        # CONFIGURACIÓN INICIAL DE LA GRÁFICA
        # ======================================================

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        self.ax.set_title(
            "Búsqueda aleatoria",
            color=self.COLOR_TEXTO
        )

        self.ax.set_xlabel(
            "x",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_ylabel(
            "y",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        for borde in self.ax.spines.values():

            borde.set_color(
                "#E8A0B0"
            )

        self.ax.grid(
            True,
            alpha=0.25
        )

        self.figura.tight_layout()

        self.canvas.draw()

    # ==========================================================
    # CREAR FUNCIÓN
    # ==========================================================

    def crear_funcion(
        self,
        expresion
    ):

        expresion = expresion.replace(
            "^",
            "**"
        )

        def f(x, y):

            entorno = {

                "x": x,

                "y": y,

                "sin": math.sin,

                "cos": math.cos,

                "tan": math.tan,

                "asin": math.asin,

                "acos": math.acos,

                "atan": math.atan,

                "sqrt": math.sqrt,

                "exp": math.exp,

                "log": math.log,

                "ln": math.log,

                "log10": math.log10,

                "pi": math.pi,

                "e": math.e,

                "abs": abs
            }

            return eval(
                expresion,
                {"__builtins__": {}},
                entorno
            )

        return f

    # ==========================================================
    # CALCULAR
    # ==========================================================

    def calcular(self):

        try:

            # ==================================================
            # DATOS
            # ==================================================

            expresion = (
                self.entrada_funcion
                .get()
                .strip()
            )

            xl = float(
                self.entrada_xl.get()
            )

            xu = float(
                self.entrada_xu.get()
            )

            yl = float(
                self.entrada_yl.get()
            )

            yu = float(
                self.entrada_yu.get()
            )

            max_iter = int(
                self.entrada_iteraciones.get()
            )

            # ==================================================
            # VALIDACIONES
            # ==================================================

            if not expresion:

                raise ValueError(
                    "Debe ingresar una función."
                )

            if xl >= xu:

                raise ValueError(
                    "xₗ debe ser menor que xᵤ."
                )

            if yl >= yu:

                raise ValueError(
                    "yₗ debe ser menor que yᵤ."
                )

            if max_iter <= 0:

                raise ValueError(
                    "El número de iteraciones debe ser mayor que 0."
                )

            # ==================================================
            # FUNCIÓN
            # ==================================================

            f = self.crear_funcion(
                expresion
            )

            # Validar función

            f(xl, yl)

            f(xu, yu)

            # ==================================================
            # EJECUTAR MÉTODO
            # ==================================================

            resultado = busqueda_aleatoria(

                f,

                xl,

                xu,

                yl,

                yu,

                max_iter

            )

            # ==================================================
            # RESULTADOS
            # ==================================================

            x = resultado[
                "x_optimo"
            ]

            y = resultado[
                "y_optimo"
            ]

            valor = resultado[
                "valor"
            ]

            iteraciones = resultado[
                "iteraciones"
            ]

            # ==================================================
            # MOSTRAR RESULTADO
            # ==================================================

            self.label_resultado.config(
                text=(
                    f"Máximo: "
                    f"x = {x:.8f}     |     "
                    f"y = {y:.8f}     |     "
                    f"f(x,y) = {valor:.8f}     |     "
                    f"Iteraciones: {iteraciones}"
                )
            )

            # ==================================================
            # TABLA
            # ==================================================

            self.mostrar_tabla(
                resultado["tabla"]
            )

            # ==================================================
            # GRÁFICA
            # ==================================================

            self.graficar(
                f,
                xl,
                xu,
                yl,
                yu,
                x,
                y,
                valor
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo procesar la función.\n\n"
                f"{error}"
            )

    # ==========================================================
    # MOSTRAR TABLA
    # ==========================================================

    def mostrar_tabla(
        self,
        datos
    ):

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # Mostrar todos los puntos si son pocos.
        # Si son demasiados, mostrar uno cada 1000
        # y siempre la última iteración.

        cantidad = len(datos)

        if cantidad <= 1000:

            datos_mostrar = datos

        else:

            datos_mostrar = [

                fila

                for fila in datos

                if fila["iteracion"] % 1000 == 0

            ]

            # Agregar siempre la última iteración

            if datos[-1] not in datos_mostrar:

                datos_mostrar.append(
                    datos[-1]
                )

        for fila in datos_mostrar:

            self.tabla.insert(
                "",
                "end",
                values=(

                    fila["iteracion"],

                    f"{fila['x']:.8f}",

                    f"{fila['y']:.8f}",

                    f"{fila['fx']:.8f}"

                )
            )

    # ==========================================================
    # GRÁFICA
    # ==========================================================

    def graficar(
        self,
        f,
        xl,
        xu,
        yl,
        yu,
        x_optimo,
        y_optimo,
        valor_optimo
    ):

        self.ax.clear()

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        # ======================================================
        # CREAR MALLA
        # ======================================================

        cantidad = 80

        valores_x = [

            xl + (xu - xl) * i / (cantidad - 1)

            for i in range(cantidad)

        ]

        valores_y = [

            yl + (yu - yl) * i / (cantidad - 1)

            for i in range(cantidad)

        ]

        matriz_z = []

        for y in valores_y:

            fila = []

            for x in valores_x:

                try:

                    z = f(x, y)

                    if math.isfinite(z):

                        fila.append(
                            z
                        )

                    else:

                        fila.append(
                            float("nan")
                        )

                except Exception:

                    fila.append(
                        float("nan")
                    )

            matriz_z.append(
                fila
            )

        # ======================================================
        # CONTORNOS
        # ======================================================

        self.ax.contourf(
            valores_x,
            valores_y,
            matriz_z,
            levels=20,
            alpha=0.85
        )

        self.ax.contour(
            valores_x,
            valores_y,
            matriz_z,
            levels=10,
            colors="#B34B6E",
            linewidths=0.8
        )

        # ======================================================
        # MÁXIMO
        # ======================================================

        self.ax.scatter(
            [x_optimo],
            [y_optimo],
            s=120,
            zorder=5,
            color="#8B3A52",
            label=(
                f"Máximo: "
                f"({x_optimo:.4f}, "
                f"{y_optimo:.4f})"
            )
        )

        # ======================================================
        # CONFIGURACIÓN
        # ======================================================

        self.ax.set_xlabel(
            "x",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_ylabel(
            "y",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_title(
            "Búsqueda aleatoria",
            color=self.COLOR_TEXTO
        )

        self.ax.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        # ======================================================
        # BORDES
        # ======================================================

        for borde in self.ax.spines.values():

            borde.set_color(
                "#E8A0B0"
            )

        # ======================================================
        # CUADRÍCULA
        # ======================================================

        self.ax.grid(
            True,
            alpha=0.2
        )

        # ======================================================
        # LEYENDA
        # ======================================================

        leyenda = self.ax.legend(
            fontsize=8
        )

        if leyenda:

            leyenda.get_frame().set_facecolor(
                self.COLOR_ENTRADA
            )

            leyenda.get_frame().set_edgecolor(
                "#E8A0B0"
            )

            for texto in leyenda.get_texts():

                texto.set_color(
                    self.COLOR_TEXTO_SECUNDARIO
                )

        # ======================================================
        # ACTUALIZAR
        # ======================================================

        self.figura.tight_layout()

        self.canvas.draw()