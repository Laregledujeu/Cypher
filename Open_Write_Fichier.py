def ouvrir_fichier(nom_du_fichier) :
    """Retourne une chaine de caractere qui contient chaque ligne du texte grace au nom du texte 'ouvrir_fichier(char)' """
    with open(nom_du_fichier,"r") as fichier_original : #on ouvre le fichier en mode r => read
        texte="".join(fichier_original.read())
    if texte=="" : #si texte = RIEN alors FALSE
        return(False)
    return(texte)

def ecrire_fichier(nom_du_fichier,texte) :
    """Permet d'ecrire dans le fichier 'nom_du_fichier' la variable 'texte' 'ecrire_fichier(char,char)' """
    with open(nom_du_fichier,"w") as fichier : #j'ouvre le fichier en mode w => write
        fichier.write(texte) #j'ecris la chaine dans le fichier

