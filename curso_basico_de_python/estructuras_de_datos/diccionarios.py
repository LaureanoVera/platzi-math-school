laureano = {
    "nombres": ("Laureano", "Ivan", "Gerardo"),
    "apellido": "Vera",
    "nacimiento": "17/12/2002",
    "nacionalidad": "Argentina",
    "DNI": 44586608,
}

print(laureano["nombres"][0])

for key in laureano.keys():
    print(key)

for value in laureano.values():
    print(value)

for item in laureano.items():
    print(item)
