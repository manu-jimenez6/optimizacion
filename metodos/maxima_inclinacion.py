#metodo de maxima inclinacion

import sympy as sp
import numpy as np


def maxima_inclinacion(
    funcion_str,
    x0,
    y0,
    tolerancia=1e-6,
    max_iter=100
):

    x, y, h = sp.symbols("x y h")

    try:

        f_expr = sp.sympify(
            funcion_str.replace("^", "**")
        )

    except Exception as e:

        raise ValueError(
            f"Función inválida:\n{e}"
        )

    dfx_expr = sp.diff(f_expr, x)
    dfy_expr = sp.diff(f_expr, y)

    f = sp.lambdify(
        (x, y),
        f_expr,
        "numpy"
    )

    tabla = []

    trayectoria = []

    xk = float(x0)
    yk = float(y0)

    error = float("inf")

    for i in range(max_iter):

        gx = float(
            dfx_expr.subs(
                {
                    x: xk,
                    y: yk
                }
            )
        )

        gy = float(
            dfy_expr.subs(
                {
                    x: xk,
                    y: yk
                }
            )
        )

        error = np.sqrt(
            gx**2 + gy**2
        )

        valor_actual = float(
            f(xk, yk)
        )

        trayectoria.append(
            (
                xk,
                yk,
                valor_actual
            )
        )

        if error < tolerancia:

            tabla.append({

                "iteracion": i,

                "x": xk,

                "y": yk,

                "fx": valor_actual,

                "dfx": gx,

                "dfy": gy,

                "h": 0,

                "error": error

            })

            break

        gh = f_expr.subs(
            {
                x: xk + gx * h,
                y: yk + gy * h
            }
        )

        dgh = sp.diff(
            gh,
            h
        )

        candidatos = sp.solve(
            dgh,
            h
        )

        h_opt = None

        mejor_valor = -float(
            "inf"
        )

        for candidato in candidatos:

            try:

                candidato = float(
                    candidato
                )

                valor = float(
                    gh.subs(
                        h,
                        candidato
                    )
                )

                if valor > mejor_valor:

                    mejor_valor = valor

                    h_opt = candidato

            except Exception:

                pass

        if h_opt is None:

            raise ValueError(
                "No se encontró un valor válido para h."
            )

        tabla.append({

            "iteracion": i,

            "x": xk,

            "y": yk,

            "fx": valor_actual,

            "dfx": gx,

            "dfy": gy,

            "h": h_opt,

            "error": error

        })

        xk = xk + gx * h_opt
        yk = yk + gy * h_opt

    valor_final = float(
        f(xk, yk)
    )

    return {

        "x_optimo": xk,

        "y_optimo": yk,

        "valor": valor_final,

        "iteraciones": len(tabla),

        "error": error,

        "tabla": tabla,

        "trayectoria": trayectoria

    }