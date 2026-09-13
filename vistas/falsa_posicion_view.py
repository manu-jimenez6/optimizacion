# vistas/falsa_posicion_view.py

import tkinter as tk
from tkinter import ttk, messagebox
import math

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.falsa_posicion import falsa_posicion


class VentanaFalsaPosicion:

    # =========================================================
    # COLORES - MISMO ESTILO DE BISECCIÓN
    # =========================================================

    COLOR_FONDO = "#FFE4E1"          # Rosa pastel claro
    COLOR_PANEL = "#FFD1DC"          # Rosa pastel
    COLOR_PANEL_2 = "#FFF0F0"        # Rosa muy claro

    COLOR_BOTON = "#E88B9E"          # Rosa botón
    COLOR_HOVER = "#D47A8D"          # Rosa hover

    COLOR_TEXTO = "#B34B6E"          # Rosa oscuro
    COLOR_TEXTO_SECUNDARIO = "#8B5A68"

    COLOR_EXITO = "#B34B6E"
    COLOR_ERROR = "#B34B6E"

    COLOR_ENTRADA = "#FFF5F5"
    COLOR_ENTRADA_TEXTO = "#B34B6E"

    COLOR_BORDE = "#E8A0B0"

    # =========================================================
    # CONSTRUCTOR
    # =========================================================

    def __init__(self, root):

        self.root = root

        # =====================================================
        # CONFIGURACIÓN
        # =====================================================

        self.root.title(
            "Método de Falsa Posición"
        )

        self.root.geometry(
            "1400x800"
        )

        self.root.minsize(
            1100,
            700
        )

        self.root.configure(
            bg=self.COLOR_FONDO
        )

        # =====================================================
        # ESTILOS
        # =====================================================

        self.configurar_estilos()

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = tk.Label(
            root,
            text="MÉTODO DE FALSA POSICIÓN",
            font=("Arial", 18, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_FONDO
        )

        titulo.pack(
            pady=(10, 2)
        )

        subtitulo = tk.Label(
            root,
            text="Encuentra una raíz mediante el método de falsa posición",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO_SECUNDARIO,
            bg=self.COLOR_FONDO
        )

        subtitulo.pack(
            pady=(0, 8)
        )

        # =====================================================
        # PANEL PRINCIPAL
        # =====================================================

        panel_principal = tk.Frame(
            root,
            bg=self.COLOR_FONDO
        )

        panel_principal.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # =====================================================
        # PANEL IZQUIERDO
        # =====================================================

        panel_izquierdo = tk.Frame(
            panel_principal,
            bg=self.COLOR_FONDO
        )

        panel_izquierdo.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 5)
        )

        # =====================================================
        # PANEL DERECHO
        # =====================================================

        panel_derecho = tk.Frame(
            panel_principal,
            bg=self.COLOR_FONDO
        )

        panel_derecho.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5, 0)
        )

        # =====================================================
        # PANEL DE ENTRADA
        # =====================================================

        panel_entrada = tk.LabelFrame(
            panel_izquierdo,
            text="Datos de entrada",
            font=("Arial", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL,
            padx=15,
            pady=10,
            relief=tk.GROOVE,
            bd=2
        )

        panel_entrada.pack(
            fill="x",
            padx=5,
            pady=5
        )

        panel_entrada.columnconfigure(
            1,
            weight=1
        )

        # =====================================================
        # FUNCIÓN
        # =====================================================

        tk.Label(
            panel_entrada,
            text="Función f(x):",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=0,
            column=0,
            padx=(5, 8),
            pady=5,
            sticky="w"
        )

        self.entrada_funcion = self.crear_entry(
            panel_entrada,
            width=40
        )

        self.entrada_funcion.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=5,
            pady=5,
            sticky="ew"
        )

        self.entrada_funcion.insert(
            0,
            "x**3 - x - 2"
        )

        # =====================================================
        # XL
        # =====================================================

        tk.Label(
            panel_entrada,
            text="xl:",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=0,
            padx=(5, 5),
            pady=5,
            sticky="w"
        )

        self.entrada_xl = self.crear_entry(
            panel_entrada,
            width=12
        )

        self.entrada_xl.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_xl.insert(
            0,
            "1"
        )

        # =====================================================
        # XU
        # =====================================================

        tk.Label(
            panel_entrada,
            text="xu:",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=1,
            column=2,
            padx=(10, 5),
            pady=5,
            sticky="w"
        )

        self.entrada_xu = self.crear_entry(
            panel_entrada,
            width=12
        )

        self.entrada_xu.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_xu.insert(
            0,
            "2"
        )

        # =====================================================
        # TOLERANCIA
        # =====================================================

        tk.Label(
            panel_entrada,
            text="Tolerancia:",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=2,
            column=0,
            padx=(5, 5),
            pady=5,
            sticky="w"
        )

        self.entrada_tolerancia = self.crear_entry(
            panel_entrada,
            width=12
        )

        self.entrada_tolerancia.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_tolerancia.insert(
            0,
            "0.001"
        )

        # =====================================================
        # MÁXIMO ITERACIONES
        # =====================================================

        tk.Label(
            panel_entrada,
            text="Máx. iteraciones:",
            font=("Arial", 10),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL
        ).grid(
            row=2,
            column=2,
            padx=(10, 5),
            pady=5,
            sticky="w"
        )

        self.entrada_iteraciones = self.crear_entry(
            panel_entrada,
            width=12
        )

        self.entrada_iteraciones.grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_iteraciones.insert(
            0,
            "100"
        )

        # =====================================================
        # BOTONES
        # =====================================================

        frame_botones = tk.Frame(
            panel_entrada,
            bg=self.COLOR_PANEL
        )

        frame_botones.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=8
        )

        self.boton_calcular = tk.Button(
            frame_botones,
            text="Calcular",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_BOTON,
            fg="white",
            activebackground=self.COLOR_HOVER,
            activeforeground="white",
            relief=tk.RAISED,
            bd=3,
            width=12,
            cursor="hand2",
            command=self.calcular
        )

        self.boton_calcular.pack(
            side="left",
            padx=5
        )

        self.boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_BORDE,
            fg="white",
            activebackground=self.COLOR_HOVER,
            activeforeground="white",
            relief=tk.RAISED,
            bd=3,
            width=12,
            cursor="hand2",
            command=self.limpiar
        )

        self.boton_limpiar.pack(
            side="left",
            padx=5
        )

        # =====================================================
        # HOVER BOTÓN CALCULAR
        # =====================================================

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

        # =====================================================
        # HOVER BOTÓN LIMPIAR
        # =====================================================

        self.boton_limpiar.bind(
            "<Enter>",
            lambda e: self.boton_limpiar.config(
                bg="#D48A9A"
            )
        )

        self.boton_limpiar.bind(
            "<Leave>",
            lambda e: self.boton_limpiar.config(
                bg=self.COLOR_BORDE
            )
        )

        # =====================================================
        # RESULTADO
        # =====================================================

        self.label_resultado = tk.Label(
            panel_izquierdo,
            text="Raíz: --     |     Iteraciones: --     |     Error: --",
            font=("Arial", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_FONDO
        )

        self.label_resultado.pack(
            pady=5
        )

        # =====================================================
        # TABLA
        # =====================================================

        panel_tabla = tk.LabelFrame(
            panel_izquierdo,
            text="Tabla de Iteraciones",
            font=("Arial", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL,
            padx=10,
            pady=10,
            relief=tk.GROOVE,
            bd=2
        )

        panel_tabla.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        # =====================================================
        # FRAME TREEVIEW
        # =====================================================

        frame_tree = tk.Frame(
            panel_tabla,
            bg=self.COLOR_PANEL
        )

        frame_tree.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # COLUMNAS
        # =====================================================

        columnas = (
            "i",
            "xl",
            "xu",
            "xr",
            "fxl",
            "fxu",
            "fxr",
            "producto",
            "error1",
            "error2",
            "error3"
        )

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings",
            style="Custom.Treeview"
        )

        nombres = {
            "i": "i",
            "xl": "xl",
            "xu": "xu",
            "xr": "xr",
            "fxl": "f(xl)",
            "fxu": "f(xu)",
            "fxr": "f(xr)",
            "producto": "f(xl)·f(xr)",
            "error1": "Error 1",
            "error2": "Error 2",
            "error3": "Error 3"
        }

        anchos = {
            "i": 45,
            "xl": 75,
            "xu": 75,
            "xr": 75,
            "fxl": 85,
            "fxu": 85,
            "fxr": 85,
            "producto": 100,
            "error1": 80,
            "error2": 80,
            "error3": 80
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=anchos[columna],
                minwidth=anchos[columna],
                anchor="center",
                stretch=False
            )

        # =====================================================
        # SCROLLBARS
        # =====================================================

        scrollbar_vertical = ttk.Scrollbar(
            frame_tree,
            orient=tk.VERTICAL,
            command=self.tabla.yview
        )

        scrollbar_horizontal = ttk.Scrollbar(
            frame_tree,
            orient=tk.HORIZONTAL,
            command=self.tabla.xview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set
        )

        self.tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        frame_tree.rowconfigure(
            0,
            weight=1
        )

        frame_tree.columnconfigure(
            0,
            weight=1
        )

        # =====================================================
        # PANEL DERECHO - GRÁFICAS
        # =====================================================

        panel_graficas = tk.Frame(
            panel_derecho,
            bg=self.COLOR_FONDO
        )

        panel_graficas.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        # =====================================================
        # GRÁFICA DE FUNCIÓN
        # =====================================================

        frame_funcion = tk.LabelFrame(
            panel_graficas,
            text="Gráfica de f(x)",
            font=("Arial", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL,
            padx=5,
            pady=5,
            relief=tk.GROOVE,
            bd=2
        )

        frame_funcion.pack(
            fill="both",
            expand=True,
            pady=(0, 5)
        )

        self.figura_funcion = Figure(
            figsize=(5, 3),
            dpi=90,
            facecolor=self.COLOR_PANEL
        )

        self.ax_funcion = self.figura_funcion.add_subplot(
            111
        )

        self.canvas_funcion = FigureCanvasTkAgg(
            self.figura_funcion,
            master=frame_funcion
        )

        self.canvas_funcion.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # GRÁFICA DEL ERROR
        # =====================================================

        frame_error = tk.LabelFrame(
            panel_graficas,
            text="Gráfica del error",
            font=("Arial", 10, "bold"),
            fg=self.COLOR_TEXTO,
            bg=self.COLOR_PANEL,
            padx=5,
            pady=5,
            relief=tk.GROOVE,
            bd=2
        )

        frame_error.pack(
            fill="both",
            expand=True,
            pady=(5, 0)
        )

        self.figura_error = Figure(
            figsize=(5, 3),
            dpi=90,
            facecolor=self.COLOR_PANEL
        )

        self.ax_error = self.figura_error.add_subplot(
            111
        )

        self.canvas_error = FigureCanvasTkAgg(
            self.figura_error,
            master=frame_error
        )

        self.canvas_error.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # GRÁFICAS INICIALES
        # =====================================================

        self.configurar_grafica_vacia()

    # =========================================================
    # CREAR ENTRY
    # =========================================================

    def crear_entry(
        self,
        parent,
        width=20
    ):

        entry = tk.Entry(
            parent,
            width=width,
            font=("Arial", 10),
            bg=self.COLOR_ENTRADA,
            fg=self.COLOR_ENTRADA_TEXTO,
            relief=tk.FLAT,
            bd=2,
            highlightthickness=2,
            highlightbackground=self.COLOR_BORDE,
            highlightcolor=self.COLOR_BORDE,
            insertbackground=self.COLOR_TEXTO
        )

        return entry

    # =========================================================
    # ESTILOS
    # =========================================================

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except tk.TclError:

            pass

        # -----------------------------------------------------
        # TREEVIEW
        # -----------------------------------------------------

        estilo.configure(
            "Custom.Treeview",
            background="#FFF0F0",
            foreground=self.COLOR_TEXTO,
            fieldbackground="#FFF0F0",
            rowheight=25,
            borderwidth=0,
            font=("Arial", 9)
        )

        # -----------------------------------------------------
        # ENCABEZADOS
        # -----------------------------------------------------

        estilo.configure(
            "Custom.Treeview.Heading",
            background="#E8A0B0",
            foreground="white",
            font=("Arial", 9, "bold"),
            relief="flat"
        )

        # -----------------------------------------------------
        # SELECCIÓN
        # -----------------------------------------------------

        estilo.map(
            "Custom.Treeview",
            background=[
                ("selected", "#E88B9E")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        # -----------------------------------------------------
        # SCROLLBARS
        # -----------------------------------------------------

        estilo.configure(
            "Vertical.TScrollbar",
            background="#E8A0B0",
            troughcolor=self.COLOR_FONDO,
            bordercolor=self.COLOR_FONDO,
            arrowcolor="white"
        )

        estilo.configure(
            "Horizontal.TScrollbar",
            background="#E8A0B0",
            troughcolor=self.COLOR_FONDO,
            bordercolor=self.COLOR_FONDO,
            arrowcolor="white"
        )

    # =========================================================
    # CREAR FUNCIÓN
    # =========================================================

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

    # =========================================================
    # CALCULAR
    # =========================================================

    def calcular(self):

        try:

            # -------------------------------------------------
            # OBTENER DATOS
            # -------------------------------------------------

            expresion = (
                self.entrada_funcion
                .get()
                .strip()
            )

            if not expresion:

                raise ValueError(
                    "Debe ingresar una función."
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

            # -------------------------------------------------
            # VALIDACIONES
            # -------------------------------------------------

            if xl >= xu:

                raise ValueError(
                    "xl debe ser menor que xu."
                )

            if tolerancia < 0:

                raise ValueError(
                    "La tolerancia no puede ser negativa."
                )

            if max_iter <= 0:

                raise ValueError(
                    "El número de iteraciones debe ser mayor que 0."
                )

            # -------------------------------------------------
            # CREAR FUNCIÓN
            # -------------------------------------------------

            f = self.crear_funcion(
                expresion
            )

            # Verificar que la función pueda evaluarse
            f(xl)
            f(xu)

            # -------------------------------------------------
            # MÉTODO DE FALSA POSICIÓN
            # -------------------------------------------------

            resultado = falsa_posicion(
                f,
                xl,
                xu,
                tolerancia,
                max_iter
            )

            # -------------------------------------------------
            # OBTENER RESULTADOS
            # -------------------------------------------------

            raiz = resultado["raiz"]

            iteraciones = resultado[
                "iteraciones"
            ]

            error = resultado[
                "error"
            ]

            # -------------------------------------------------
            # MOSTRAR RESULTADO
            # -------------------------------------------------

            self.label_resultado.config(
                text=(
                    f"Raíz: {raiz:.8f}"
                    f"     |     Iteraciones: {iteraciones}"
                    f"     |     Error: {error:.8f}"
                ),
                fg=self.COLOR_TEXTO
            )

            # -------------------------------------------------
            # MOSTRAR TABLA
            # -------------------------------------------------

            self.mostrar_tabla(
                resultado["tabla"]
            )

            # -------------------------------------------------
            # GRAFICAR FUNCIÓN
            # -------------------------------------------------

            self.graficar_funcion(
                f,
                xl,
                xu,
                raiz
            )

            # -------------------------------------------------
            # GRAFICAR ERROR
            # -------------------------------------------------

            self.graficar_error(
                resultado["tabla"]
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except ZeroDivisionError:

            messagebox.showerror(
                "Error",
                "Se produjo una división entre cero."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo procesar la función.\n\n{error}"
            )

    # =========================================================
    # MOSTRAR TABLA
    # =========================================================

    def mostrar_tabla(
        self,
        datos
    ):

        # -----------------------------------------------------
        # LIMPIAR TABLA
        # -----------------------------------------------------

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # -----------------------------------------------------
        # INSERTAR DATOS
        # -----------------------------------------------------

        for fila in datos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    fila["iteracion"],
                    self.formatear_numero(
                        fila["xl"]
                    ),
                    self.formatear_numero(
                        fila["xu"]
                    ),
                    self.formatear_numero(
                        fila["xr"]
                    ),
                    self.formatear_numero(
                        fila["fxl"]
                    ),
                    self.formatear_numero(
                        fila["fxu"]
                    ),
                    self.formatear_numero(
                        fila["fxr"]
                    ),
                    self.formatear_numero(
                        fila["producto"]
                    ),
                    self.formatear_numero(
                        fila["error1"]
                    ),
                    self.formatear_numero(
                        fila["error2"]
                    ),
                    self.formatear_numero(
                        fila["error3"]
                    )
                )
            )

    # =========================================================
    # FORMATEAR NÚMERO
    # =========================================================

    def formatear_numero(
        self,
        valor
    ):

        try:

            texto = f"{valor:.6f}"

            texto = texto.rstrip(
                "0"
            ).rstrip(
                "."
            )

            return texto

        except Exception:

            return str(valor)

    # =========================================================
    # GRÁFICA DE FUNCIÓN
    # =========================================================

    def graficar_funcion(
        self,
        f,
        xl,
        xu,
        raiz
    ):

        self.ax_funcion.clear()

        self.ax_funcion.set_facecolor(
            self.COLOR_PANEL
        )

        # -----------------------------------------------------
        # RANGO
        # -----------------------------------------------------

        margen = (
            xu - xl
        ) * 0.20

        if margen == 0:

            margen = 1

        inicio = xl - margen
        final = xu + margen

        cantidad = 300

        valores_x = []
        valores_y = []

        paso = (
            final - inicio
        ) / cantidad

        # -----------------------------------------------------
        # EVALUAR FUNCIÓN
        # -----------------------------------------------------

        for i in range(
            cantidad + 1
        ):

            x = inicio + i * paso

            try:

                y = f(x)

                if (
                    isinstance(
                        y,
                        (int, float)
                    )
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

        # -----------------------------------------------------
        # DIBUJAR FUNCIÓN
        # -----------------------------------------------------

        if valores_x:

            self.ax_funcion.plot(
                valores_x,
                valores_y,
                color="#D47A8D",
                linewidth=2,
                label="f(x)"
            )

        # -----------------------------------------------------
        # EJE X
        # -----------------------------------------------------

        self.ax_funcion.axhline(
            0,
            color="#B34B6E",
            linewidth=1
        )

        # -----------------------------------------------------
        # RAÍZ
        # -----------------------------------------------------

        self.ax_funcion.scatter(
            [raiz],
            [0],
            color="#8B3A52",
            s=60,
            zorder=5,
            label=f"Raíz = {raiz:.6f}"
        )

        # -----------------------------------------------------
        # INTERVALO
        # -----------------------------------------------------

        self.ax_funcion.axvline(
            xl,
            color="#E8A0B0",
            linestyle="--",
            alpha=0.7
        )

        self.ax_funcion.axvline(
            xu,
            color="#E8A0B0",
            linestyle="--",
            alpha=0.7
        )

        # -----------------------------------------------------
        # CONFIGURACIÓN
        # -----------------------------------------------------

        self.ax_funcion.set_xlabel(
            "x",
            color=self.COLOR_TEXTO
        )

        self.ax_funcion.set_ylabel(
            "f(x)",
            color=self.COLOR_TEXTO
        )

        self.ax_funcion.set_title(
            "Función y raíz",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_funcion.tick_params(
            colors=self.COLOR_TEXTO
        )

        self.ax_funcion.grid(
            True,
            alpha=0.2
        )

        # -----------------------------------------------------
        # BORDE DE LA GRÁFICA
        # -----------------------------------------------------

        for spine in self.ax_funcion.spines.values():

            spine.set_color(
                self.COLOR_BORDE
            )

        # -----------------------------------------------------
        # LEYENDA
        # -----------------------------------------------------

        self.ax_funcion.legend(
            facecolor=self.COLOR_PANEL,
            edgecolor=self.COLOR_BORDE,
            labelcolor=self.COLOR_TEXTO
        )

        self.figura_funcion.tight_layout(
            pad=1
        )

        self.canvas_funcion.draw()

    # =========================================================
    # GRÁFICA DEL ERROR
    # =========================================================

    def graficar_error(
        self,
        datos
    ):

        self.ax_error.clear()

        self.ax_error.set_facecolor(
            self.COLOR_PANEL
        )

        iteraciones = []
        errores = []

        # -----------------------------------------------------
        # OBTENER DATOS
        # -----------------------------------------------------

        for fila in datos:

            iteraciones.append(
                fila["iteracion"]
            )

            errores.append(
                fila["error3"]
            )

        # -----------------------------------------------------
        # GRAFICAR
        # -----------------------------------------------------

        if len(iteraciones) > 0:

            self.ax_error.plot(
                iteraciones,
                errores,
                color="#D47A8D",
                marker="o",
                markersize=3,
                linewidth=1.5
            )

        # -----------------------------------------------------
        # CONFIGURACIÓN
        # -----------------------------------------------------

        self.ax_error.set_xlabel(
            "Iteración",
            color=self.COLOR_TEXTO
        )

        self.ax_error.set_ylabel(
            "Error %",
            color=self.COLOR_TEXTO
        )

        self.ax_error.set_title(
            "Error por iteración",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_error.tick_params(
            colors=self.COLOR_TEXTO
        )

        self.ax_error.grid(
            True,
            alpha=0.2
        )

        # -----------------------------------------------------
        # BORDES
        # -----------------------------------------------------

        for spine in self.ax_error.spines.values():

            spine.set_color(
                self.COLOR_BORDE
            )

        self.figura_error.tight_layout(
            pad=1
        )

        self.canvas_error.draw()

    # =========================================================
    # GRÁFICAS VACÍAS
    # =========================================================

    def configurar_grafica_vacia(self):

        # =====================================================
        # FUNCIÓN
        # =====================================================

        self.ax_funcion.clear()

        self.ax_funcion.set_facecolor(
            self.COLOR_PANEL
        )

        self.ax_funcion.set_title(
            "Función",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_funcion.set_xlabel(
            "x",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_funcion.set_ylabel(
            "f(x)",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_funcion.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_funcion.grid(
            True,
            alpha=0.2
        )

        for spine in self.ax_funcion.spines.values():

            spine.set_color(
                self.COLOR_BORDE
            )

        self.figura_funcion.tight_layout(
            pad=1
        )

        self.canvas_funcion.draw()

        # =====================================================
        # ERROR
        # =====================================================

        self.ax_error.clear()

        self.ax_error.set_facecolor(
            self.COLOR_PANEL
        )

        self.ax_error.set_title(
            "Error por iteración",
            color=self.COLOR_TEXTO,
            fontweight="bold"
        )

        self.ax_error.set_xlabel(
            "Iteración",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_error.set_ylabel(
            "Error %",
            color=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_error.tick_params(
            colors=self.COLOR_TEXTO_SECUNDARIO
        )

        self.ax_error.grid(
            True,
            alpha=0.2
        )

        for spine in self.ax_error.spines.values():

            spine.set_color(
                self.COLOR_BORDE
            )

        self.figura_error.tight_layout(
            pad=1
        )

        self.canvas_error.draw()

    # =========================================================
    # LIMPIAR
    # =========================================================

    def limpiar(self):

        # -----------------------------------------------------
        # CAMPOS
        # -----------------------------------------------------

        self.entrada_funcion.delete(
            0,
            tk.END
        )

        self.entrada_xl.delete(
            0,
            tk.END
        )

        self.entrada_xu.delete(
            0,
            tk.END
        )

        self.entrada_tolerancia.delete(
            0,
            tk.END
        )

        self.entrada_iteraciones.delete(
            0,
            tk.END
        )

        # -----------------------------------------------------
        # TABLA
        # -----------------------------------------------------

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # -----------------------------------------------------
        # RESULTADO
        # -----------------------------------------------------

        self.label_resultado.config(
            text="Raíz: --     |     Iteraciones: --     |     Error: --",
            fg=self.COLOR_TEXTO
        )

        # -----------------------------------------------------
        # GRÁFICAS
        # -----------------------------------------------------

        self.configurar_grafica_vacia()