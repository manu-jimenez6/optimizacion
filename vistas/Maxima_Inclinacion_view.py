# vistas/maxima_inclinacion_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math
import numpy as np
import sympy as sp

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

from metodos.maxima_inclinacion import (
    maxima_inclinacion
)


class VentanaMaximaInclinacion:

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
            "Método de Máxima Inclinación"
        )

        self.root.geometry(
            "1300x800"
        )

        self.root.minsize(
            1100,
            700
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
            "TCombobox",
            fieldbackground=self.COLOR_ENTRADA,
            background=self.COLOR_ENTRADA,
            foreground=self.COLOR_ENTRADA_TEXTO,
            borderwidth=0,
            relief="flat",
            padding=5
        )

        estilo.map(
            "TCombobox",
            fieldbackground=[
                ("readonly", self.COLOR_ENTRADA)
            ],
            foreground=[
                ("readonly", self.COLOR_ENTRADA_TEXTO)
            ]
        )

        estilo.configure(
            "Treeview",
            background=self.COLOR_PANEL_2,
            foreground=self.COLOR_TEXTO_SECUNDARIO,
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

        estilo.map(
            "Vertical.TScrollbar",
            background=[
                ("active", self.COLOR_HOVER)
            ]
        )

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="MÉTODO DE MÁXIMA INCLINACIÓN",
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
                "Encuentra máximos de funciones de dos variables "
                "utilizando el gradiente"
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
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
        )

        self.entrada_funcion.grid(
            row=0,
            column=1,
            padx=8,
            pady=5
        )

        self.entrada_funcion.insert(
            0,
            "3*x**2 - 120*x + y**2"
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
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
        )

        self.entrada_x0.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_x0.insert(
            0,
            "0"
        )

        tk.Label(
            panel_entrada,
            text="y₀:",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        self.entrada_y0 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=10,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
        )

        self.entrada_y0.grid(
            row=0,
            column=5,
            padx=5
        )

        self.entrada_y0.insert(
            0,
            "1"
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
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
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
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
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
            lambda e:
            self.boton_calcular.config(
                bg=self.COLOR_HOVER
            )
        )

        self.boton_calcular.bind(
            "<Leave>",
            lambda e:
            self.boton_calcular.config(
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
            "y",
            "fx",
            "dfx",
            "dfy",
            "h",
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

            "y": "y",

            "fx": "f(x,y)",

            "dfx": "∂f/∂x",

            "dfy": "∂f/∂y",

            "h": "h",

            "error": "Error"
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=90,
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
            width=500
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
            text="SUPERFICIE Y TRAYECTORIA",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).pack(
            pady=8
        )

        self.figura = Figure(
            figsize=(6, 5),
            dpi=90,
            facecolor=self.COLOR_PANEL
        )

        self.ax = self.figura.add_subplot(
            111,
            projection="3d"
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

    def crear_funcion(
        self,
        expresion
    ):

        expresion = expresion.replace(
            "^",
            "**"
        )

        x, y = sp.symbols(
            "x y"
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

        f = sp.lambdify(
            (x, y),
            expresion_sympy,
            "numpy"
        )

        return (
            f,
            expresion_sympy
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

            y0 = float(
                self.entrada_y0.get()
            )

            tolerancia = float(
                self.entrada_tolerancia.get()
            )

            max_iter = int(
                self.entrada_iteraciones.get()
            )

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

            f, expresion_sympy = self.crear_funcion(
                expresion
            )

            valor_inicial = f(
                x0,
                y0
            )

            if not np.isfinite(valor_inicial):

                raise ValueError(
                    "La función no tiene un valor válido "
                    "en el punto inicial."
                )

            resultado = maxima_inclinacion(

                expresion,

                x0,

                y0,

                tolerancia,

                max_iter

            )

            xr = resultado[
                "x_optimo"
            ]

            yr = resultado[
                "y_optimo"
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
                    f"Máximo: "
                    f"x = {xr:.10f}     |     "
                    f"y = {yr:.10f}     |     "
                    f"f(x,y) = {valor:.10f}     |     "
                    f"Iteraciones: {iteraciones}     |     "
                    f"Error: {error:.10f}"
                ),
                fg=self.COLOR_EXITO
            )

            self.mostrar_tabla(
                resultado["tabla"]
            )

            self.graficar(
                f,
                resultado["trayectoria"],
                xr,
                yr,
                valor
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

                    f"{fila['y']:.8f}",

                    f"{fila['fx']:.8f}",

                    f"{fila['dfx']:.8f}",

                    f"{fila['dfy']:.8f}",

                    f"{fila['h']:.8f}",

                    f"{fila['error']:.8f}"

                )
            )

    def graficar(
        self,
        f,
        trayectoria,
        xr,
        yr,
        zr
    ):

        self.ax.clear()

        self.ax.set_facecolor(
            self.COLOR_PANEL_2
        )

        xs = np.array(
            [
                punto[0]
                for punto in trayectoria
            ]
        )

        ys = np.array(
            [
                punto[1]
                for punto in trayectoria
            ]
        )

        zs = np.array(
            [
                punto[2]
                for punto in trayectoria
            ]
        )

        if len(xs) > 0:

            rango_x = max(
                np.ptp(xs),
                4
            )

            rango_y = max(
                np.ptp(ys),
                4
            )

            margen_x = rango_x * 0.5

            margen_y = rango_y * 0.5

            xmin = xs.min() - margen_x
            xmax = xs.max() + margen_x

            ymin = ys.min() - margen_y
            ymax = ys.max() + margen_y

        else:

            xmin = xr - 5
            xmax = xr + 5

            ymin = yr - 5
            ymax = yr + 5

        cantidad = 40

        valores_x = np.linspace(
            xmin,
            xmax,
            cantidad
        )

        valores_y = np.linspace(
            ymin,
            ymax,
            cantidad
        )

        X, Y = np.meshgrid(
            valores_x,
            valores_y
        )

        try:

            Z = f(
                X,
                Y
            )

            Z = np.array(
                Z,
                dtype=float
            )

            Z[
                ~np.isfinite(Z)
            ] = np.nan

            self.ax.plot_surface(
                X,
                Y,
                Z,
                alpha=0.55,
                color="#E8A0B0"
            )

        except Exception:

            pass

        if len(xs) > 0:

            self.ax.plot(
                xs,
                ys,
                zs,
                linewidth=2,
                marker="o",
                markersize=4,
                color=self.COLOR_BOTON,
                label="Trayectoria"
            )

            self.ax.scatter(
                [xs[0]],
                [ys[0]],
                [zs[0]],
                s=70,
                color=self.COLOR_TEXTO_SECUNDARIO,
                label="Punto inicial"
            )

        self.ax.scatter(
            [xr],
            [yr],
            [zr],
            s=120,
            zorder=10,
            color=self.COLOR_HOVER,
            edgecolors="white",
            linewidths=1,
            label="Máximo"
        )

        self.ax.set_xlabel(
            "x",
            color=self.COLOR_TEXTO
        )

        self.ax.set_ylabel(
            "y",
            color=self.COLOR_TEXTO
        )

        self.ax.set_zlabel(
            "f(x,y)",
            color=self.COLOR_TEXTO
        )

        self.ax.set_title(
            "Método de Máxima Inclinación",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        leyenda = self.ax.legend(
            fontsize=8
        )

        if leyenda:

            leyenda.get_frame().set_facecolor(
                self.COLOR_PANEL
            )

            leyenda.get_frame().set_edgecolor(
                self.COLOR_BOTON
            )

            for texto in leyenda.get_texts():

                texto.set_color(
                    self.COLOR_TEXTO_SECUNDARIO
                )

        self.figura.tight_layout()

        self.canvas.draw()
