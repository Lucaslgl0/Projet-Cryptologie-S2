def FichierEnTexte(fichier):
    return open(fichier).readlines()[0]


def TexteEnFichier(texte, nom):
    open(nom, "w+").write(texte)


def TexteEnListe(texte):
    Liste = []
    for i in texte:
        temp = str(ord(i))
        if len(temp) < 3:
            temp = '0' + temp
        Liste.append(temp[0])
        Liste.append(temp[1])
        Liste.append(temp[2])
    return Liste


def ListeEnTexte(Liste):
    texte = ''
    for i in range(0, len(Liste), 3):
        charactère = int(str(Liste[i]) + str(Liste[i + 1]) + str(Liste[i + 2]))
        texte += chr(charactère)
    return texte
