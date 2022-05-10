from operations_liste import (
    nombre_vers_liste,
    soustraction,
    multiplication,
    euclide_etendue,
    PGCD,
)


# Choix des nombres premiers et de l'exposant

nombre_premier1 = nombre_vers_liste(10000005143)
nombre_premier2 = nombre_vers_liste(10000018097)
exposant = [6,5,5,3,7]

# Création des cles

phi_n = multiplication(
    soustraction(nombre_premier1, [1]), soustraction(nombre_premier2, [1])
)
if PGCD(exposant, phi_n) != [1]:
    print(
        "e n'est pas premier avec phi_n il faut changer soit l'exposant, soit les nombres premiers"
    )
n = multiplication(nombre_premier1, nombre_premier2)
d = euclide_etendue(exposant, phi_n)[1]

print("!!!!:créations des cles terminée:!!!!")
