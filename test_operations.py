from operations_liste import *
from random import *


class bcolors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


def test_NombreToListe():
    assert nombre_vers_liste(123) == [1, 2, 3]


def test_NombreToListe2():
    assert nombre_vers_liste(10786) == [1, 0, 7, 8, 6]


def test_addition():
    assert addition([1, 2], [3, 4]) == nombre_vers_liste(46)


def test_addictionconteur():
    assert addition([1, 9], [3, 4]) == nombre_vers_liste(19 + 34)


def test_finaddictionconteur():
    assert addition([9, 1], [3, 4]) == nombre_vers_liste(91 + 34)


def test_gauche():
    assert addition([1, 2], [3]) == nombre_vers_liste(15)


def test_droit():
    assert addition([3], [1, 2]) == nombre_vers_liste(15)


def test_compteur():
    assert addition([9, 1], [9]) == nombre_vers_liste(100)


def test_general():
    assert addition([9, 9], [1, 2, 8, 9]) == nombre_vers_liste(1289 + 99)


def test_zero():
    assert addition([0], [2, 0]) == [2, 0]


def test_changeliste():
    assert change_retenue([1, 2]) == [1, 3]


def test_changeliste1():
    assert change_retenue([1, 9]) == [2, 0]


def test_changeliste3():
    assert change_retenue([9]) == [1, 0]


def test_multiplication_1():
    assert multiplication([2, 8, 4], [3, 5]) == [9, 9, 4, 0]


def test_multiplication_2():
    assert multiplication([0], [3, 5]) == [0]


def test_multiplication_3():
    assert multiplication([9, 9, 9, 9], [9, 9]) == [9, 8, 9, 9, 0, 1]


def test_estplusgrand_1():
    assert est_plus_grand([1, 2, 3, 4], [1, 2, 3, 3])


def test_estplusgrand_2():
    assert not est_plus_grand([1, 2, 3, 3], [1, 2, 3, 4])


def test_estplusgrand_3():
    assert not est_plus_grand([0], [1])


def test_estplusgrand_4():
    assert est_plus_grand([1, 0], [1, 0])


def test_division_1():
    assert division([1, 2], [1]) == [[1, 2], [0]]


def test_division_2():
    assert division([9, 5, 3], [1, 7]) == [[5, 6], [1]]


def test_division_3():
    assert division([1, 2, 3, 4, 5, 6], [7, 8, 9]) == [[1, 5, 6], [3, 7, 2]]


def test_division_4():
    assert division([1, 0, 0, 0, 0, 0], [4, 9, 3]) == [[2, 0, 2], [4, 1, 4]]


def test_division_5():
    assert division([1, 2, 0, 1], [2]) == [[6, 0, 0], [1]]


def test_division_6():
    assert division([5, 3, 6, 8, 7, 2], [8, 7, 0, 9]) == [[6, 1], [5, 6, 2, 3]]


for j in range(1, 10000):
    L1 = nombre_vers_liste(j)
    print(bcolors.WARNING, "L1 :", L1)
    for i in range(1, j):
        L2 = nombre_vers_liste(i)
        division_test = division(L1, L2)
        division_vraie = [nombre_vers_liste(j // i), nombre_vers_liste(j % i)]
        if division_test == division_vraie:
            continue
            # print(bcolors.OK, division_test)
        else:
            print(
                bcolors.FAIL,
                L1,
                L2,
                "Ce qu'on obtient:",
                division_test,
                ". Ce qu'on devrait obtenir :",
                division_vraie,
            )
            exit()


def test_soustraction1():
    assert soustraction([1, 2], [1]) == nombre_vers_liste(11)


def test_soustraction2():
    assert soustraction([2, 0], [1, 4]) == [6]


def test_soustraction3():
    assert soustraction([1, 0, 0], [9, 9]) == [1]


def test_supprime_zéros():
    L1 = [0, 0, 0, 1, 2, 0, 1, 0, 0]
    supprime_zéros(L1)
    assert L1 == [1, 2, 0, 1, 0, 0]
