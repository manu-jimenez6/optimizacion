# vistas/newton_raphson_view.py

import tkinter as tk
from tkinter import ttk, messagebox

import math
import sympy as sp

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.newton_raphson import newton_raphson


class VentanaNewtonRaphson:
    
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
            "Método de Newton-Raphson"
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

        self.resultados = []

        self.configurar_estilos()

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="MÉTODO DE NEWTON-RAPHSON",
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
                "Encuentra máximos y mínimos "
                "mediante la segunda derivada"
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
            pady=5,
            sticky="w"
        )

        self.entrada_funcion = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=35,
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
            "x**3 - 3*x"
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
            padx=(15, 5),
            pady=5
        )

        self.entrada_x0 = tk.Entry(
            panel_entrada,
            font=("Segoe UI", 11),
            width=15,
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            insertbackground=self.COLOR_TEXTO,
            relief="flat"
        )

        self.entrada_x0.grid(
            row=0,
            column=3,
            padx=8,
            pady=5
        )

        self.entrada_x0.insert(
            0,
            "-2, 2"
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
            padx=(15, 5),
            pady=5
        )

        self.combo_tipo = ttk.Combobox(
            panel_entrada,
            values=[
                "Máximo",
                "Mínimo",
                "Ambos"
            ],
            state="readonly",
            width=12,
            font=("Segoe UI", 10)
        )

        self.combo_tipo.grid(
            row=0,
            column=5,
            padx=8,
            pady=5
        )

        self.combo_tipo.set(
            "Ambos"
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
            row=0,
            column=6,
            padx=(15, 5),
            pady=5
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

        panel_derivadas = tk.Frame(
            self.root,
            bg=self.COLOR_PANEL,
            padx=15,
            pady=8
        )

        panel_derivadas.pack(
            fill="x",
            padx=20,
            pady=(0, 8)
        )

        tk.Label(
            panel_derivadas,
            text="f'(x):",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        self.label_primera = tk.Label(
            panel_derivadas,
            text="--",
            font=("Segoe UI", 10),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_PANEL,
            anchor="w"
        )

        self.label_primera.grid(
            row=0,
            column=1,
            padx=8,
            pady=3,
            sticky="w"
        )

        tk.Label(
            panel_derivadas,
            text="f''(x):",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=3
        )

        self.label_segunda = tk.Label(
            panel_derivadas,
            text="--",
            font=("Segoe UI", 10),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_PANEL,
            anchor="w"
        )

        self.label_segunda.grid(
            row=1,
            column=1,
            padx=8,
            pady=3,
            sticky="w"
        )

        self.label_resultado = tk.Label(
            self.root,
            text="Resultados: --",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_EXITO,
            bg=self.COLOR_FONDO
        )

        self.label_resultado.pack(
            pady=(2, 8)
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
            pady=(8, 6)
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
            "tipo",
            "i",
            "x",
            "fx",
            "fpx",
            "fppx",
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

            "tipo": "Tipo",

            "i": "i",

            "x": "xᵢ",

            "fx": "f(xᵢ)",

            "fpx": "f'(xᵢ)",

            "fppx": "f''(xᵢ)",

            "xr": "xᵢ₊₁",

            "fxr": "f(xᵢ₊₁)",

            "error": "Error"
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=95,
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

        panel_graficas = tk.Frame(
            panel_inferior,
            bg=self.COLOR_PANEL,
            width=360
        )

        panel_graficas.pack(
            side="right",
            fill="both",
            padx=(8, 0)
        )

        panel_graficas.pack_propagate(
            False
        )

        tk.Label(
            panel_graficas,
            text="FUNCIÓN Y PUNTOS CRÍTICOS",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).pack(
            pady=(8, 2)
        )

        frame_funcion = tk.Frame(
            panel_graficas,
            bg=self.COLOR_PANEL
        )

        frame_funcion.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 5)
        )

        self.figura_funcion = Figure(
            figsize=(4, 3),
            dpi=85,
            facecolor=self.COLOR_PANEL
        )

        self.ax_funcion = (
            self.figura_funcion
            .add_subplot(111)
        )

        self.canvas_funcion = FigureCanvasTkAgg(
            self.figura_funcion,
            master=frame_funcion
        )

        self.canvas_funcion.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        tk.Label(
            panel_graficas,
            text="ERROR POR ITERACIÓN",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).pack(
            pady=(5, 2)
        )

        frame_error = tk.Frame(
            panel_graficas,
            bg=self.COLOR_PANEL
        )

        frame_error.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8)
        )

        self.figura_error = Figure(
            figsize=(4, 2.5),
            dpi=85,
            facecolor=self.COLOR_PANEL
        )

        self.ax_error = (
            self.figura_error
            .add_subplot(111)
        )

        self.canvas_error = FigureCanvasTkAgg(
            self.figura_error,
            master=frame_error
        )

        self.canvas_error.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
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

    def crear_funciones(self, expresion):

        x = sp.symbols("x")

        expresion = expresion.replace("^", "**")

        entorno = {

            "x": x,

            "sin": sp.sin,

            "cos": sp.cos,

            "tan": sp.tan,

            "asin": sp.asin,

            "acos": sp.acos,

            "atan": sp.atan,

            "sqrt": sp.sqrt,

            "exp": sp.exp,

            "log": sp.log,

            "ln": sp.log,

            "log10": sp.log,

            "pi": sp.pi,

            "e": sp.E,

            "abs": sp.Abs
        }

        try:

            funcion = sp.sympify(
                expresion,
                locals=entorno
            )

        except Exception as error:

            raise ValueError(
                "La función no es válida.\n\n"
                f"{error}"
            )
            
        primera = sp.diff(funcion, x)

        segunda = sp.diff(primera, x)

        f = sp.lambdify(x, funcion, "math")

        fp = sp.lambdify(x, primera, "math")

        fpp = sp.lambdify(x, segunda, "math")

        return (
            funcion,
            primera,
            segunda,
            f,
            fp,
            fpp
        )

    def obtener_x0(self):

        texto = (
            self.entrada_x0
            .get()
            .strip()
        )

        if not texto:

            raise ValueError(
                "Debe ingresar al menos un valor de x₀."
            )

        try:

            valores = []

            partes = texto.split(",")

            for parte in partes:

                valor = float(parte.strip())

                valores.append(valor)

            return valores

        except ValueError:

            raise ValueError(
                "Los valores de x₀ deben ser números.\n\n"
                "Ejemplo:\n"
                "-2, 2"
            )

    def calcular(self):

        try:

            expresion = (
                self.entrada_funcion
                .get()
                .strip()
            )

            tipo_busqueda = (
                self.combo_tipo
                .get()
            )

            x0_lista = self.obtener_x0()

            if not expresion:

                raise ValueError(
                    "Debe ingresar una función."
                )

            (
                funcion_sympy,
                primera_sympy,
                segunda_sympy,
                f,
                fp,
                fpp
            ) = self.crear_funciones(expresion)

            self.label_primera.config(
                text=str(sp.sstr(primera_sympy))
            )

            self.label_segunda.config(
                text=str(sp.sstr(segunda_sympy))
            )

            self.resultados = []

            errores = []

            for x0 in x0_lista:

                try:

                    resultado = newton_raphson(
                        f,
                        fp,
                        fpp,
                        x0,
                        self.TOLERANCIA,
                        self.MAX_ITERACIONES
                    )

                    x_nuevo = resultado["x_critico"]

                    repetido = False

                    for anterior in self.resultados:

                        if abs(
                            anterior["x_critico"] - x_nuevo
                        ) < 0.0001:

                            repetido = True

                            break

                    if not repetido:

                        self.resultados.append(resultado)

                except Exception as e:

                    errores.append(
                        f"x₀ = {x0}: {e}"
                    )

            if not self.resultados:

                mensaje = (
                    "No se pudo encontrar ningún punto crítico.\n\n"
                )

                if errores:

                    mensaje += (
                        "Errores por x₀:\n"
                        + "\n".join(errores)
                    )

                else:

                    mensaje += "Prueba con otro valor de x₀."

                raise ValueError(mensaje)

            if tipo_busqueda == "Ambos":

                resultados_filtrados = list(self.resultados)

            else:

                resultados_filtrados = [
                    r for r in self.resultados
                    if r["tipo"] == tipo_busqueda
                ]

            if not resultados_filtrados:

                tipos_encontrados = list({
                    r["tipo"] for r in self.resultados
                })

                mensaje = (
                    f"No se encontró un '{tipo_busqueda}' "
                    f"con los valores iniciales proporcionados.\n\n"
                    f"Tipos encontrados: "
                    f"{', '.join(tipos_encontrados) or 'ninguno'}.\n\n"
                    f"Prueba con otros valores de x₀."
                )

                if errores:

                    mensaje += (
                        "\n\nErrores por x₀:\n"
                        + "\n".join(errores)
                    )

                raise ValueError(mensaje)

            resultados_filtrados.sort(
                key=lambda r: r["x_critico"]
            )

            self.mostrar_resultados(resultados_filtrados)

            self.mostrar_tabla(resultados_filtrados)

            self.graficar_funcion(f, resultados_filtrados)

            self.graficar_error(resultados_filtrados)

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                "No se pudo procesar la función.\n\n"
                f"{error}"
            )

    def mostrar_resultados(self, resultados):

        textos = []

        for resultado in resultados:

            tipo = resultado["tipo"]

            x = resultado["x_critico"]

            valor = resultado["valor"]

            textos.append(
                f"{tipo}: x = {x:.8f}, "
                f"f(x) = {valor:.8f}"
            )

        texto = "     |     ".join(textos)

        self.label_resultado.config(
            text=texto,
            fg=self.COLOR_EXITO
        )

    def mostrar_tabla(self, resultados):

        # Limpiar

        for item in self.tabla.get_children():

            self.tabla.delete(item)

        # Agregar

        for resultado in resultados:

            tipo = resultado["tipo"]

            for fila in resultado["tabla"]:

                self.tabla.insert(

                    "",

                    "end",

                    values=(

                        tipo,

                        fila["iteracion"],

                        f"{fila['x']:.8f}",

                        f"{fila['fx']:.8f}",

                        f"{fila['fpx']:.8f}",

                        f"{fila['fppx']:.8f}",

                        f"{fila['xr']:.8f}",

                        f"{fila['fxr']:.8f}",

                        f"{fila['error1']:.8f}"
                    )
                )

    def graficar_funcion(self, f, resultados):

        self.ax_funcion.clear()

        self.ax_funcion.set_facecolor(self.COLOR_PANEL_2)

        xs = [r["x_critico"] for r in resultados]

        minimo = min(xs)

        maximo = max(xs)

        distancia = max(maximo - minimo, 2)

        inicio = minimo - distancia

        final = maximo + distancia

        cantidad = 400

        valores_x = []

        valores_y = []

        paso = (final - inicio) / cantidad

        for i in range(cantidad + 1):

            x = inicio + i * paso

            try:

                y = f(x)

                if (
                    isinstance(y, (int, float))
                    and math.isfinite(y)
                ):

                    valores_x.append(x)

                    valores_y.append(y)

            except Exception:

                pass

        if valores_x:

            self.ax_funcion.plot(
                valores_x,
                valores_y,
                linewidth=2,
                color=self.COLOR_BOTON,
                label="f(x)"
            )

        for resultado in resultados:

            x = resultado["x_critico"]

            y = resultado["valor"]

            tipo = resultado["tipo"]

            self.ax_funcion.scatter(
                [x],
                [y],
                s=80,
                zorder=5,
                color=self.COLOR_HOVER,
                edgecolors="white",
                linewidths=1,
                label=(
                    f"{tipo}: "
                    f"({x:.4f}, {y:.4f})"
                )
            )

        self.ax_funcion.axhline(
            0,
            linewidth=1,
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_funcion.set_xlabel(
            "x",
            color=self.COLOR_TEXTO
        )

        self.ax_funcion.set_ylabel(
            "f(x)",
            color=self.COLOR_TEXTO
        )

        self.ax_funcion.set_title(
            "Función y puntos críticos",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_funcion.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_funcion.grid(
            True,
            alpha=0.3,
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        for borde in self.ax_funcion.spines.values():

            borde.set_color(self.COLOR_TEXTO_SECUNDARIO)

        leyenda = self.ax_funcion.legend(fontsize=8)

        if leyenda:

            leyenda.get_frame().set_facecolor(self.COLOR_PANEL)

            leyenda.get_frame().set_edgecolor(self.COLOR_BOTON)

            for texto in leyenda.get_texts():

                texto.set_color(self.COLOR_TEXTO_SECUNDARIO)

        self.figura_funcion.tight_layout()

        self.canvas_funcion.draw()

    def graficar_error(self, resultados):

        self.ax_error.clear()

        self.ax_error.set_facecolor(self.COLOR_PANEL_2)

        for resultado in resultados:

            datos = resultado["tabla"]

            iteraciones = []

            errores = []

            for fila in datos:

                iteraciones.append(fila["iteracion"])

                errores.append(fila["error1"])

            if iteraciones:

                self.ax_error.plot(
                    iteraciones,
                    errores,
                    marker="o",
                    markersize=3,
                    linewidth=1.5,
                    color=self.COLOR_BOTON,
                    label=resultado["tipo"]
                )

        self.ax_error.set_xlabel(
            "Iteración",
            color=self.COLOR_TEXTO
        )

        self.ax_error.set_ylabel(
            "Error absoluto",
            color=self.COLOR_TEXTO
        )

        self.ax_error.set_title(
            "Error por iteración",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_error.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_error.grid(
            True,
            alpha=0.3,
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        for borde in self.ax_error.spines.values():

            borde.set_color(self.COLOR_TEXTO_SECUNDARIO)

        if resultados:

            leyenda = self.ax_error.legend(fontsize=8)

            if leyenda:

                leyenda.get_frame().set_facecolor(self.COLOR_PANEL)

                leyenda.get_frame().set_edgecolor(self.COLOR_BOTON)

                for texto in leyenda.get_texts():

                    texto.set_color(self.COLOR_TEXTO_SECUNDARIO)

        self.figura_error.tight_layout()

        self.canvas_error.draw()
