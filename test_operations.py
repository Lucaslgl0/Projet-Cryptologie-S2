from operations import (
    NombreToListe,
    addition,
    retenue,
    multiplication,
    EstPlusGrand,
    soustraction,
    division,
    exposant,
    supprime_zéros,
)


def test_NombreToListe():
    assert NombreToListe(123) == [1, 2, 3]


def test_NombreToListe2():
    assert NombreToListe(10786) == [1, 0, 7, 8, 6]


def test_addition():
    assert addition([1, 2], [3, 4]) == NombreToListe(46)


def test_addictionconteur():
    assert addition([1, 9], [3, 4]) == NombreToListe(19 + 34)


def test_finaddictionconteur():
    assert addition([9, 1], [3, 4]) == NombreToListe(91 + 34)


def test_gauche():
    assert addition([1, 2], [3]) == NombreToListe(15)


def test_droit():
    assert addition([3], [1, 2]) == NombreToListe(15)


def test_compteur():
    assert addition([9, 1], [9]) == NombreToListe(100)


def test_general():
    assert addition([9, 9], [1, 2, 8, 9]) == NombreToListe(1289 + 99)


def test_zero():
    assert addition([0], [2, 0]) == [2, 0]


def test_changeliste():
    assert retenue([1, 2]) == [1, 3]


def test_changeliste1():
    assert retenue([1, 9]) == [2, 0]


def test_changeliste3():
    assert retenue([9]) == [1, 0]


def test_multiplication_1():
    assert multiplication([2, 8, 4], [3, 5]) == [9, 9, 4, 0]


def test_multiplication_2():
    assert multiplication([0], [3, 5]) == [0]


def test_multiplication_3():
    assert multiplication([9, 9, 9, 9], [9, 9]) == [9, 8, 9, 9, 0, 1]


def test_estplusgrand_1():
    assert EstPlusGrand([1, 2, 3, 4], [1, 2, 3, 3])


def test_estplusgrand_2():
    assert not EstPlusGrand([1, 2, 3, 3], [1, 2, 3, 4])


def test_estplusgrand_3():
    assert not EstPlusGrand([0], [1])


def test_estplusgrand_4():
    assert not EstPlusGrand([1, 0], [1, 0])


def test_division_1():
    assert division([1, 2], [1]) == [[1, 2], [0, 0]]


def test_division_2():
    assert division([9, 5, 3], [1, 7]) == [[5, 6], [0, 0, 1]]


def test_soustraction1():
    assert soustraction([1, 2], [1]) == NombreToListe(11)


def test_soustraction2():
    assert soustraction([2, 0], [1, 4]) == [0, 6]


def test_soustraction3():
    assert soustraction([1, 0, 0], [9, 9]) == [0, 0, 1]


def test_exposant1():
    assert exposant([5, 6], [3]) == NombreToListe(56**3)


def test_supprime_zéros():
    L1 = [0, 0, 0, 1, 2, 0, 1, 0, 0]
    supprime_zéros(L1)
    assert L1 == [1, 2, 0, 1, 0, 0]
