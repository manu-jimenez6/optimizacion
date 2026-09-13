# metodos/newton.py


def newton(
    f,
    df,
    d2f,
    x0,
    tolerancia,
    max_iter
):


    x_actual = x0

    tabla = []

    error = float("inf")


    for i in range(1, max_iter + 1):


        primera_derivada = df(x_actual)

        segunda_derivada = d2f(x_actual)


        if abs(segunda_derivada) < 1e-15:

            raise ZeroDivisionError(
                "La segunda derivada es cero o demasiado cercana "
                "a cero en x = "
                f"{x_actual:.10f}."
            )


        x_nuevo = (
            x_actual
            - primera_derivada / segunda_derivada
        )


        if not isinstance(x_nuevo, (int, float)):

            raise ValueError(
                "El método produjo un valor no válido."
            )


        error = abs(
            x_nuevo - x_actual
        )


        valor = f(x_nuevo)

        dfx = df(x_nuevo)

        d2fx = d2f(x_nuevo)


        tabla.append({

            "iteracion": i,

            "x": x_nuevo,

            "fx": valor,

            "dfx": dfx,

            "d2fx": d2fx,

            "error": error

        })


        x_actual = x_nuevo


        if error <= tolerancia:

            break


    valor_final = f(x_actual)

    segunda_final = d2f(x_actual)


    if segunda_final > 0:

        tipo_encontrado = "Mínimo"

    elif segunda_final < 0:

        tipo_encontrado = "Máximo"

    else:

        tipo_encontrado = "No determinado"


    return {

        "x_optimo": x_actual,

        "valor": valor_final,

        "iteraciones": len(tabla),

        "error": error,

        "tipo_encontrado": tipo_encontrado,

        "tabla": tabla

    }