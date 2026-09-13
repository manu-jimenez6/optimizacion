# vistas/razon_dorada_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.razon_dorada import (
    razon_dorada
)


class VentanaRazonDorada:

    # ==========================================================
    # COLORES
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
    
    COLOR_GRAFICA = "#E88B9E"
    COLOR_LINEA_EJE = "#D47A8D"

    # ==========================================================
    # CONFIGURACIÓN
    # ==========================================================

    TOLERANCIA = 0.01
    MAX_ITERACIONES = 100

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Razón Dorada"
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
            background=self.COLOR_BOTON,
            foreground=self.COLOR_TEXTO,
            font=("Segoe UI", 9, "bold"),
            relief="flat"
        )

        estilo.map(
            "Treeview",
            background=[
                ("selected", self.COLOR_BOTON)
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
            text="RAZÓN DORADA",
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
                "Encuentra mínimos o máximos de una función "
                "mediante el método de la razón dorada"
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
            "2*sin(x) - x**2/10"
        )

        # ======================================================
        # LÍMITE INFERIOR
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
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat"
        )

        self.entrada_xl.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_xl.insert(
            0,
            "0"
        )

        # ======================================================
        # LÍMITE SUPERIOR
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
            width=9,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief="flat"
        )

        self.entrada_xu.grid(
            row=0,
            column=5,
            padx=5
        )

        self.entrada_xu.insert(
            0,
            "4"
        )

        # ======================================================
        # BUSCAR
        # ======================================================

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
                "Máximo",
                "Mínimo",
                "Ambos"
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
            "Máximo"
        )

        # ======================================================
        # TOLERANCIA
        # ======================================================

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
            relief="flat"
        )

        self.entrada_tolerancia.grid(
            row=1,
            column=3,
            padx=5
        )

        self.entrada_tolerancia.insert(
            0,
            "0.01"
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
            relief="flat"
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
            "tipo",
            "i",
            "xl",
            "xu",
            "x1",
            "x2",
            "fx1",
            "fx2",
            "error"
        )

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings"
        )

        nombres = {

            "tipo": "Tipo",

            "i": "i",

            "xl": "xₗ",

            "xu": "xᵤ",

            "x1": "x₁",

            "x2": "x₂",

            "fx1": "f(x₁)",

            "fx2": "f(x₂)",

            "error": "Error %"

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

        self.tabla.column(
            "tipo",
            width=75
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
            text="FUNCIÓN Y ÓPTIMOS",
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

            tolerancia = float(
                self.entrada_tolerancia.get()
            )

            max_iter = int(
                self.entrada_iteraciones.get()
            )

            tipo = self.combo_tipo.get()

            # ==================================================
            # VALIDACIONES
            # ==================================================

            if not expresion:

                raise ValueError(
                    "Debe ingresar una función."
                )

            if xl >= xu:

                raise ValueError(
                    "El límite inferior debe ser menor "
                    "que el límite superior."
                )

            if tolerancia <= 0:

                raise ValueError(
                    "La tolerancia debe ser mayor que 0."
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

            f(xl)
            f(xu)

            # ==================================================
            # EJECUTAR MÉTODO
            # ==================================================

            resultado = razon_dorada(

                f,

                xl,

                xu,

                tolerancia,

                max_iter,

                tipo

            )

            # ==================================================
            # MÁXIMO
            # ==================================================

            if tipo == "Máximo":

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
                        f"Máximo: "
                        f"x = {xr:.10f}     |     "
                        f"f(x) = {valor:.10f}     |     "
                        f"Iteraciones: {iteraciones}     |     "
                        f"Error: {error:.10f}%"
                    )
                )

                self.mostrar_tabla(
                    resultado["tabla"],
                    "Máximo"
                )

                self.graficar(f, xl, xu, resultado, "Máximo")

            # ==================================================
            # MÍNIMO
            # ==================================================

            elif tipo == "Mínimo":

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
                        f"Mínimo: "
                        f"x = {xr:.10f}     |     "
                        f"f(x) = {valor:.10f}     |     "
                        f"Iteraciones: {iteraciones}     |     "
                        f"Error: {error:.10f}%"
                    )
                )

                self.mostrar_tabla(
                    resultado["tabla"],
                    "Mínimo"
                )

                self.graficar(f, xl, xu, resultado, "Mínimo")

            # ==================================================
            # AMBOS
            # ==================================================

            else:

                maximo = resultado[
                    "maximo"
                ]

                minimo = resultado[
                    "minimo"
                ]

                self.label_resultado.config(
                    text=(
                        f"Máximo: "
                        f"x = {maximo['x_optimo']:.8f} | "
                        f"f(x) = {maximo['valor']:.8f}"
                        f"     ||     "
                        f"Mínimo: "
                        f"x = {minimo['x_optimo']:.8f} | "
                        f"f(x) = {minimo['valor']:.8f}"
                    )
                )

                # Tabla de ambos

                self.mostrar_tabla_ambos(
                    maximo["tabla"],
                    minimo["tabla"]
                )

                # Gráfica de ambos

                self.graficar_ambos(
                    f,
                    xl,
                    xu,
                    maximo,
                    minimo
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

    # ==========================================================
    # MOSTRAR TABLA
    # ==========================================================

    def mostrar_tabla(
        self,
        datos,
        tipo
    ):

        # Limpiar tabla

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # Insertar datos

        for fila in datos:

            self.tabla.insert(
                "",
                "end",
                values=(

                    tipo,

                    fila["iteracion"],

                    f"{fila['xl']:.8f}",

                    f"{fila['xu']:.8f}",

                    f"{fila['x1']:.8f}",

                    f"{fila['x2']:.8f}",

                    f"{fila['fx1']:.8f}",

                    f"{fila['fx2']:.8f}",

                    f"{fila['error']:.8f}"

                )
            )

    # ==========================================================
    # MOSTRAR TABLA DE AMBOS
    # ==========================================================

    def mostrar_tabla_ambos(
        self,
        tabla_maximo,
        tabla_minimo
    ):

        # Limpiar tabla

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # ======================================================
        # MÁXIMO
        # ======================================================

        for fila in tabla_maximo:

            self.tabla.insert(
                "",
                "end",
                values=(

                    "Máximo",

                    fila["iteracion"],

                    f"{fila['xl']:.8f}",

                    f"{fila['xu']:.8f}",

                    f"{fila['x1']:.8f}",

                    f"{fila['x2']:.8f}",

                    f"{fila['fx1']:.8f}",

                    f"{fila['fx2']:.8f}",

                    f"{fila['error']:.8f}"

                )
            )

        # ======================================================
        # MÍNIMO
        # ======================================================

        for fila in tabla_minimo:

            self.tabla.insert(
                "",
                "end",
                values=(

                    "Mínimo",

                    fila["iteracion"],

                    f"{fila['xl']:.8f}",

                    f"{fila['xu']:.8f}",

                    f"{fila['x1']:.8f}",

                    f"{fila['x2']:.8f}",

                    f"{fila['fx1']:.8f}",

                    f"{fila['fx2']:.8f}",

                    f"{fila['error']:.8f}"

                )
            )

    # ==========================================================
    # GRÁFICA
    # ==========================================================

    def graficar(self, f, xl, xu, resultado, tipo):
        self.ax.clear()
        self.ax.set_facecolor("#FFF5F5")

        xr = resultado["x_optimo"]
        yr = resultado["valor"]
        # elimina: tipo = resultado["tipo"]

    
        self.ax.set_title(f"Razón dorada - {tipo}")
    

        # ======================================================
        # RANGO
        # ======================================================

        distancia = max(
            xu - xl,
            2
        )

        inicio = (
            xl - distancia * 0.25
        )

        final = (
            xu + distancia * 0.25
        )

        # ======================================================
        # FUNCIÓN
        # ======================================================

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
                color=self.COLOR_GRAFICA,
                linewidth=2,
                label="f(x)"
            )

        # ======================================================
        # LÍMITES
        # ======================================================

        self.ax.scatter(
            [xl, xu],
            [f(xl), f(xu)],
            s=45,
            color="#C85A7A",
            label="Límites"
        )

        # ======================================================
        # ÓPTIMO
        # ======================================================

        self.ax.scatter(
            [xr],
            [yr],
            s=100,
            color="#E88B9E",
            zorder=5,
            label=(
                f"{tipo}: "
                f"({xr:.5f}, {yr:.5f})"
            )
        )

        # ======================================================
        # EJE X
        # ======================================================

        self.ax.axhline(
            0,
            color=self.COLOR_LINEA_EJE,
            linewidth=1
        )

        self.ax.set_xlabel(
            "x"
        )

        self.ax.set_ylabel(
            "f(x)"
        )

        self.ax.set_title(
            f"Razón dorada - {tipo}"
        )

        self.ax.grid(
            True,
            alpha=0.3
        )

        self.ax.legend(
            fontsize=8
        )

        self.figura.tight_layout()

        self.canvas.draw()

    # ==========================================================
    # GRÁFICA DE AMBOS
    # ==========================================================

    def graficar_ambos(
        self,
        f,
        xl,
        xu,
        resultado_maximo,
        resultado_minimo
    ):

        self.ax.clear()

        self.ax.set_facecolor(
            "#F8FAFC"
        )

        # ======================================================
        # DATOS
        # ======================================================

        xmax = resultado_maximo[
            "x_optimo"
        ]

        ymax = resultado_maximo[
            "valor"
        ]

        xmin = resultado_minimo[
            "x_optimo"
        ]

        ymin = resultado_minimo[
            "valor"
        ]

        # ======================================================
        # RANGO
        # ======================================================

        distancia = max(
            xu - xl,
            2
        )

        inicio = (
            xl - distancia * 0.25
        )

        final = (
            xu + distancia * 0.25
        )

        # ======================================================
        # FUNCIÓN
        # ======================================================

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
                color=self.COLOR_GRAFICA,
                linewidth=2,
                label="f(x)"
            )

        # ======================================================
        # LÍMITES
        # ======================================================

        self.ax.scatter(
            [xl, xu],
            [f(xl), f(xu)],
            s=45,
            color="#C85A7A",
            label="Límites"
        )

        # MÁXIMO
        self.ax.scatter(
            [xmax],
            [ymax],
            s=100,
            color="#E88B9E",
            zorder=5,
            label=(
                f"Máximo: "
                f"({xmax:.5f}, {ymax:.5f})"
            )
        )

        # MÍNIMO
        self.ax.scatter(
            [xmin],
            [ymin],
            s=100,
            color="#C85A7A",
            zorder=5,
            label=(
                f"Mínimo: "
                f"({xmin:.5f}, {ymin:.5f})"
            )
        )

        # ======================================================
        # EJE X
        # ======================================================

        self.ax.axhline(
            0,
            color=self.COLOR_LINEA_EJE,
            linewidth=1
        )

        self.ax.set_xlabel(
            "x"
        )

        self.ax.set_ylabel(
            "f(x)"
        )

        self.ax.set_title(
            "Método de la razón dorada - Máximo y mínimo"
        )

        self.ax.grid(
            True,
            alpha=0.3
        )

        self.ax.legend(
            fontsize=8
        )

        self.figura.tight_layout()

        self.canvas.draw()