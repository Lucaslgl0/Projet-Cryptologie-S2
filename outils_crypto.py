def fichier_vers_texte(fichier):
    """Récupération des caractères d'un fichier dans une chaine de charactères

    Cette fonction va nous permettre de récupérer les clés contenus dans des fichiers.
    Ces clés sont codés dans un format spécial (normalisé) mais cette fonction va uniquement nous permettre de récupérer la clé comme chaine de charactères.

    Args :
        fichier (file): sera le fichier contenant la clé

    Returns :
        str : Le contenu du fichier converti en chaine de charactères.
    """
    return open(fichier).readlines()[0]


def texte_vers_fichier(texte, fichier):
    """Envoi d'une chaine de charactères dans un fichier

    Cette fonction va nous permettre d'écrire dans un fichier déjà existant n'importe quel texte.
    Si nous devons renvoyer une information qui a été modifié par nos fonctions, nous pourrons la réécrire dans un fichier grâce à cette fonction.

    Args :
        texte (str): sera la chaine de charactères contenant l'information
        fichier (file): sera le fichier où l'on écrira l'information

    Returns :
        La fonction ne retourne rien mais modifie directement le fichier
    """
    open(fichier, "w+").write(texte)


def texte_vers_liste(texte):
    """Transformation d'une chaine de charactères en une liste

    Cette fonction est utile une fois que l'on a récupéré une information d'un fichier (dans notre cas un nombre très grand).
    Cette information sous forme de chaine de charactères sera transformée en une liste où chaque élément de la liste correspond à un charactère.
    Dans notre cas, pour suivre le chiffrement d'information via le protocole RSA, nous avons décidé de récupérer le message contenu dans la chaine de charactère pour convertir chaque charactère du message en son code ASCII (norme informatique du codage de charactères où chaque charactère est lié à un numéro) et le rentrer dans la liste (où chaque chiffre du code ASCII devient donc un élément de la liste ordonnée).


    Args :
        texte (str): sera la chaine de charactère contenant l'information (le message à communiquer)

    Returns :
        list : La fonction renvoie une liste ordonnée contenant le message codé en ASCII par l'ordinateur et où chaque chiffre de ce codage est un élément de la liste.
    """
    Liste = []
    for i in texte:
        temp = str(ord(i))
        if len(temp) < 3:
            temp = "0" + temp
        Liste.append(int(temp[0]))
        Liste.append(int(temp[1]))
        Liste.append(int(temp[2]))
    return Liste


def liste_vers_texte(Liste):
    """Transformation d'une liste en chaine de charactères

    Cette fonction est pour décoder un message, une fois que nous avons une liste contenant tout les chiffres d'un codage ASCII.
    Cette fonction est l'inverse de la précédente : 'texte_vers_liste'. Nous allons récupérer et convertir notre chaine de charactères codé en ASCII

    Args :
        Liste (list): sera la liste contenant le message décodé par sa représentations ASCII (où chaque nombre de cette représentation est un élémént de la liste).

    Returns :
        str : La fonction nous renvoie donc la chaine de charactère correspondand au code ASCII décodé contenu dans la liste d'entrée.
    """
    texte = ""
    for i in range(0, len(Liste), 3):
        charactère = int(str(Liste[i]) + str(Liste[i + 1]) + str(Liste[i + 2]))
        texte += chr(charactère)
    return texte


def reconstruit(L):
    new = []
    for i in range(len(L)):
        new.extend(L[i])
    return new


def decoupage(L, taille):
    sub = len(L) / taille  # le nombre de division
    if int(sub) != sub:
        b = taille - (len(L) % taille)  # nombre de 0 à rajouter
        sub = int(sub) + 1
        for i in range(b):
            L = [0] + L
    new = []
    for i in range(0, len(L), taille):  # décomposition dans une liste
        new.append(L[i : i + taille])
    return new
