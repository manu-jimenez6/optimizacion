# metodos/interpolacion_cuadratica.py

def interpolacion_cuadratica(
    f,
    x1,
    x2,
    x3,
    tipo="Mínimo",
    tolerancia=0.001,
    max_iter=100
):

    tabla = []


    puntos = sorted([x1, x2, x3])

    x1 = puntos[0]
    x2 = puntos[1]
    x3 = puntos[2]



    for i in range(1, max_iter + 1):

        fx1 = f(x1)
        fx2 = f(x2)
        fx3 = f(x3)



        denominador = (
            2 * fx1 * (x2 - x3)
            + 2 * fx2 * (x3 - x1)
            + 2 * fx3 * (x1 - x2)
        )

        if abs(denominador) < 1e-14:

            raise ZeroDivisionError(
                "No se puede calcular la interpolación cuadrática "
                "porque el denominador es cero o muy cercano a cero."
            )


        numerador = (
            fx1 * (x2 ** 2 - x3 ** 2)
            + fx2 * (x3 ** 2 - x1 ** 2)
            + fx3 * (x1 ** 2 - x2 ** 2)
        )


        xr = numerador / denominador

        fxr = f(xr)


        error = abs(xr - x2)

        if abs(xr) > 1e-14:

            error_relativo = abs(
                (xr - x2) / xr
            )

        else:

            error_relativo = error

        error_porcentual = error_relativo * 100



        tabla.append({

            "iteracion": i,

            "x1": x1,
            "x2": x2,
            "x3": x3,

            "fx1": fx1,
            "fx2": fx2,
            "fx3": fx3,

            "xr": xr,
            "fxr": fxr,

            "error": error,
            "error_relativo": error_relativo,
            "error_porcentual": error_porcentual
        })


        if error <= tolerancia:

            x2 = xr
            break


        puntos_nuevos = [
            (x1, fx1),
            (x2, fx2),
            (x3, fx3),
            (xr, fxr)
        ]



        puntos_nuevos.sort(
            key=lambda punto: punto[0]
        )


        if tipo == "Mínimo":


            puntos_nuevos.sort(
                key=lambda punto: punto[1]
            )

        elif tipo == "Máximo":



            puntos_nuevos.sort(
                key=lambda punto: punto[1],
                reverse=True
            )

        else:

            raise ValueError(
                "El tipo debe ser 'Mínimo' o 'Máximo'."
            )


        mejor = puntos_nuevos[0]

        x_mejor = mejor[0]



        candidatos = sorted(
            puntos_nuevos,
            key=lambda punto: punto[0]
        )

        indice_mejor = None

        for j, punto in enumerate(candidatos):

            if abs(
                punto[0] - x_mejor
            ) < 1e-14:

                indice_mejor = j

                break


        if (
            indice_mejor is not None
            and indice_mejor > 0
            and indice_mejor < len(candidatos) - 1
        ):

            seleccionados = [
                candidatos[indice_mejor - 1],
                candidatos[indice_mejor],
                candidatos[indice_mejor + 1]
            ]

        else:


            if len(candidatos) >= 3:

                seleccionados = candidatos[:3]

            else:

                seleccionados = candidatos

        seleccionados.sort(
            key=lambda punto: punto[0]
        )

        x1 = seleccionados[0][0]
        x2 = seleccionados[1][0]
        x3 = seleccionados[2][0]

    xr_final = tabla[-1]["xr"]

    valor_final = f(xr_final)

    return {

        "x_optimo": xr_final,

        "valor": valor_final,

        "iteraciones": len(tabla),

        "error": tabla[-1]["error"],

        "tabla": tabla
    }