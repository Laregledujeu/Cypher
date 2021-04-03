import Open_Write_Fichier as OpenWrite
import Enlever_Caractere as EC

def cryptage(cle,chemin_original,chemin_final):
    phrase=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original)) #on ouvre le fichier cela nous donne une longue chaine de caractere                                                  # j'initialise la variable
    phrasevide=""
    for i in range(len(phrase)):                                    # je crée une boucle "for" sur la longueur de la phrase
        if phrase[i] in "abcdefghijklmnopqrstuvwxyz":               # je demande si le i de la boucle for tombe sur les caractère mis en entrée ( lettre minuscule)
            ordTotal=ord(phrase[i])+int(cle)                             # place de la lettre dans la table ascii
            if ordTotal<=122:                                       # je demande si la lettre dans la table ascii est inferieur à l'index 122( lettre "z" )
                phrasevide=phrasevide+chr(ordTotal)                 # j'ajoute la lettre codée à la variable(il va chercher la lettre correspondand au chiffre dans la table ascii)
            else :
                nouvelleCle=ordTotal-123                            # c'est ce qu'il me reste à ajouter au dessus de "z"
                phrasevide=phrasevide+chr(97+nouvelleCle)           # j'ajoute la lettre en repartant de "a"+ ce qu'il restait au dessus de "z"
        elif phrase[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":               # on fait pareil pour les majuscules
                ordTotal=ord(phrase[i])+int(cle)                         # place dans la table ascii ( donc c'est un chifffre)
                if ordTotal<91:
                    phrasevide=phrasevide+chr(ordTotal)             # il va chercher la lettre correspondand au chiffre dans la table ascii
                else :
                    nouvelleCle=ordTotal-123                        # même chose avec les majuscules ( autre index )
                    phrasevide=phrasevide+chr(97+nouvelleCle)
        elif phrase[i]==" ":                                          # si c'est un espace il le compte
            phrasevide=phrasevide+" "
        else :                                                      #si on le connait pas on ne le code pas 
            phrasevide+=phrase[i]
    OpenWrite.ecrire_fichier(chemin_final,phrasevide)               #on ecrit le texte dans un fichier                                      

def decryptage(cle,chemin_original,chemin_final) :
    """Permet de decrypter un texte a l'aide d'une cle 'decrytage(char,str)' """
    texte=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original)) #on ouvre le fichier cela nous donne une longue chaine de caractere
    cle=cle[0].lower() # je ne prend que la premiere lettre et en minuscule
    if texte!=False : #si texte n'est pas vide
        if ord(cle)<=97 or ord(cle)>122 : #on regarde si la cle est correcte
            return(False) #si non alors stop
        texte_decrypter=""
        for carac in texte : #boucle for de chaque caractere du texte
            if carac in "abcdefghijklmnopqrstuvwxyz" : #si le caractere est en minuscule
                texte_decrypter+=chr(((ord(carac)-(ord(cle)-97*2))%26)+97) #je decode et ecris le caractere dans le texte
            elif carac in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
                texte_decrypter+=chr(((ord(carac)-(ord(cle)-65*2))%26)+65) #je decode et ecris le caractere dans le texte
            else : #si je ne connait pas le carac alors je ne le code pas
                texte_crypter+=carac
        OpenWrite.ecrire_fichier(chemin_final,texte_decrypter) #on ecrit le texte dans un fichier