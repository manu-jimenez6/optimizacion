# vistas/interpolacion_cuadratica_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.interpolacion_cuadratica import (
    interpolacion_cuadratica
)


class VentanaInterpolacionCuadratica:

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

    TOLERANCIA = 0.001
    MAX_ITERACIONES = 100

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Interpolación Cuadrática"
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

    def crear_estilos(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except tk.TclError:

            pass

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

        estilo.configure(
            "TCombobox",
            fieldbackground=self.COLOR_ENTRADA,
            background=self.COLOR_BOTON,
            foreground=self.COLOR_ENTRADA_TEXTO,
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 10)
        )

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="INTERPOLACIÓN CUADRÁTICA",
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
                "Encuentra máximos o mínimos "
                "aproximando la función mediante una parábola"
            ),
            font=("Segoe UI", 10),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_FONDO
        )

        subtitulo.pack(
            pady=(0, 10)
        )

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

        tk.Label(
            panel_entrada,
            text="Función f(x):",
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
            "x**2 - 4*x + 5"
        )

        tk.Label(
            panel_entrada,
            text="x₁:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.entrada_x1 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_x1.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_x1.insert(
            0,
            "1"
        )

        tk.Label(
            panel_entrada,
            text="x₂:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        self.entrada_x2 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_x2.grid(
            row=0,
            column=5,
            padx=5
        )

        self.entrada_x2.insert(
            0,
            "2"
        )

        tk.Label(
            panel_entrada,
            text="x₃:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        self.entrada_x3 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_x3.grid(
            row=0,
            column=7,
            padx=5
        )

        self.entrada_x3.insert(
            0,
            "3"
        )

        tk.Label(
            panel_entrada,
            text="Buscar:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=10
        )

        self.combo_tipo = ttk.Combobox(
            panel_entrada,
            values=[
                "Mínimo",
                "Máximo"
            ],
            state="readonly",
            width=12
        )

        self.combo_tipo.grid(
            row=1,
            column=1,
            padx=8,
            pady=10,
            sticky="w"
        )

        self.combo_tipo.set(
            "Mínimo"
        )

        tk.Label(
            panel_entrada,
            text="Tolerancia:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=2,
            padx=5
        )

        self.entrada_tolerancia = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_ENTRADA_TEXTO
        )

        self.entrada_tolerancia.grid(
            row=1,
            column=3,
            padx=5
        )

        self.entrada_tolerancia.insert(
            0,
            "0.001"
        )

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
            "100"
        )

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
            column=7,
            padx=10
        )

        # Efecto hover

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

        columnas = (
            "i",
            "x1",
            "x2",
            "x3",
            "fx1",
            "fx2",
            "fx3",
            "xr",
            "fxr",
            "error"
        )

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings"
        )

        nombres = {

            "i": "i",

            "x1": "x₁",

            "x2": "x₂",

            "x3": "x₃",

            "fx1": "f(x₁)",

            "fx2": "f(x₂)",

            "fx3": "f(x₃)",

            "xr": "xᵣ",

            "fxr": "f(xᵣ)",

            "error": "Error"
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=85,
                anchor="center"
            )

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
            text="FUNCIÓN Y ÓPTIMO",
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

        # Configuración inicial de la gráfica

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        self.ax.set_title(
            "Interpolación cuadrática",
            color=self.COLOR_TEXTO
        )

        self.ax.set_xlabel(
            "x",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_ylabel(
            "f(x)",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.grid(
            True,
            alpha=0.25
        )

        self.figura.tight_layout()

        self.canvas.draw()
        
    def crear_funcion(
        self,
        expresion
    ):

        expresion = expresion.replace(
            "^",
            "**"
        )

        def f(x):

            entorno = {

                "x": x,

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

    def calcular(self):

        try:

            expresion = (
                self.entrada_funcion
                .get()
                .strip()
            )

            x1 = float(
                self.entrada_x1.get()
            )

            x2 = float(
                self.entrada_x2.get()
            )

            x3 = float(
                self.entrada_x3.get()
            )

            tolerancia = float(
                self.entrada_tolerancia.get()
            )

            max_iter = int(
                self.entrada_iteraciones.get()
            )

            tipo = self.combo_tipo.get()

            if not expresion:

                raise ValueError(
                    "Debe ingresar una función."
                )

            if tolerancia <= 0:

                raise ValueError(
                    "La tolerancia debe ser mayor que 0."
                )

            if max_iter <= 0:

                raise ValueError(
                    "El número de iteraciones debe ser mayor que 0."
                )

            if (
                x1 == x2
                or x1 == x3
                or x2 == x3
            ):

                raise ValueError(
                    "Los tres valores iniciales deben ser diferentes."
                )

            if not (
                x1 < x2 < x3
                or x3 < x2 < x1
            ):

                valores = sorted(
                    [x1, x2, x3]
                )

                x1 = valores[0]
                x2 = valores[1]
                x3 = valores[2]

            f = self.crear_funcion(
                expresion
            )

            # Validar función

            f(x1)
            f(x2)
            f(x3)

            resultado = interpolacion_cuadratica(

                f,

                x1,
                x2,
                x3,

                tipo,

                tolerancia,

                max_iter
            )

            xr = resultado[
                "x_optimo"
            ]

            valor = resultado[
                "valor"
            ]

            iteraciones = resultado[
                "iteraciones"
            ]

            error = resultado[
                "error"
            ]

            self.label_resultado.config(
                text=(
                    f"{tipo}: "
                    f"x = {xr:.10f}     |     "
                    f"f(x) = {valor:.10f}     |     "
                    f"Iteraciones: {iteraciones}     |     "
                    f"Error: {error:.10f}"
                )
            )


            self.mostrar_tabla(
                resultado["tabla"]
            )

            self.graficar(
                f,
                x1,
                x2,
                x3,
                xr,
                valor,
                tipo
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except ZeroDivisionError as error:

            messagebox.showerror(
                "Error matemático",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo procesar la función.\n\n"
                f"{error}"
            )

    def mostrar_tabla(
        self,
        datos
    ):

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        for fila in datos:

            self.tabla.insert(
                "",
                "end",
                values=(

                    fila["iteracion"],

                    f"{fila['x1']:.8f}",

                    f"{fila['x2']:.8f}",

                    f"{fila['x3']:.8f}",

                    f"{fila['fx1']:.8f}",

                    f"{fila['fx2']:.8f}",

                    f"{fila['fx3']:.8f}",

                    f"{fila['xr']:.8f}",

                    f"{fila['fxr']:.8f}",

                    f"{fila['error']:.8f}"
                )
            )

    def graficar(
        self,
        f,
        x1,
        x2,
        x3,
        xr,
        yr,
        tipo
    ):

        self.ax.clear()

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        minimo = min(
            x1,
            x2,
            x3,
            xr
        )

        maximo = max(
            x1,
            x2,
            x3,
            xr
        )

        distancia = max(
            maximo - minimo,
            2
        )

        inicio = (
            minimo - distancia * 0.5
        )

        final = (
            maximo + distancia * 0.5
        )
        
        valores_x = []
        valores_y = []

        cantidad = 400

        paso = (
            final - inicio
        ) / cantidad

        for i in range(
            cantidad + 1
        ):

            x = (
                inicio
                + i * paso
            )

            try:

                y = f(x)

                if (
                    isinstance(y, (int, float))
                    and math.isfinite(y)
                ):

                    valores_x.append(
                        x
                    )

                    valores_y.append(
                        y
                    )

            except Exception:

                pass

        if valores_x:

            self.ax.plot(
                valores_x,
                valores_y,
                linewidth=2,
                color="#D47A8D",
                label="f(x)"
            )
            
        self.ax.scatter(
            [x1, x2, x3],
            [f(x1), f(x2), f(x3)],
            s=45,
            color="#E8A0B0",
            label="Puntos iniciales"
        )

        self.ax.scatter(
            [xr],
            [yr],
            s=100,
            zorder=5,
            color="#8B3A52",
            label=(
                f"{tipo}: "
                f"({xr:.5f}, {yr:.5f})"
            )
        )

        self.ax.axhline(
            0,
            linewidth=1,
            color="#B34B6E"
        )

        self.ax.set_xlabel(
            "x",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_ylabel(
            "f(x)",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax.set_title(
            "Interpolación cuadrática",
            color=self.COLOR_TEXTO
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
            alpha=0.3
        )

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
                
        self.figura.tight_layout()

        self.canvas.draw()
