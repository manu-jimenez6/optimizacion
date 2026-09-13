# metodos/busqueda_aleatoria.py

import random


def busqueda_aleatoria(
    funcion,
    xl,
    xu,
    yl,
    yu,
    max_iter
):


    maximo = float("-inf")

    mejor_x = None
    mejor_y = None


    tabla = []


    for i in range(1, max_iter + 1):

        x = xl + (xu - xl) * random.random()

        y = yl + (yu - yl) * random.random()


        fx = funcion(x, y)


        if fx > maximo:

            maximo = fx

            mejor_x = x

            mejor_y = y


        tabla.append({

            "iteracion": i,

            "x": mejor_x,

            "y": mejor_y,

            "fx": maximo

        })


    return {

        "x_optimo": mejor_x,

        "y_optimo": mejor_y,

        "valor": maximo,

        "iteraciones": max_iter,

        "tabla": tabla

    }