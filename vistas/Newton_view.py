# vistas/newton_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math
import sympy as sp

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.Newton import (
    newton
)


class VentanaNewton:

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

        self.root.title(
            "Método de Newton"
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
                ("selected", self.COLOR_BOTON)
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        estilo.map(
            "Treeview.Heading",
            background=[
                ("active", self.COLOR_HOVER)
            ]
        )

        estilo.configure(
            "Vertical.TScrollbar",
            background=self.COLOR_BOTON,
            troughcolor=self.COLOR_PANEL_2,
            bordercolor=self.COLOR_PANEL,
            arrowcolor="white"
        )

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="MÉTODO DE NEWTON",
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
                "Encuentra máximos o mínimos utilizando "
                "la primera y segunda derivada"
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
            insertbackground=self.COLOR_TEXTO
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
            text="x₀:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.entrada_x0 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=10,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_TEXTO
        )

        self.entrada_x0.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_x0.insert(
            0,
            "1"
        )

        tk.Label(
            panel_entrada,
            text="Buscar:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=4,
            padx=5
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
            row=0,
            column=5,
            padx=5
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
            column=0,
            padx=8,
            pady=10
        )

        self.entrada_tolerancia = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=10,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_TEXTO
        )

        self.entrada_tolerancia.grid(
            row=1,
            column=1,
            padx=8,
            pady=10,
            sticky="w"
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
            column=2,
            padx=5
        )

        self.entrada_iteraciones = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=10,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat",
            insertbackground=self.COLOR_TEXTO
        )

        self.entrada_iteraciones.grid(
            row=1,
            column=3,
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
            column=5,
            padx=10
        )

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
            "x",
            "fx",
            "dfx",
            "d2fx",
            "error"
        )

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings"
        )

        nombres = {

            "i": "i",

            "x": "x",

            "fx": "f(x)",

            "dfx": "f'(x)",

            "d2fx": "f''(x)",

            "error": "Error"
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=100,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            frame_tree,
            orient="vertical",
            command=self.tabla.yview,
            style="Vertical.TScrollbar"
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

    def crear_funciones(
        self,
        expresion
    ):

        expresion = expresion.replace(
            "^",
            "**"
        )

        x = sp.symbols(
            "x"
        )

        try:

            expresion_sympy = sp.sympify(
                expresion
            )

        except Exception as error:

            raise ValueError(
                "La función ingresada no es válida.\n\n"
                f"{error}"
            )

        primera = sp.diff(
            expresion_sympy,
            x
        )

        segunda = sp.diff(
            primera,
            x
        )


        f = sp.lambdify(
            x,
            expresion_sympy,
            "math"
        )

        df = sp.lambdify(
            x,
            primera,
            "math"
        )

        d2f = sp.lambdify(
            x,
            segunda,
            "math"
        )

        return (
            f,
            df,
            d2f,
            str(primera),
            str(segunda)
        )

    def calcular(self):

        try:

            expresion = (
                self.entrada_funcion
                .get()
                .strip()
            )

            x0 = float(
                self.entrada_x0.get()
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

            (
                f,
                df,
                d2f,
                expresion_df,
                expresion_d2f
            ) = self.crear_funciones(
                expresion
            )

            f(x0)

            df(x0)

            d2f(x0)

            resultado = newton(

                f,

                df,

                d2f,

                x0,

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

            tipo_encontrado = resultado[
                "tipo_encontrado"
            ]


            self.label_resultado.config(
                text=(
                    f"{tipo_encontrado}: "
                    f"x = {xr:.10f}     |     "
                    f"f(x) = {valor:.10f}     |     "
                    f"Iteraciones: {iteraciones}     |     "
                    f"Error: {error:.10f}"
                ),
                fg=self.COLOR_EXITO
            )

            if (
                tipo_encontrado != tipo
                and tipo_encontrado != "No determinado"
            ):

                messagebox.showwarning(
                    "Tipo de óptimo",
                    (
                        f"Se solicitó buscar un {tipo.lower()}, "
                        f"pero el punto encontrado corresponde "
                        f"a un {tipo_encontrado.lower()}.\n\n"
                        "Pruebe con otro valor inicial x₀."
                    )
                )

            self.mostrar_tabla(
                resultado["tabla"]
            )

            self.graficar(
                f,
                x0,
                xr,
                valor,
                tipo_encontrado
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
                (
                    "No se pudo procesar la función.\n\n"
                    f"{error}"
                )
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

                    f"{fila['x']:.8f}",

                    f"{fila['fx']:.8f}",

                    f"{fila['dfx']:.8f}",

                    f"{fila['d2fx']:.8f}",

                    f"{fila['error']:.8f}"

                )
            )

    def graficar(
        self,
        f,
        x0,
        xr,
        yr,
        tipo
    ):

        self.ax.clear()

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        distancia = max(
            abs(xr - x0),
            2
        )

        inicio = (
            min(x0, xr)
            - distancia * 0.8
        )

        final = (
            max(x0, xr)
            + distancia * 0.8
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
                color=self.COLOR_BOTON,
                linewidth=2,
                label="f(x)"
            )

        try:

            y0 = f(x0)

            self.ax.scatter(
                [x0],
                [y0],
                s=55,
                color="#E8A0B0",
                label=(
                    f"Inicial: "
                    f"({x0:.5f}, {y0:.5f})"
                )
            )

        except Exception:

            pass

        self.ax.scatter(
            [xr],
            [yr],
            s=100,
            color=self.COLOR_TEXTO,
            edgecolors="white",
            linewidths=1.5,
            zorder=5,
            label=(
                f"{tipo}: "
                f"({xr:.5f}, {yr:.5f})"
            )
        )

        self.ax.axhline(
            0,
            color="#D47A8D",
            linewidth=1
        )

        self.ax.axvline(
            0,
            color="#D47A8D",
            linewidth=1,
            alpha=0.5
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
            "Método de Newton",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax.grid(
            True,
            alpha=0.25,
            color="#D47A8D"
        )

        self.ax.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        for spine in self.ax.spines.values():

            spine.set_color(
                "#E8A0B0"
            )

        leyenda = self.ax.legend(
            fontsize=8
        )

        leyenda.get_frame().set_facecolor(
            self.COLOR_PANEL
        )

        leyenda.get_frame().set_edgecolor(
            "#E8A0B0"
        )

        self.figura.tight_layout()

        self.canvas.draw()
