from operations_liste import (
    nombre_vers_liste,
    soustraction,
    multiplication,
    euclide_etendue,
    PGCD,
)


# Choix des nombres premiers et de l'exposant

nombre_premier1 = nombre_vers_liste(991)  # 10000005143
nombre_premier2 = nombre_vers_liste(727)  # 10000018097
exposant = [7]

# Création des cles

phi_n = multiplication(
    soustraction(nombre_premier1, [1]), soustraction(nombre_premier2, [1])
)
if PGCD(exposant, phi_n) != [1]:
    print(
        "e n'est pas premier avec phi_n il faut changer soit e soit un nombre premier"
    )
n = multiplication(nombre_premier1, nombre_premier2)
d = euclide_etendue(exposant, phi_n)[1]

print("!!!!:créations des cles terminée:!!!!")
