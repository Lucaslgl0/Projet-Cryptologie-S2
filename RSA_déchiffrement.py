from operations_liste import supprime_zéros, expo_modulaire
from outils_crypto import liste_vers_texte, texte_vers_fichier, reconstruit, decoupage

# Récupération de la cles privée d et du module n

from RSA_cles import n, d


# Recupération du message chiffré dans le fichier texte, chiffré.txt

fichier = open("message_chiffré.txt").readlines()[0]

L = []
for i in range(len(fichier)):
    L.append(int(fichier[i]))
chiffré = decoupage(L, len(n))

# Déchiffrement

clair = []
for chif in chiffré:
    res = expo_modulaire(chif, d, n)
    remplie = len(n) - 1 - len(res) # permet de rendre des listes de taille len(n)-1
    clair.append([0 for i in range(remplie)] + res)

clair = reconstruit(clair)
clair = supprime_zéros(clair)
message_dechiffré = []
for i in clair:
    message_dechiffré.append(int(i))

# Ajout des zeros pouvant manquer pour le passage en code ASCCI, en debut du message 

if len(message_dechiffré)%3!=0:
    ajoute0 = 3 *((len(message_dechiffré)//3) + 1) - len(message_dechiffré)
    for i in range(ajoute0):
        message_dechiffré = [0] + message_dechiffré

# Transforme le message déchiffré en texte puis l'ouvre dans un fichier

passage_texte = liste_vers_texte(message_dechiffré)
texte_vers_fichier(passage_texte, "message_déchiffré.txt")

print("!!!!:déchiffrement terminée:!!!!")
