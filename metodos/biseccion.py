# metodos/biseccion.py

def biseccion(f, xl, xu, tolerancia=0.001, max_iter=100):


    fxl = f(xl)
    fxu = f(xu)

    if fxl * fxu > 0:

        raise ValueError(
            "El intervalo no encierra una raíz.\n"
            "Debe cumplirse que f(xl) * f(xu) < 0."
        )

    tabla = []

    for i in range(1, max_iter + 1):


        xr = (xl + xu) / 2


        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)

        producto = fxl * fxr

        error1 = abs(xu - xr)

        error2 = abs(xl - xr)

        error3 = abs(xu - xl)


        tabla.append({

            "iteracion": i, "xu": xu, "xl": xl, "xr": xr, "fxu": fxu, "fxl": fxl, "fxr": fxr, "producto": producto, "error1": error1, "error2": error2, "error3": error3
        })


        if fxr == 0:

            return {
                "raiz": xr, "iteraciones": i, "error": 0, "tabla": tabla 
            }

        if error3 < tolerancia:

            return {
                "raiz": xr, "iteraciones": i, "error": error3, "tabla": tabla
            }


        if producto < 0:

            xu = xr

        elif producto > 0:


            xl = xr

        else:

            return {
                "raiz": xr, "iteraciones": i, "error": 0, "tabla": tabla 
            }


    return {
        "raiz": xr, "iteraciones": max_iter, "error": error3, "tabla": tabla
    }