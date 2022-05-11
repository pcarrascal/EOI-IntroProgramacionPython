def ClasificaGenero(dataset, _len=100):

    """

    Función que calcula el % de hombres y mujeres

    El dataset debe ser una lista que contiene "F" para mujeres y "M" para hombres (de tamaño 100 por defecto)

    Devuelve False si el dato no es correcto (e imprime el motivo)

    """

    # Check Type

    if type(dataset) != list:

        print("Dataset is not a list")

        return False



    # Check Len

    if len(dataset) != _len:

        print("Wrong dataset size (must be) 100")

        return False



    uniq_values = set(dataset)

    if uniq_values != {"F", "M"}:

        print("Values must")

        return False



    n_hombres = len([gender for gender in dataset if gender == "M"])

    p_hombres = n_hombres / _len * 100

    p_mujeres = 100 - p_hombres

    print(f"Hay {p_hombres}% de hombres y {p_mujeres}% mujeres")

    if p_hombres > 50:

        print("Hay más hombres")

    elif p_hombres < 50:

        print("Hay más mujeres")

    else:

        print("Hay igualdad")

    return True


def TestHombresMujeres():



    stars = "***********************"



    print(stars)

    print("CASO aleatorio")

    datasetHombresMujeres = ["M" if random.randint(0, 1) else "F" for _ in range(100)]

    ClasificaGenero(datasetHombresMujeres)



    print(stars)

    print("CASO de Igualdad")

    datasetHombresMujeres = list("M" * 50 + "F" * 50)

    ClasificaGenero(datasetHombresMujeres)



    print(stars)

    print("CASO Dataset No es Lista")

    ClasificaGenero(4)



    print(stars)

    print("CASO Dataset Corto")

    ClasificaGenero(["F", "M"])



    print(stars)

    print("CASO Dataset no contiene F/M")

    ClasificaGenero(range(100))



    print(stars)

#Presione Mayús + Tabulación para navegar por el historial de chat.
