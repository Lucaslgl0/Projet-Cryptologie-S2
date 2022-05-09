from operations_liste import supprime_zéros, expo_modulaire
from outils_crypto import liste_vers_texte, texte_vers_fichier, reconstruit, decoupage

# Récupération de la cles privée d et du module n

from RSA_cles import n, d


# Rupération du message chiffré dans le fichier texte, code.txt

fichier = open("message_chiffré.txt").readlines()[0]

L = []
for i in range(len(fichier)):
    L.append(int(fichier[i]))
chiffré = decoupage(L, len(n))

# Déchiffrement
clair = []
for chif in chiffré:
    res = expo_modulaire(chif, d, n)
    remplie = len(n) - 1 - len(res)
    clair.append([0 for i in range(remplie)] + res)
clair = reconstruit(clair)
clair = supprime_zéros(clair)
super_clair = []
for i in clair:
    super_clair.append(int(i))

# Transforme le message déchiffré en texte puis l'ouvre dans un fichier
if len(super_clair)%3!=1:
    print("erreur dans le découpage")
 # notre programme de liste à texte prend 3 élements en même temps pour le code ASCII, cf Luigi

clair_texte = liste_vers_texte(super_clair)
texte_vers_fichier(clair_texte, "message_déchiffré.txt")

print("!!!!:déchiffrement terminée:!!!!")
