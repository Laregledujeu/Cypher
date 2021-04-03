import Open_Write_Fichier as OpenWrite
import Enlever_Caractere as EC

def cryptage(cle_a,cle_b,chemin_original,chemin_final) :
    texte=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original))
    cle_a,cle_b=cle_a%26,cle_b%26 #on divise par 26 et on garde le reste si jamais la cle est superieur a 26
    texte_final=""
    for lettre in texte : #for de tout les caracteres
        if lettre in "abcdefghijklmnopqrstuvwxyz" :#si c'est une minuscule
            texte_final+=chr(((cle_a*(ord(lettre)-97)+cle_b)%26)+97) #je code et ecris le caractere dans le texte
        elif lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            texte_final+=chr(((cle_a*(ord(lettre)-65)+cle_b)%26)+65) #je code et ecris le caractere dans le texte
        elif lettre in "0123456789" :
            texte_final+=chr(((cle_a*(ord(lettre)-48)+cle_b)%10)+48) #je code et ecris le caractere dans le texte
        else : #si je ne connait pas le caractere alors je ne le code pas
            texte_final+=lettre
    OpenWrite.ecrire_fichier(chemin_final,texte_final)

def decryptage(cle_a,cle_b,chemin_original,chemin_final) :
    texte=EC.enlever_carac_accent(OpenWrite.ouvrir_fichier(chemin_original)) #texte est le contenu du fichier qui a pour chemin d'acces chemin_original et au qu'elle on retire les accents
    cle_a,cle_b=cle_a%26,cle_b%26 #on divise par 26 et on garde le reste si jamais la cle est superieur a 26
    inconnue=1 #je cherche la valeur de A' grace a une boucle while qui ne s'arrete que lorsque que le theoreme de Bachet-Bezout est vrai
    while (cle_a*inconnue)%26!=1 :
        inconnue+=1
    texte_final=""
    for lettre in texte :
        if lettre in "abcdefghijklmnopqrstuvwxyz" :
            texte_final+=chr(((((ord(lettre)-97)-cle_b)*inconnue)%26)+97) #je code et ecris le caractere dans le texte
        elif lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            texte_final+=chr(((((ord(lettre)-65)-cle_b)*inconnue)%26)+65) #je code et ecris le caractere dans le texte
        elif lettre in "0123456789" :
            texte_final+=chr(((((ord(lettre)-48)-cle_b)*inconnue)%10)+48) #je code et ecris le caractere dans le texte
        else :
            texte_final+=lettre #si le carac a passer tous le if alors je ne le code pas
    OpenWrite.ecrire_fichier(chemin_final,texte_final) #le texte est ecrit dans le fichier qui a pour chemin d'acces
