from random import randint

dataset = list(
        {
            "gender": "F" if randint(0, 1) == 0 else "M",
            "age": randint(0, 120),
        }
        for _ in range(100)
    )

print(dataset)

mujeres_mayores_edad = len(
        [
            person
            for person in dataset
            if person["gender"] == "F" and person["age"] >= 18
        ]
    )
print(f"Número de mujeres mayores de edad: {mujeres_mayores_edad}")

hombres_menores_edad = len(
        [
            person
            for person in dataset
            if person["gender"] == "F" and person["age"] < 18
        ]
    )
print(f"Número de hombres mayores de edad: {hombres_menores_edad}")

hombres_mujeres_menor_edad=len(
        [
            person["age"]
            for person in dataset
        ]
    )
print(f"numero de mujeres mayores de edad:{hombres_menores_edad}")


