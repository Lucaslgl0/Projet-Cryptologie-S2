class Nombres(object):
    def __init__(self):
        self = []

    def NombreToListe(chiffre):
        # Le but de ce programme cera d'affecté tous les chiffres d'un nombre dans chaque élément de sa liste associée
        new = []
        E = 1  # Notre exposant qui va passer des dizaines, aux centaines, aux milliers, ...
        while chiffre % E != chiffre:
            E *= 10
            new = [(chiffre % E) // (E / 10)] + new
        return new

    def change_compteur(L):  # Notre fonction retenue
        if len(L) == 0:
            return [1]

        else:
            if L[-1] != 9:
                L[-1] += 1
                return L
            else:
                L[-1] = 0
            return change_compteur(L[:-1]) + [L[-1]]

    def addition(L1, L2):
        if len(L1) < len(L2):
            L1, L2 = L2, L1
        taille1 = len(L1)
        taille2 = len(L2) 
        new = []
        supplementaire = []
        min_taille = min(taille1, taille2)
        compteur = 0

        for i in range(min_taille):
            if L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + compteur < 10:
                new = [L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + compteur] + new
                compteur = 0
            else:
                new = [L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + compteur - 10] + new
                compteur = 1
        if taille1 == taille2 and compteur == 1:
            new = [1] + new
            compteur = 0
        if taille1 != taille2:
            if compteur == 1:
                supplementaire = change_compteur(L1[: (taille1 - taille2)])
            else:
                supplementaire = L1[: (taille1 - taille2)]
            new = supplementaire + new
        return new

    def multiplication(L1, L2):
        resultat = [0]
        if len(L1) == len(L2):
            L1 = [0] + L1
        L1, L2 = max(L1, L2, key=len), min(L1, L2, key=len)
        for i in range(len(L2)):
            for j in range(len(L1)):
                resultat = addition(
                    resultat,
                    (
                        NombreToListe(L1[len(L1) - j - 1] * L2[len(L2) - i - 1])
                        + [0 for i in range(i + j)]
                    ),
                )
        return resultat

    def EstPlusGrand(L1, L2):
        if len(L1) < len(L2):
            L1 = [0 for i in range(len(L2) - len(L1))] + L1
        else:
            L2 = [0 for i in range(len(L1) - len(L2))] + L2
        for i in range(len(L1)):
            if L1[i] == L2[i]:
                continue
            elif L1[i] < L2[i]:
                return False
            else:
                return True
        return False

    def soustraction(L1, L2):
        if EstPlusGrand(L2, L1):
            L1, L2 = L2, L1
        taille1 = len(L1)
        taille2 = len(L2)
        new = []
        compteur = 0
        for i in range(taille2):
            L2[taille2 - 1 - i] += compteur
            if L1[taille1 - 1 - i] - L2[taille2 - 1 - i] < 0:  # attention out of range
                compteur = 1
                new = [10 + L1[taille1 - 1 - i] - L2[taille2 - 1 - i]] + new
            else:
                new = [L1[taille1 - 1 - i] - L2[taille2 - 1 - i]] + new
                compteur = 0
        if compteur == 1:
            L1[taille1 - taille2 - 1] -= 1
        new = L1[: (taille1 - taille2)] + new
        return new

    def division(L1, L2):
        i = 0
        stop = 0
        while stop == 0:
            if EstPlusGrand(multiplication(L2, NombreToListe(i + 1)), L1):
                return [
                    NombreToListe(i),
                    soustraction(L1, multiplication(L2, NombreToListe(i))),
                ]
            i += 1

    def exposant(L1, x):
        resultat = [1]
        while x != [0]:
            x = soustraction(x, [1])
            resultat = multiplication(resultat, L1)
        return resultat
