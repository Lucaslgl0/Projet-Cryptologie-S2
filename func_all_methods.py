# Création d'un dictionnaire de l'ensemble de nos caractères
dictionnaire = []
# Ponctuation
for code in range(33, 48):
   dictionnaire.append(chr(code))
dictionnaire.append(":")
dictionnaire.append(";")
dictionnaire.append("?")
# Lettres majuscules
for code in range(65, 91):
   dictionnaire.append(chr(code))
# Lettres minuscules
for code in range(97, 123):
   dictionnaire.append(chr(code))
# Le caractère espace
dictionnaire.append(" ")
# Les accents
dictionnaire.append("é")
dictionnaire.append("è")
dictionnaire.append("à")


# Codage chiffrement de César (par décalage)
'''
Cas général:
On cherche l'indice ASCII de chaque caractère de notre message pour le convertir en l'indice de notre dictionnaire.
On va ensuite appliqué un décalage à cet indice (modulo la taille de notre dictionnaire)
indice = ord(char) - (nombre nécessaire à la conversion)
resultat += chr((indice + décalage) % (taille du dictionnaire))
'''


def chiffrement_cesar(texte, décalage):
   resultat = ""
   # Parcours les caractères du message
   for char in texte:
      resultat += dictionnaire[(dictionnaire.index(char) + décalage) % len(dictionnaire)]
   return resultat


def dechiffrement_cesar(message):
   # On va tester toutes les valeurs de décalage
   for decalage in range(len(dictionnaire)):
      resultat = ""
      for lettre in message:
            resultat += dictionnaire[(dictionnaire.index(lettre) + decalage) % len(dictionnaire)]
      print(decalage, "-", resultat)
