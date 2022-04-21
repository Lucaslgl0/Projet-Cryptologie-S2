from func_all_methods import chiffrement_cesar, dechiffrement_cesar, dictionnaire

print("============================================================== Début session ==============================================================")
print("")


print("Nous allons utiliser le dictionnaire suivant : ", dictionnaire)
print("Nous utiliserons donc un dictionnaire personnalisé pour illustrer dans l'exemple du chiffrement de césar.")
print("Dans les autres exemples, nous garderons le codage ASCII.")


message_user = input("Entrez un message à coder : ")
verif = 0
while verif == 0:
   verif = 1
   for char in message_user:
      if char in dictionnaire:
         continue
      else:
         verif = 0
   if verif == 0:
      message_user = input("Des caractères ne sont pas présents dans le dictionnaire. Entrez un message à coder : ")

print("Votre message est :", message_user)

decalage_cesar = int(input("Entrez la valeur du décalage que vous souhaitez appliquer : "))

message_chiffre_cesar = chiffrement_cesar(message_user, decalage_cesar)

print("Votre message chiffré par le chiffrement de César (", decalage_cesar, ") est :", message_chiffre_cesar)


print("")
print("============================================================== Fin session ==============================================================")
print("")
print("============================================================ Début décryptage ============================================================")
print("")
print("Nous devons déchiffrer le message '", message_chiffre_cesar, "' codé par un chiffrement de César à un décalage inconnu.")
dechiffrement_cesar(message_chiffre_cesar)
print("")
print("============================================================= Fin décryptage ============================================================")
