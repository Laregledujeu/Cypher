import Enlever_Caractere as EC
import Open_Write_Fichier as OpenWrite

carre_polybe_codage=[('', '11'), ('', '21'), ('', '31'), ('', '41'), ('', '51'), ('', '12'), ('', '22'), ('', '32'), ('', '42'), ('', '52'), ('', '13'), ('', '23'), ('', '33'), ('', '43'), ('', '53'), ('', '14'), ('', '24'), ('', '34'), ('', '44'), ('', '54'), ('', '15'), ('', '25'), ('', '35'), ('', '45'), ('', '55')]
carre_polybe_decodage=[('11',''), ('21',''), ('31',''), ('41',''), ('51',''), ('12',''), ('22',''), ('32',''), ('42',''), ('52',''), ('13',''), ('23',''), ('33',''), ('43',''), ('53',''), ('14',''), ('24',''), ('34',''), ('44',''), ('54',''), ('15',''), ('25',''), ('35',''), ('45',''), ('55','')]

def correction_tableau(cle) :
    global carre_polybe_codage #je declare que j'utilise la liste de __main__
    global carre_polybe_decodage #je declare que j'utilise la liste de __main__

    #je remet a zero les listes
    carre_polybe_codage=[('', '11'), ('', '21'), ('', '31'), ('', '41'), ('', '51'), ('', '12'), ('', '22'), ('', '32'), ('', '42'), ('', '52'), ('', '13'), ('', '23'), ('', '33'), ('', '43'), ('', '53'), ('', '14'), ('', '24'), ('', '34'), ('', '44'), ('', '54'), ('', '15'), ('', '25'), ('', '35'), ('', '45'), ('', '55')]
    carre_polybe_decodage=[('11',''), ('21',''), ('31',''), ('41',''), ('51',''), ('12',''), ('22',''), ('32',''), ('42',''), ('52',''), ('13',''), ('23',''), ('33',''), ('43',''), ('53',''), ('14',''), ('24',''), ('34',''), ('44',''), ('54',''), ('15',''), ('25',''), ('35',''), ('45',''), ('55','')]
    temp="" #je declare une variable tampo
    for carac in cle : #boucle for pour enlever toutes les ponctuation et les nombres  de la clef
        if carac in ",?;/:§!°]=}[({'-_&0123456789 " :
            pass
        else : #si le carac n'est pas dans la chaine des interdits
            temp+=carac #alors j'ajoute carac a temp
    cle=temp #je dit que la cle est egale a temp qui est la variable tampon qui m'a servi dans ma boucle for
    cle=EC.enlever_carac_accent(cle.lower()) #je corrige encore la clef
    temp="" #je remet a zero temp
    increment=0 #je dit que l'increment est a 0
    if cle!="" : #si la cle est vide cela veut dire que on fait un polybe sans cle donc je passe
        for carac in cle : #boucle for dans la cle
            if carac not in temp : #si le caractere n'est pas dans la variable tampon alors
                if str(carac)=="j" : #si le caractere est j alors je ne fait rien
                    pass
                else : #sinon je continue a faire les listes de codage et de decodage
                    carre_polybe_codage[increment]=str(carac),carre_polybe_codage[increment][1] #je dit que l'element'increment' de la liste est un tuple de carac et de son nombre
                    carre_polybe_decodage[increment]=carre_polybe_decodage[increment][1],str(carac) #je dit que l'element'increment' de la liste est un tuple de nombre et de carac
                    temp+=carac #j'ajoute le carac a temp qui est la liste qui contient tous les caracteres deja mis dans les listes
                    increment+=1 #j'incremente incremente
    for carac in range(0,26) : #for de 0 a 26
        if chr((97+carac)) not in temp : #si le carac n'est pas dans temp
            if chr((97+carac))=="j" : #si c'est j alors je fait rien
                pass
            else : #sinon je continue a faire les listes de codage et de decodage
                carre_polybe_codage[increment]=chr(carac+97),carre_polybe_codage[increment][1] #je dit que l'element'increment' de la liste est un tuple de carac et de son nombre
                carre_polybe_decodage[increment]=carre_polybe_decodage[increment][0],chr(carac+97)  #je dit que l'element'increment' de la liste est un tuple de nombre et de carac
                temp+=chr(carac+97) #j'ajoute le carac a temp qui est la liste qui contient tous les caracteres deja mis dans les listes
                increment+=1 #j'incremente incremente
    carre_polybe_codage=dict(carre_polybe_codage) #je transforme la liste de codage en dictionnaires
    carre_polybe_decodage=dict(carre_polybe_decodage) #je transforme la liste de codage en dictionnaires

def cryptage(cle,chemin_original,chemin_final) :
    texte=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original)) #on ouvre le fichier cela nous donne une longue chaine de caractere
    texte.lower()
    if texte!=False : #si le texte n'est pas vide
        correction_tableau(cle) #je modifie les dictionnaires de codage et de decodage
        texte_crypter="" #textecrypter est vide
        for carac in texte :# for de tous les caracteres dans le texte
            if carac in "j" : #si le caractere est j alors je le code avec la cle i
                texte_crypter+=(carre_polybe_codage["i"]+",")
            elif carac in "abcdefghiklmnopqrstuvwxyz" : #sinon je demande la valeurs dans le dictionnaires puis je rajoute une virgule
                texte_crypter+=(carre_polybe_codage[carac]+",")
            else :
                texte_crypter+='"'+carac+'",'# si je ne conait pas le caractere alors je ne le code pas mais je l'entoure de "
        OpenWrite.ecrire_fichier(chemin_final,texte_crypter[:-1]) #on ecrit le texte sans la derniere virgule dans un fichier

def decryptage(cle,chemin_original,chemin_final) :
    texte=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original)) #on ouvre le fichier cela nous donne une longue chaine de caractere
    texte=texte.lower() #je ne gere que les minuscules
    if texte!=False : #si le texte n'est pas vide
        correction_tableau(cle) #je modifie les dictionnaires de codage et de decodage
        texte=texte.split(",") #je separe le texte grace au virgule
        texte_decrypter="" #textedecrypter est vide
        for carac in texte : # for de tous les caracteres dans le texte
            if '"' not in carac : #si il n'y a pas de " alors je prends la valeur du dictionnaires
                texte_decrypter+=carre_polybe_decodage[carac]
            else : #si il y a des " alors je ne l'est pas coder donc je prend le caractere entre "
                texte_decrypter+=carac[1]
        OpenWrite.ecrire_fichier(chemin_final,texte_decrypter) #on ecrit le texte dans un fichier