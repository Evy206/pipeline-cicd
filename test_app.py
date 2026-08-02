from app import additionner


def test_additionner_positifs():
    resultat = additionner(2, 3)
    assert resultat == 5


def test_additionner_negatifs():
    resultat = additionner(-1, -4)
    assert resultat == -5


def test_additionner_zero():
    resultat = additionner(0, 7)
    assert resultat == 7