from operations_liste import *
from random import *


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


def test_soustraction1():
    assert soustraction([1, 2], [1]) == nombre_vers_liste(11)


def test_soustraction2():
    assert soustraction([2, 0], [1, 4]) == [6]


def test_soustraction3():
    assert soustraction([1, 0, 0], [9, 9]) == [1]


def test_supprime_zéro_1():
    L1 = [0, 0, 0, 1, 2, 0, 1, 0, 0]
    supprime_zéros(L1)
    assert L1 == [1, 2, 0, 1, 0, 0]


def test_supprime_zéros_2():
    L1 = [0, 0, 0, 0]
    assert supprime_zéros(L1) == [0]


def test_change_retenue_1():
    assert change_retenue([9, 9]) == [1, 0, 0]


def test_change_retenue_2():
    assert change_retenue([4, 3]) == [4, 4]


def test_PGCD_1():
    assert PGCD([2, 2, 1], [7, 8, 2]) == [1, 7]


def test_PGCD_2():
    assert PGCD([8, 1, 1], [1, 2, 3, 7]) == [1]


def test_expo_modulaire_1():
    assert expo_modulaire([3, 7], [1, 7], [7, 9, 2, 6, 3, 4, 9, 0]) == [
        6,
        8,
        1,
        0,
        7,
        1,
        1,
        7,
    ]


def test_expo_modulaire_2():
    assert expo_modulaire([2, 6], [2, 1], [8, 7, 6, 2, 3, 7, 6, 4, 3, 2, 9]) == [
        5,
        0,
        8,
        4,
        5,
        5,
        0,
        2,
        9,
        3,
        3,
    ]


def test_sous_neg_1():
    assert soustraction_negative()
