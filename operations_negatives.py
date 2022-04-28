def soustraction_negative(
    l1, l2, base=10
):  ## les test marchent j'espere que tout marche pour la base 2 j'ai eu peur de devoir passer par le complementaire
    L1=deepcopy(l1)
    L2=deepcopy(l2)
    negatif = False
    if L1[0] == L2[0] == "negatif":
        L1.remove("negatif")
        L2.remove("negatif")
        return soustraction(L2, L1)
    elif L2[0] == "negatif":
        L2.remove("negatif")
        return addition(L1, L2)
    elif L1[0] == "negatif":
        L1.remove("negatif")
        c = addition(L2, L1)
        c.insert(0, "negatif")
        return c
    elif EstPlusGrand(L2, L1):
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
    fonctiondegage0devant(new)  ##important pour la base 2

    if negatif:
        new.insert(0, "negatif")

    return new
  
  def multiplication(l1, l2, base=10):
    L1=deepcopy(l1)
    L2=deepcopy(l2)
    negatif = False
    if L1[0]==L2[0]=="negatif":
        L1.remove("negatif")
        L2.remove("negatif")
    elif L1[0]=="negatif":
        negatif = True
        L1.remove("negatif")
    elif L2[0]=="negatif":
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
                    NombreToListe(L1[len(L1) - j - 1] * L2[len(L2) - i - 1])
                    + [0 for i in range(i + j)]
                ),
                base,
            )
    if negatif:
        resultat.insert(0,"negatif")
    return resultat
