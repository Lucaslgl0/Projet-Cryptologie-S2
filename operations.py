from copy import *


def supprime_zéros(liste):
    for i in range(len(liste)):
        if liste[0] == 0:
            del liste[0]
        else:
            break


def NombreToListe(chiffre):
    """Transformation d'un nombre en une liste

    Fonction utile pour les nombres potentiellement très grands que python ne pourra pas traiter simplement.
    Cela nous permet de créer une liste qui représentera un nombre où chaque case de la liste représente un chiffre composant le nombre.
    L'unité sera la dernière case, le chiffre des dizaines sera l'avant-dernière, etc

    Args :
        chiffre (int): sera le nombre en entier qui sera, dans notre cas, très grand

    Returns :
        list : Le nombre converti en liste comme décrit plus haut
    """
    new = []
    E = 1
    while chiffre % E != chiffre:
        E *= 10
        new = [(chiffre % E) // (E / 10)] + new
    return new


def soustraction(
    L1, L2, base=10
):  ## les test marchent j'espere que tout marche pour la base 2 j'ai eu peur de devoir passer par le complementaire
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
            new = [base + L1[taille1 - 1 - i] - L2[taille2 - 1 - i]] + new
        else:
            new = [L1[taille1 - 1 - i] - L2[taille2 - 1 - i]] + new
            compteur = 0
    if compteur == 1:
        L1[taille1 - taille2 - 1] -= 1
    new = L1[: (taille1 - taille2)] + new
    supprime_zéros(new)  ##important pour la base 2
    return new


def addition(L1, L2, base=10):
    if len(L1) < len(L2):
        L1, L2 = L2, L1
    taille1 = len(L1)
    taille2 = len(L2)
    new = []
    supplementaire = []
    min_taille = min(taille1, taille2)
    retenue = 0

    for i in range(min_taille):
        if L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + retenue < base:
            new = [L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + retenue] + new
            retenue = 0
        else:
            new = [L1[taille1 - 1 - i] + L2[taille2 - 1 - i] + retenue - base] + new
            retenue = 1
    if taille1 == taille2 and retenue == 1:
        new = [1] + new
        retenue = 0
    if taille1 != taille2:
        if retenue == 1:
            supplementaire = change_retenue(L1[: (taille1 - taille2)], base)
        else:
            supplementaire = L1[: (taille1 - taille2)]
        new = supplementaire + new
    return new


def change_retenue(L, base=10):  # Notre fonction retenue
    if len(L) == 0:
        return [1]

    else:
        print(L[-1])
        if L[-1] != (base - 1):
            L[-1] += 1
            return L
        else:
            L[-1] = 0
        return change_retenue(L[:-1], base) + [L[-1]]  ##NE PAS OUBLIER LA BASE!!


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


def expodentation(L1, exp, mod):
    liste_exposant = decomposition(exp)
    res = [1]
    for i in range(len(liste_exposant)):
        mult = exposant(L1, liste_exposant[0])
        l2 = modulo(mult, mod)
        res = modulo(multiplication(res, l2), mod)
    return res


def listpremiers(n):
    k = []
    i = 2
    while len(k) != n + 1:
        y = i
        t = False
        for element in k:
            if y % element == 0:
                t = True
        if not t:
            k += [i]

        i += 1
    return k


def listedepremier(n):
    res = []
    x = listpremiers(n)
    for element in x:
        res += [NombreToListe(element)]
    return res


def division(l1, l2):
    L1 = deepcopy(l1)
    L2 = deepcopy(l2)
    Q = []
    R = []
    while EstPlusGrand(L1, L2):
        decoupage = L1[: ((len(L2) + 1))]  ##prog marche pas pour liste de meme taille

        decoupage = supprime_zéros(decoupage)
        print("decpooupa", decoupage)

        i = [1]
        while EstPlusGrand(decoupage, multiplication(i, L2)):

            i = addition(i, [1])

        newdecoupage = soustraction(decoupage, multiplication(L2, soustraction(i, [1])))

        for j in range(
            len(L2) + 1
        ):  ##voila ou etaos ma faute depuis le debut envie de ma suisider fort putin de +1 pour 2h de taff yes
            L1.pop(0)
        newdecoupage = supprime_zéros(newdecoupage)
        L1 = newdecoupage + L1
        supprime_zéros(L1)

        Q = Q + soustraction(i, [1])
        print(Q)

    reste = soustraction(l1, multiplication(Q, l2))
    supprime_zéros(reste)
    if reste == l2:
        Q = addition(Q, [1])
        reste = [0]

    return Q, reste


def est_premier(L1):
    i = [1]
    while EstPlusGrand(L1, i):
        x, y = division(L1, i)
        if y == 0:
            return False
        addition(i, [1])
    return True


def decomposition(l1):
    L1 = deepcopy(l1)
    liste_de_premier = listedepremier(100)
    decomposition1 = []
    while not L1 in (liste_de_premier):
        for element in liste_de_premier:

            x, y = division(L1, element)

            if y == [0]:

                L1 = x
                L1 = supprime_zéros(L1)
                decomposition1 += [element]
                break
    decomposition1 += [L1]

    return decomposition1


print(decomposition([2, 0]))


def exposant(L1, x):
    resultat = [1]
    while x != [0]:
        x = soustraction(x, [1])
        resultat = multiplication(resultat, L1)
    return resultat


def modulo(L1, modulo):
    x, reste = division(L1, modulo)
    return reste


def maximum(L1):
    m = L1[0]
    for element in L1:
        if EstPlusGrand(element, m):
            m = element
    return m
