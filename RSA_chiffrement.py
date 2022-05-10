from outils_crypto import fichier_vers_texte, texte_vers_liste, decoupage, reconstruit
from operations_liste import expo_modulaire

# Récupération des cles publiques, l'exposant et le modulo:n

from RSA_cles import n, exposant

# Récupération du message
# Attention seule la premiere ligne est lue

fichier = fichier_vers_texte("message.txt")  # nom du fichier ou est le message
message = texte_vers_liste(fichier)

# Crytage

new = decoupage(message, len(n)-1)  # liste de liste de taille len(n)-1
chiffré = []
for mes in new:
    ret = expo_modulaire(mes, exposant, n)
    rempli = len(n) - len(ret)  # nombre de zero à rajouter à gauche
    chiffré.append([0 for i in range(rempli)] + ret)  # liste de liste de taille len(n)
chiffré = reconstruit(chiffré)  # liste de chiffre

# Création d'un fichier texte avec le message chiffré

f_code = ""
for i in chiffré:
    f_code += str(int(i))
code = open("message_chiffré.txt", "w")
code.write(f_code)
code.close()

print("!!!!:chiffrement terminé:!!!!")
