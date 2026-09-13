# metodos/razon_dorada.py

def razon_dorada(
    funcion,
    xl,
    xu,
    tolerancia,
    max_iter,
    tipo="Máximo"
):


    if tipo not in ("Mínimo", "Máximo", "Ambos"):
        raise ValueError("El tipo de búsqueda no es válido.")

    if xl >= xu:
        raise ValueError(
            "El límite inferior (xl) debe ser menor que "
            "el límite superior (xu)."
        )

    if tolerancia <= 0:
        raise ValueError(
            "La tolerancia debe ser mayor que cero."
        )

    if max_iter <= 0:
        raise ValueError(
            "El número máximo de iteraciones debe ser mayor que cero."
        )


    phi = 0.6180339887


    def calcular_extremo(
        xl_inicial,
        xu_inicial,
        buscar_maximo
    ):

        xl = xl_inicial
        xu = xu_inicial


        x1 = xl + (1 - phi) * (xu - xl)
        x2 = xl + phi * (xu - xl)

        fx1 = funcion(x1)
        fx2 = funcion(x2)


        xr_anterior = None
        error = 100.0

        iteracion = 1

        tabla = []


        while (
            error > tolerancia
            and iteracion <= max_iter
        ):


            xr = (xl + xu) / 2
            fxr = funcion(xr)


            if xr_anterior is not None:

                if xr != 0:
                    error = abs(
                        (xr - xr_anterior) / xr
                    ) * 100

                else:
                    error = abs(
                        xr - xr_anterior
                    ) * 100


            tabla.append({
                "iteracion": iteracion,
                "xl": xl,
                "xu": xu,
                "x1": x1,
                "x2": x2,
                "fx1": fx1,
                "fx2": fx2,
                "xr": xr,
                "fxr": fxr,
                "error": error
            })


            if buscar_maximo:

                if fx1 > fx2:

                    xu = x2

                    x2 = x1
                    fx2 = fx1

                    x1 = xl + (1 - phi) * (xu - xl)
                    fx1 = funcion(x1)

                else:


                    xl = x1

                    x1 = x2
                    fx1 = fx2

                    x2 = xl + phi * (xu - xl)
                    fx2 = funcion(x2)


            else:

                if fx1 < fx2:


                    xu = x2

                    x2 = x1
                    fx2 = fx1

                    x1 = xl + (1 - phi) * (xu - xl)
                    fx1 = funcion(x1)

                else:


                    xl = x1

                    x1 = x2
                    fx1 = fx2

                    x2 = xl + phi * (xu - xl)
                    fx2 = funcion(x2)


            xr_anterior = xr

            iteracion += 1


        xr = (xl + xu) / 2
        fxr = funcion(xr)

        return {
            "x_optimo": xr,
            "valor": fxr,
            "iteraciones": len(tabla),
            "error": error,
            "tabla": tabla
        }


    if tipo == "Mínimo":

        return calcular_extremo(
            xl,
            xu,
            False
        )


    if tipo == "Máximo":

        return calcular_extremo(
            xl,
            xu,
            True
        )


    resultado_minimo = calcular_extremo(
        xl,
        xu,
        False
    )

    resultado_maximo = calcular_extremo(
        xl,
        xu,
        True
    )

    return {
        "minimo": resultado_minimo,
        "maximo": resultado_maximo
    }