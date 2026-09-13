# vistas/biseccion_view.py

import tkinter as tk
from tkinter import ttk, messagebox
import math

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from metodos.biseccion import biseccion


class VentanaBiseccion:


    COLOR_FONDO = "#FFE4E1"          # Rosa pastel claro
    COLOR_PANEL = "#FFD1DC"          # Rosa pastel
    COLOR_PANEL_2 = "#FFF0F0"        # Rosa muy claro

    COLOR_PRINCIPAL = "#B34B6E"      # Rosa oscuro
    COLOR_BOTON = "#E88B9E"          # Rosa botón
    COLOR_HOVER = "#D47A8D"          # Rosa hover
    COLOR_OSCURO = "#8B3A52"         # Rosa oscuro para destacar

    COLOR_TEXTO = "#B34B6E"
    COLOR_TEXTO_OSCURO = "#8B3A52"

    COLOR_ENTRADA = "#FFF5F5"
    COLOR_ENTRADA_TEXTO = "#B34B6E"

    COLOR_BLANCO = "#FFFFFF"
    COLOR_BORDE = "#E8A0B0"

    # =========================================================
    # CONSTRUCTOR
    # =========================================================

    def __init__(self, root):

        self.root = root

        # -----------------------------------------------------
        # CONFIGURACIÓN DE VENTANA
        # -----------------------------------------------------

        self.root.title("Método de Bisección")
        self.root.geometry("1400x800")
        self.root.minsize(1100, 700)
        self.root.configure(
            bg=self.COLOR_FONDO
        )

        # -----------------------------------------------------
        # CONFIGURAR ESTILOS
        # -----------------------------------------------------

        self.configurar_estilos()

        # -----------------------------------------------------
        # VARIABLES
        # -----------------------------------------------------

        self.entrada_funcion = None
        self.entrada_xl = None
        self.entrada_xu = None
        self.entrada_tolerancia = None
        self.entrada_iteraciones = None

        self.tabla = None

        self.figura_funcion = None
        self.ax_funcion = None
        self.canvas_funcion = None

        self.figura_error = None
        self.ax_error = None
        self.canvas_error = None

        self.label_resultado = None
        self.estado_label = None

        # -----------------------------------------------------
        # CREAR INTERFAZ
        # -----------------------------------------------------

        self.crear_interfaz()

    # =========================================================
    # ESTILOS
    # =========================================================

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        # -----------------------------------------------------
        # TREEVIEW
        # -----------------------------------------------------

        estilo.configure(
            "Rosa.Treeview",
            background=self.COLOR_PANEL_2,
            foreground=self.COLOR_PRINCIPAL,
            fieldbackground=self.COLOR_PANEL_2,
            rowheight=27,
            borderwidth=0,
            font=("Arial", 9)
        )

        estilo.configure(
            "Rosa.Treeview.Heading",
            background=self.COLOR_BOTON,
            foreground=self.COLOR_BLANCO,
            font=("Arial", 9, "bold"),
            relief="flat"
        )

        estilo.map(
            "Rosa.Treeview",
            background=[
                ("selected", self.COLOR_PRINCIPAL)
            ],
            foreground=[
                ("selected", self.COLOR_BLANCO)
            ]
        )

        # -----------------------------------------------------
        # SCROLLBARS
        # -----------------------------------------------------

        estilo.configure(
            "Rosa.Vertical.TScrollbar",
            background=self.COLOR_BORDE,
            troughcolor=self.COLOR_FONDO,
            bordercolor=self.COLOR_FONDO,
            arrowcolor=self.COLOR_PRINCIPAL
        )

        estilo.configure(
            "Rosa.Horizontal.TScrollbar",
            background=self.COLOR_BORDE,
            troughcolor=self.COLOR_FONDO,
            bordercolor=self.COLOR_FONDO,
            arrowcolor=self.COLOR_PRINCIPAL
        )

    # =========================================================
    # CREAR ENTRY
    # =========================================================

    def crear_entry_redondeado(
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
            insertbackground=self.COLOR_PRINCIPAL
        )

        return entry

    # =========================================================
    # CREAR INTERFAZ
    # =========================================================

    def crear_interfaz(self):

        # =====================================================
        # PANEL PRINCIPAL
        # =====================================================

        panel_principal = tk.PanedWindow(
            self.root,
            orient=tk.HORIZONTAL,
            bg=self.COLOR_FONDO,
            sashwidth=5,
            relief=tk.FLAT
        )

        panel_principal.pack(
            fill=tk.BOTH,
            expand=True,
            padx=8,
            pady=8
        )

        # =====================================================
        # PANEL IZQUIERDO
        # =====================================================

        panel_izquierdo = tk.Frame(
            panel_principal,
            bg=self.COLOR_FONDO
        )

        panel_principal.add(
            panel_izquierdo,
            minsize=600
        )

        # =====================================================
        # PANEL DERECHO
        # =====================================================

        panel_derecho = tk.Frame(
            panel_principal,
            bg=self.COLOR_FONDO
        )

        panel_principal.add(
            panel_derecho,
            minsize=500
        )

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = tk.Label(
            panel_izquierdo,
            text="MÉTODO DE BISECCIÓN",
            font=("Arial", 16, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRINCIPAL
        )

        titulo.pack(
            pady=(8, 2)
        )

        subtitulo = tk.Label(
            panel_izquierdo,
            text="Encuentra una raíz mediante el método de bisección",
            font=("Arial", 9),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRINCIPAL
        )

        subtitulo.pack(
            pady=(0, 8)
        )

        # =====================================================
        # PANEL DE ENTRADA
        # =====================================================

        frame_entrada = tk.LabelFrame(
            panel_izquierdo,
            text="Datos de entrada",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            padx=15,
            pady=12,
            relief=tk.GROOVE,
            bd=2
        )

        frame_entrada.pack(
            fill=tk.X,
            padx=10,
            pady=5
        )

        frame_entrada.columnconfigure(
            1,
            weight=1
        )

        # =====================================================
        # FUNCIÓN
        # =====================================================

        tk.Label(
            frame_entrada,
            text="Función f(x):",
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            font=("Arial", 10)
        ).grid(
            row=0,
            column=0,
            sticky=tk.W,
            padx=5,
            pady=5
        )

        self.entrada_funcion = self.crear_entry_redondeado(
            frame_entrada,
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
            frame_entrada,
            text="xl:",
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            font=("Arial", 10)
        ).grid(
            row=1,
            column=0,
            sticky=tk.W,
            padx=5,
            pady=5
        )

        self.entrada_xl = self.crear_entry_redondeado(
            frame_entrada,
            width=15
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
            frame_entrada,
            text="xu:",
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            font=("Arial", 10)
        ).grid(
            row=1,
            column=2,
            sticky=tk.W,
            padx=5,
            pady=5
        )

        self.entrada_xu = self.crear_entry_redondeado(
            frame_entrada,
            width=15
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
            frame_entrada,
            text="Tolerancia:",
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            font=("Arial", 10)
        ).grid(
            row=2,
            column=0,
            sticky=tk.W,
            padx=5,
            pady=5
        )

        self.entrada_tolerancia = self.crear_entry_redondeado(
            frame_entrada,
            width=15
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
        # ITERACIONES
        # =====================================================

        tk.Label(
            frame_entrada,
            text="Máx. iteraciones:",
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            font=("Arial", 10)
        ).grid(
            row=2,
            column=2,
            sticky=tk.W,
            padx=5,
            pady=5
        )

        self.entrada_iteraciones = self.crear_entry_redondeado(
            frame_entrada,
            width=15
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
            frame_entrada,
            bg=self.COLOR_PANEL
        )

        frame_botones.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=(10, 3)
        )

        # -----------------------------------------------------
        # BOTÓN CALCULAR
        # -----------------------------------------------------

        self.boton_calcular = tk.Button(
            frame_botones,
            text="CALCULAR",
            command=self.calcular,
            width=14,
            bg=self.COLOR_BOTON,
            fg=self.COLOR_BLANCO,
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2,
            activebackground=self.COLOR_HOVER,
            activeforeground=self.COLOR_BLANCO,
            cursor="hand2"
        )

        self.boton_calcular.pack(
            side=tk.LEFT,
            padx=5
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

        # -----------------------------------------------------
        # BOTÓN LIMPIAR
        # -----------------------------------------------------

        self.boton_limpiar = tk.Button(
            frame_botones,
            text="LIMPIAR",
            command=self.limpiar,
            width=14,
            bg=self.COLOR_BORDE,
            fg=self.COLOR_BLANCO,
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2,
            activebackground=self.COLOR_HOVER,
            activeforeground=self.COLOR_BLANCO,
            cursor="hand2"
        )

        self.boton_limpiar.pack(
            side=tk.LEFT,
            padx=5
        )

        self.boton_limpiar.bind(
            "<Enter>",
            lambda e: self.boton_limpiar.config(
                bg=self.COLOR_HOVER
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
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRINCIPAL
        )

        self.label_resultado.pack(
            pady=5
        )

        # =====================================================
        # TABLA
        # =====================================================

        frame_tabla = tk.LabelFrame(
            panel_izquierdo,
            text="Tabla de Iteraciones",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            padx=8,
            pady=8,
            relief=tk.GROOVE,
            bd=2
        )

        frame_tabla.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=5
        )

        # =====================================================
        # FRAME SCROLL
        # =====================================================

        frame_tree = tk.Frame(
            frame_tabla,
            bg=self.COLOR_PANEL
        )

        frame_tree.pack(
            fill=tk.BOTH,
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

        # =====================================================
        # SCROLLBARS
        # =====================================================

        scrollbar_vertical = ttk.Scrollbar(
            frame_tree,
            orient=tk.VERTICAL,
            style="Rosa.Vertical.TScrollbar"
        )

        scrollbar_horizontal = ttk.Scrollbar(
            frame_tree,
            orient=tk.HORIZONTAL,
            style="Rosa.Horizontal.TScrollbar"
        )

        # =====================================================
        # TABLA
        # =====================================================

        self.tabla = ttk.Treeview(
            frame_tree,
            columns=columnas,
            show="headings",
            style="Rosa.Treeview",
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set
        )

        scrollbar_vertical.config(
            command=self.tabla.yview
        )

        scrollbar_horizontal.config(
            command=self.tabla.xview
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
        # ENCABEZADOS
        # =====================================================

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
            "xl": 85,
            "xu": 85,
            "xr": 85,
            "fxl": 90,
            "fxu": 90,
            "fxr": 90,
            "producto": 105,
            "error1": 85,
            "error2": 85,
            "error3": 85
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
        # ESTADO
        # =====================================================

        self.estado_label = tk.Label(
            panel_izquierdo,
            text="Listo",
            font=("Arial", 9),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRINCIPAL
        )

        self.estado_label.pack(
            pady=3
        )

        # =====================================================
        # PANEL DERECHO
        # =====================================================

        # -----------------------------------------------------
        # GRÁFICA FUNCIÓN
        # -----------------------------------------------------

        frame_grafica_funcion = tk.LabelFrame(
            panel_derecho,
            text="Gráfica de f(x)",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            padx=5,
            pady=5,
            relief=tk.GROOVE,
            bd=2
        )

        frame_grafica_funcion.pack(
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=(5, 3)
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
            master=frame_grafica_funcion
        )

        self.canvas_funcion.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True
        )

        # -----------------------------------------------------
        # GRÁFICA ERROR
        # -----------------------------------------------------

        frame_grafica_error = tk.LabelFrame(
            panel_derecho,
            text="Gráfica Error 1 (|xu - xr|)",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_PRINCIPAL,
            padx=5,
            pady=5,
            relief=tk.GROOVE,
            bd=2
        )

        frame_grafica_error.pack(
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=(3, 5)
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
            master=frame_grafica_error
        )

        self.canvas_error.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True
        )

        # =====================================================
        # GRÁFICAS INICIALES
        # =====================================================

        self.configurar_grafica_vacia()

    # =========================================================
    # CREAR FUNCIÓN
    # =========================================================

    def crear_funcion(self, expresion):

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

            self.estado_label.config(
                text="Calculando..."
            )

            self.root.update()

            # -------------------------------------------------
            # OBTENER DATOS
            # -------------------------------------------------

            expresion = self.entrada_funcion.get().strip()

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

            if tolerancia <= 0:

                raise ValueError(
                    "La tolerancia debe ser mayor que 0."
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

            # Comprobar función
            f(xl)
            f(xu)

            # -------------------------------------------------
            # EJECUTAR BISECCIÓN
            # -------------------------------------------------

            resultado = biseccion(
                f,
                xl,
                xu,
                tolerancia,
                max_iter
            )

            # -------------------------------------------------
            # RESULTADOS
            # -------------------------------------------------

            raiz = resultado["raiz"]
            iteraciones = resultado["iteraciones"]
            error = resultado["error"]

            # -------------------------------------------------
            # MOSTRAR RESULTADO
            # -------------------------------------------------

            self.label_resultado.config(
                text=(
                    f"Raíz: {raiz:.8f}"
                    f"     |     Iteraciones: {iteraciones}"
                    f"     |     Error: {error:.8f}"
                ),
                fg=self.COLOR_OSCURO
            )

            # -------------------------------------------------
            # MOSTRAR TABLA
            # -------------------------------------------------

            self.mostrar_tabla(
                resultado["tabla"]
            )

            # -------------------------------------------------
            # GRÁFICA FUNCIÓN
            # -------------------------------------------------

            self.graficar_funcion(
                f,
                xl,
                xu,
                raiz
            )

            # -------------------------------------------------
            # GRÁFICA ERROR
            # -------------------------------------------------

            self.graficar_error(
                resultado["tabla"]
            )

            # -------------------------------------------------
            # ESTADO
            # -------------------------------------------------

            self.estado_label.config(
                text="Cálculo realizado correctamente."
            )

        except ValueError as error:

            self.estado_label.config(
                text=f"Error: {error}"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

        except ZeroDivisionError:

            self.estado_label.config(
                text="Error: división entre cero."
            )

            messagebox.showerror(
                "Error",
                "La función produjo una división entre cero."
            )

        except Exception as error:

            self.estado_label.config(
                text=f"Error: {error}"
            )

            messagebox.showerror(
                "Error",
                f"No se pudo procesar la función.\n\n{error}"
            )

    # =========================================================
    # MOSTRAR TABLA
    # =========================================================

    def mostrar_tabla(self, datos):

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
                    f"{fila['xl']:.8f}",
                    f"{fila['xu']:.8f}",
                    f"{fila['xr']:.8f}",
                    f"{fila['fxl']:.8f}",
                    f"{fila['fxu']:.8f}",
                    f"{fila['fxr']:.8f}",
                    f"{fila['producto']:.8f}",
                    f"{fila['error1']:.8f}",
                    f"{fila['error2']:.8f}",
                    f"{fila['error3']:.8f}"
                )
            )

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

        # -----------------------------------------------------
        # FONDO
        # -----------------------------------------------------

        self.ax_funcion.set_facecolor(
            self.COLOR_ENTRADA
        )

        self.figura_funcion.patch.set_facecolor(
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
                    isinstance(y, (int, float))
                    and math.isfinite(y)
                ):

                    valores_x.append(x)
                    valores_y.append(y)

            except Exception:

                pass

        # -----------------------------------------------------
        # FUNCIÓN
        # -----------------------------------------------------

        if valores_x:

            self.ax_funcion.plot(
                valores_x,
                valores_y,
                linewidth=2,
                color=self.COLOR_BOTON,
                label="f(x)"
            )

        # -----------------------------------------------------
        # EJE X
        # -----------------------------------------------------

        self.ax_funcion.axhline(
            0,
            linewidth=1,
            color=self.COLOR_PRINCIPAL
        )

        # -----------------------------------------------------
        # RAÍZ
        # -----------------------------------------------------

        self.ax_funcion.scatter(
            [raiz],
            [0],
            s=60,
            zorder=5,
            color=self.COLOR_OSCURO,
            label=f"Raíz = {raiz:.6f}"
        )

        # -----------------------------------------------------
        # INTERVALO
        # -----------------------------------------------------

        self.ax_funcion.axvline(
            xl,
            linestyle="--",
            alpha=0.5,
            color=self.COLOR_BORDE
        )

        self.ax_funcion.axvline(
            xu,
            linestyle="--",
            alpha=0.5,
            color=self.COLOR_BORDE
        )

        # -----------------------------------------------------
        # TEXTOS
        # -----------------------------------------------------

        self.ax_funcion.set_xlabel(
            "x",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.set_ylabel(
            "f(x)",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.set_title(
            "Función y raíz",
            color=self.COLOR_PRINCIPAL
        )

        # -----------------------------------------------------
        # EJES
        # -----------------------------------------------------

        self.ax_funcion.tick_params(
            colors=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.grid(
            True,
            alpha=0.25,
            color=self.COLOR_BORDE
        )

        # -----------------------------------------------------
        # LEYENDA
        # -----------------------------------------------------

        if valores_x:

            self.ax_funcion.legend(
                facecolor=self.COLOR_PANEL,
                edgecolor=self.COLOR_BORDE,
                labelcolor=self.COLOR_PRINCIPAL
            )

        # -----------------------------------------------------
        # BORDES
        # -----------------------------------------------------

        for borde in self.ax_funcion.spines.values():

            borde.set_color(
                self.COLOR_BORDE
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

        # -----------------------------------------------------
        # FONDO
        # -----------------------------------------------------

        self.ax_error.set_facecolor(
            self.COLOR_ENTRADA
        )

        self.figura_error.patch.set_facecolor(
            self.COLOR_PANEL
        )

        iteraciones = []
        errores = []

        # -----------------------------------------------------
        # OBTENER ERROR 1
        # -----------------------------------------------------

        for fila in datos:

            iteraciones.append(
                fila["iteracion"]
            )

            errores.append(
                fila["error1"]
            )

        # -----------------------------------------------------
        # DIBUJAR
        # -----------------------------------------------------

        if len(iteraciones) > 0:

            self.ax_error.plot(
                iteraciones,
                errores,
                marker="o",
                markersize=3,
                linewidth=1.5,
                color=self.COLOR_BOTON
            )

        # -----------------------------------------------------
        # CONFIGURACIÓN
        # -----------------------------------------------------

        self.ax_error.set_xlabel(
            "Iteración",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.set_ylabel(
            "Error",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.set_title(
            "Error por iteración",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.tick_params(
            colors=self.COLOR_PRINCIPAL
        )

        self.ax_error.grid(
            True,
            alpha=0.25,
            color=self.COLOR_BORDE
        )

        # -----------------------------------------------------
        # BORDES
        # -----------------------------------------------------

        for borde in self.ax_error.spines.values():

            borde.set_color(
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

        self.ax_funcion.set_facecolor(
            self.COLOR_ENTRADA
        )

        self.figura_funcion.patch.set_facecolor(
            self.COLOR_PANEL
        )

        self.ax_funcion.set_title(
            "Función y raíz",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.set_xlabel(
            "x",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.set_ylabel(
            "f(x)",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.tick_params(
            colors=self.COLOR_PRINCIPAL
        )

        self.ax_funcion.grid(
            True,
            alpha=0.25,
            color=self.COLOR_BORDE
        )

        for borde in self.ax_funcion.spines.values():

            borde.set_color(
                self.COLOR_BORDE
            )

        self.figura_funcion.tight_layout(
            pad=1
        )

        self.canvas_funcion.draw()

        # =====================================================
        # ERROR
        # =====================================================

        self.ax_error.set_facecolor(
            self.COLOR_ENTRADA
        )

        self.figura_error.patch.set_facecolor(
            self.COLOR_PANEL
        )

        self.ax_error.set_title(
            "Error por iteración",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.set_xlabel(
            "Iteración",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.set_ylabel(
            "Error",
            color=self.COLOR_PRINCIPAL
        )

        self.ax_error.tick_params(
            colors=self.COLOR_PRINCIPAL
        )

        self.ax_error.grid(
            True,
            alpha=0.25,
            color=self.COLOR_BORDE
        )

        for borde in self.ax_error.spines.values():

            borde.set_color(
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
        # LIMPIAR ENTRADAS
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
        # LIMPIAR TABLA
        # -----------------------------------------------------

        for item in self.tabla.get_children():

            self.tabla.delete(
                item
            )

        # -----------------------------------------------------
        # LIMPIAR RESULTADO
        # -----------------------------------------------------

        self.label_resultado.config(
            text=(
                "Raíz: --     |     "
                "Iteraciones: --     |     "
                "Error: --"
            ),
            fg=self.COLOR_PRINCIPAL
        )

        # -----------------------------------------------------
        # LIMPIAR ESTADO
        # -----------------------------------------------------

        self.estado_label.config(
            text="Listo"
        )

        # -----------------------------------------------------
        # LIMPIAR GRÁFICAS
        # -----------------------------------------------------

        self.ax_funcion.clear()
        self.ax_error.clear()

        self.configurar_grafica_vacia()

