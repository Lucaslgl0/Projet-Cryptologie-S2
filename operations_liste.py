from copy import *
from math import *

############################################################################################################################
# [------------------------------------------] DEBUT DE NOS FONCTIONS OUTILS [---------------------------------------------]#
############################################################################################################################


def supprime_zéros(liste):
    """Suppression des zéros à l'avant d'une liste

    Cette fonction modifie la liste en enlevant les zéros inutiles devant.

    Args :
        liste (list) : qui sera notre liste de chiffres

    Returns :
        None
    """
    while True:
        if liste[0] == 0 and len(liste) != 1:
            del liste[0]
        else:
            t = False
            return liste


def nombre_vers_liste(chiffre):
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
    if new == []:
        new = [0]
    return new


def change_retenue(L, base=10):
    """Ajout d'une retenue lors d'une opération

    Cette fonction nous permet de supprimer le problème de retenue sur nos opérations.

    Args :
        L (list): notre liste en entrée sur laquelle sera appliquée la retenue
        base (int): Par défaut 10, permet de changer de base si nous le voulons

    Return :
        None : modifie simplement la liste
    """
    if len(L) == 0:
        return [1]

    else:
        if L[-1] != (base - 1):
            L[-1] += 1
            return L
        else:
            L[-1] = 0
        return change_retenue(L[:-1], base) + [L[-1]]


def est_plus_grand(L1, L2):
    """Permet de comparer deux listes

    Cette fonction vérifie, chiffre par chiffre dans la liste, si notre première liste est plus grande que la seconde.
    Cela va nous être utile par la suite lors de différentes opérations.

    Args :
        L1, L2 (list): nos deux listes à comparer

    Return :
        boolean : rend True si L1 est plus grand ou égal à L2 et False sinon
    """
    L1 = supprime_zéros(L1)
    L2 = supprime_zéros(L2)
    if L1 == L2:
        return True
    if len(L1) < len(L2):
        L1 = [0 for i in range(len(L2) - len(L1))] + L1
    else:
        L2 = [0 for i in range(len(L1) - len(L2))] + L2
    for i in range(len(L1)):
        if L1[i] == L2[i]:
            if i == len(L1) - 1:
                return False
            continue
        elif L1[i] < L2[i]:
            return False
        else:
            return True
    return False


def reconstruit(L):
    new = []
    for i in range(len(L)):
        new.extend(L[i])
    return new


def decoupage(L, taille):
    sub = len(L) / taille  # le nombre de division
    if int(sub) != sub:
        b = taille - (len(L) % taille)  # nombre de 0 à rajouter
        sub = int(sub) + 1
        for i in range(b):
            L = [0] + L
    new = []
    for i in range(0, len(L), taille):  # décomposition dans une liste
        new.append(L[i : i + taille])
    return new


def passage_binaire(l1):
    nombre=""
    for i in l1:
        nombre+=str(int(i))
    res = str(bin(int(nombre)))[2:]
    return nombre_vers_liste(int(res))


############################################################################################################################
# [--------------------------------------------------] FIN DE NOS OUTILS [-------------------------------------------------]#
############################################################################################################################

############################################################################################################################
# [-----------------------------------------] DEBUT DE NOS FONCTIONS OPERATIONS[-------------------------------------------]#
############################################################################################################################


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
            supplementaire = change_retenue(L1[: (taille1 - taille2)])
        else:
            supplementaire = L1[: (taille1 - taille2)]
        new = supplementaire + new
    return new


def soustraction(
    l1, l2, base=10
):  # les test marchent j'espere que tout marche pour la base 2 j'ai eu peur de devoir passer par le complementaire

    L1 = deepcopy(l1)
    L2 = deepcopy(l2)

    if est_plus_grand(L2, L1):
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
    supprime_zéros(new)  # important pour la base 2
    return new


def multiplication(L1, L2, base=10):
    resultat = [0]
    if len(L1) == len(L2):
        L1 = [0] + L1
    L1, L2 = max(L1, L2, key=len), min(L1, L2, key=len)
    for i in range(len(L2)):
        for j in range(len(L1)):
            resultat = addition(
                resultat,
                (
                    nombre_vers_liste(L1[len(L1) - j - 1] * L2[len(L2) - i - 1])
                    + [0 for i in range(i + j)]
                ),
            )
    return resultat


"""
def division(l1, l2):
    L1 = deepcopy(l1)
    L2 = deepcopy(l2)
    Q = []
    R = []
    while est_plus_grand(L1, L2) or (L1[0] == 0 and len(L1) > 1):

        if L1[0] == [0 for i in range(len(L1))]:
            Q.append(0)
            L1.pop(0)

        decoupage = L1[: ((len(L2) + 1))]  # prog marche pas pour liste de meme taille

        decoupage = supprime_zéros(decoupage)

        i = [1]
        while est_plus_grand(decoupage, multiplication(i, L2)):

            i = addition(i, [1])

        newdecoupage = soustraction(decoupage, multiplication(L2, soustraction(i, [1])))

        for j in range(
            len(L2) + 1
        ):  # voila ou etaos ma faute depuis le debut envie de ma suisider fort putin de +1 pour 2h de taff yes
            if len(L1) != 0:
                L1.pop(0)
        newdecoupage = supprime_zéros(newdecoupage)
        L1 = newdecoupage + L1
        print(L1)

        Q = Q + soustraction(i, [1])

    reste = soustraction(l1, multiplication(Q, l2))
    supprime_zéros(reste)
    if reste == l2:
        Q = addition(Q, [1])
        reste = [0]

    return [Q, reste]
"""


