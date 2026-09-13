# metodos/falsa_posicion.py

def falsa_posicion(f, xl, xu, tolerancia, max_iter):


    fxl = f(xl)
    fxu = f(xu)

    if fxl * fxu > 0:
        raise ValueError(
            "El intervalo no encierra una raíz. "
            "Debe cumplirse que f(xl) · f(xu) < 0."
        )


    tabla = []

    xr_anterior = None

    error = float("inf")


    for i in range(max_iter):


        denominador = fxl - fxu

        if denominador == 0:
            raise ZeroDivisionError(
                "No se puede calcular falsa posición porque "
                "f(xl) - f(xu) = 0."
            )

        xr = xu - (
            fxu * (xl - xu)
        ) / denominador

        fxr = f(xr)


        if xr_anterior is None:

            error1 = abs(xu - xl)
            error2 = abs(xu - xl) / 2
            error3 = abs(xu - xl) / 2

        else:

            error1 = abs(xr - xr_anterior)

            error2 = abs(
                (xr - xr_anterior) / xr
            ) if xr != 0 else error1

            error3 = (
                abs(xr - xr_anterior) / abs(xr)
            ) * 100 if xr != 0 else error1

        error = error1


        producto = fxl * fxr


        tabla.append({
            "iteracion": i,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "fxl": fxl,
            "fxu": fxu,
            "fxr": fxr,
            "producto": producto,
            "error1": error1,
            "error2": error2,
            "error3": error3
        })

        if fxr == 0:
            error = 0
            break

        if tolerancia > 0 and xr_anterior is not None:
            if error1 <= tolerancia:
                break


        if xr_anterior is not None:

            if error1 <= tolerancia:

                break


        if fxl * fxr < 0:

            xu = xr
            fxu = fxr

        elif fxr * fxu < 0:

            xl = xr
            fxl = fxr

        else:


            break


        xr_anterior = xr


    return {
        "raiz": xr,
        "iteraciones": len(tabla),
        "error": error,
        "tabla": tabla
    }