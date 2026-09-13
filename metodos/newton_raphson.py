# metodos/newton_raphson.py

import math


def newton_raphson(
    f,
    primera_derivada,
    segunda_derivada,
    x0,
    tolerancia=0.001,
    max_iter=100
):

    tabla = []

    x_actual = x0

    error = float("inf")

    for i in range(max_iter):


        try:
            fx = f(x_actual)
            fpx = primera_derivada(x_actual)
            fppx = segunda_derivada(x_actual)
        except Exception as e:
            raise ValueError(
                f"No se pudo evaluar la función en x = {x_actual:.10f}: {e}"
            )


        if not (
            isinstance(fx, (int, float))
            and isinstance(fpx, (int, float))
            and isinstance(fppx, (int, float))
            and math.isfinite(fx)
            and math.isfinite(fpx)
            and math.isfinite(fppx)
        ):
            raise ValueError(
                f"La función o sus derivadas no devolvieron "
                f"valores numéricos finitos en x = {x_actual:.10f}."
            )


        if abs(fppx) < 1e-10:

            raise ZeroDivisionError(
                f"La segunda derivada es cero o muy cercana a cero "
                f"en x = {x_actual:.10f}."
            )


        x_nuevo = x_actual - fpx / fppx


        if not math.isfinite(x_nuevo) or abs(x_nuevo) > 1e10:

            raise ValueError(
                f"El método divergió en x = {x_actual:.10f}."
            )


        error1 = abs(x_nuevo - x_actual)


        if abs(x_nuevo) > 1e-14:

            error2 = abs((x_nuevo - x_actual) / x_nuevo)

        else:

            error2 = error1


        error3 = error2 * 100

        error = error1


        try:
            fx_nuevo = f(x_nuevo)
            fpx_nuevo = primera_derivada(x_nuevo)
            fppx_nuevo = segunda_derivada(x_nuevo)
        except Exception as e:
            raise ValueError(
                f"No se pudo evaluar la función en x = {x_nuevo:.10f}: {e}"
            )


        tabla.append({

            "iteracion": i,

            "x": x_actual,

            "fx": fx,

            "fpx": fpx,

            "fppx": fppx,

            "xr": x_nuevo,

            "fxr": fx_nuevo,

            "fpxr": fpx_nuevo,

            "error1": error1,

            "error2": error2,

            "error3": error3
        })


        x_actual = x_nuevo


        if abs(fpx_nuevo) <= tolerancia:

            break


    x_critico = x_actual

    valor = f(x_critico)

    segunda_derivada_final = segunda_derivada(x_critico)



    if segunda_derivada_final > 0:

        tipo = "Mínimo"

    elif segunda_derivada_final < 0:

        tipo = "Máximo"

    else:

        tipo = "No determinado"

    return {

        "x_critico": x_critico,

        "valor": valor,

        "tipo": tipo,

        "segunda_derivada": segunda_derivada_final,

        "iteraciones": len(tabla),

        "error": error,

        "tabla": tabla
    }