def division(l1, l2):
    L1 = deepcopy(l1)
    L2 = deepcopy(l2)
    L1 = supprime_zéros(L1)
    L2 = supprime_zéros(L2)
    if est_plus_grand(L2,L1):
        return [[0],L1]
    if L1==L2:
        return [[1],[0]]
    Q = []
    restedecoupage = 0
    decoupage = L1[: (len(L2))]
    while est_plus_grand(L1, L2):
        V = [0]

        while est_plus_grand(decoupage, L2):
            decoupage = soustraction(decoupage, L2)
            V = addition([1], V)


        Q = Q + V
        if len(l1) - restedecoupage == len(L2):
            break
        restedecoupage += 1
        decoupage = decoupage + [l1[len(L2) + restedecoupage - 1]]

        if L1 == [0 for i in range(len(L1))]:
            Q += [0 for j in range(len(L1))]

    decoupage = supprime_zéros(decoupage)
    if decoupage == []:
        decoupage = [0]

    return [Q, decoupage]


def modulo(L1, modulo):
    x, reste = division(L1, modulo)
    return reste


def expo_modulaire(l1, exposant, module):
    L1 = deepcopy(l1)
    res = [1]
    expobinaire = passage_binaire(exposant)

    for i in range(len(expobinaire) - 1, -1, -1):
        if expobinaire[i] == 1:
            res = multiplication(res, L1)
            res = modulo(res, module)

        L1 = multiplication(L1, L1)
        L1 = modulo(L1, module)

    return res

from copy import *
from operations_liste import *


def multiplication_negative(l1, l2, base=10):
    L1 = deepcopy(l1)
    L2 = deepcopy(l2)
    negatif = False
    if L1[0] == L2[0] == "negatif":
        L1.remove("negatif")
        L2.remove("negatif")
    elif L1[0] == "negatif":
        negatif = True
        L1.remove("negatif")
    elif L2[0] == "negatif":
        negatif = True
        L2.remove("negatif")

    resultat = [0]
    if len(L1) == len(L2):
        L1 = [0] + L1
    L1, L2 = max(L1, L2, key=len), min(L1, L2, key=len)
    for i in range(len(L2)):
        for j in range(len(L1)):
            resultat = addition(
                resultat,
                (
                    nombre_vers_liste(L1[len(L1) - j - 1] * L2[len(L2) - i - 1])
                    + [0 for i in range(i + j)]
                ),
                base,
            )
    supprime_zéros(resultat)
    if negatif:
        resultat.insert(0, "negatif")
    return resultat


def soustraction_negative(l1, l2, base=10):
    L1 = deepcopy(l1)
    L2 = deepcopy(l2)
    negatif = False
    if L1[0] == L2[0] == "negatif":
        L1.remove("negatif")
        L2.remove("negatif")
        return soustraction_negative(L2, L1)
    elif L2[0] == "negatif":
        L2.remove("negatif")
        return addition(L1, L2)
    elif L1[0] == "negatif":
        L1.remove("negatif")
        c = addition(L2, L1)
        c.insert(0, "negatif")
        return c
    elif est_plus_grand(L2, L1):
        negatif = True
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
    supprime_zéros(new)  # important pour la base 2

    if negatif:
        new.insert(0, "negatif")

    return new


def euclide_etendue(L1, L2):
    L = deepcopy(L2)
    """
    prend en entré 2 listes et rend leurs pgcd et les deux coef de bezout sous formes de listes
    """
    echange = False
    if est_plus_grand(L2, L1):
        L2, L1 = L1, L2
        echange = True
    x = [1]
    X = [0]
    y = [0]
    Y = [1]
    while L2 != [0]:
        Q = division(L1, L2)[0]
        L1, L2 = L2, division(L1, L2)[1]
        t = soustraction_negative(x, multiplication_negative(Q, X))
        X, x = t, X
        c = soustraction_negative(y, multiplication_negative(Q, Y))
        Y, y = c, Y
    if echange:
        x, y = y, x

    if x[0] == "negatif":
        x.remove("negatif")
        g = soustraction_negative(L, x)
        x = g
    return L1, x, y  # on a l'égalité pgcd= x*L1+y*L2  ,l'inverse de  L1 modulo L2 est x


def PGCD(L1, L2):
    if est_plus_grand(L2, L1):
        L2, L1 = L1, L2

    while L2 != [0]:
        Q = division(L1, L2)[0]
        L1, L2 = L2, division(L1, L2)[1]
    return L1

def trouvepremier(n):
    t=True
    r=False
    while t :
        nombrepremier=[]
        for i in range (n-1) : 
            nombrepremier+=[randint(0,9)]
        nombrepremier+=[randrange(1,10,2)]
        b=randint(1,10**(n//2))
        b=NombreToListe(b)
        print(nombrepremier)
        if expomodulaire(b,soustraction(nombrepremier,[1]),nombrepremier)==[1]:

            for i in range (100):
                print("AAAA")

                b=randint(300,1300)
                b=NombreToListe(b)
                if expomodulaire(b,soustraction(nombrepremier,[1]),nombrepremier)==[1]:
                    r=True

                else:
                    r=False
                    break

        if r:
            t=False
    return nombrepremier
