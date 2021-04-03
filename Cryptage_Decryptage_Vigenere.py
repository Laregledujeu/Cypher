import Enlever_Caractere as EC
import Open_Write_Fichier as OpenWrite

def liste_clef(texte,clef) :
    """Permet de generer une liste de clef de meme longeur que le texte a decoder 'liste_clef(texte,clef)'"""
    x=0
    texte_final=""
    for caractere_texte in texte :
        if caractere_texte in ",?;/:§!°]=}[({'-_& " :
            texte_final+=" "
        else :
            if x==len(clef) :
                x=0
            texte_final+=clef[x]
            x+=1
    return(texte_final)

def cryptage(clef,chemin_original,chemin_final) :
    """Permet de crypter un texte avce le code vigenere 'cryptage(texte,clef)'"""
    texte=OpenWrite.ouvrir_fichier(chemin_original)
    texte=EC.enlever_carac_accent(texte.lower())
    clef=EC.enlever_carac_accent(clef.lower())
    clef=liste_clef(texte,clef)
    texte_final_coder=""
    tableau_cryptage="abcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyzacdefghijklmnopqrstuvwxyzabdefghijklmnopqrstuvwxyzabcefghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdeghijklmnopqrstuvwxyzabcdefhijklmnopqrstuvwxyzabcdefgijklmnopqrstuvwxyzabcdefghjklmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyzabcdefghijlmnopqrstuvwxyzabcdefghijkmnopqrstuvwxyzabcdefghijklnopqrstuvwxyzabcdefghijklmopqrstuvwxyzabcdefghijklmnpqrstuvwxyzabcdefghijklmnoqrstuvwxyzabcdefghijklmnoprstuvwxyzabcdefghijklmnopqstuvwxyzabcdefghijklmnopqrtuvwxyzabcdefghijklmnopqrsuvwxyzabcdefghijklmnopqrstvwxyzabcdefghijklmnopqrstuxyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwxzabcdefghijklmnopqrstuvwxy"
    for increment,carac in enumerate(texte) :
        if clef[increment]!=" " :
            x=ord(carac)-97
            y=ord(clef[increment])-97
            texte_final_coder+=tableau_cryptage[x*26+y]
        else :
            texte_final_coder+=carac
    OpenWrite.ecrire_fichier(chemin_final,texte_final_coder)

def decryptage(cle,chemin_original,chemin_final) :
    """Permet de decrypter un texte avce le code vigenere 'cryptage(texte,clef)'"""
    texte=OpenWrite.ouvrir_fichier(chemin_original)
    texte=EC.enlever_carac_accent(texte.lower())
    clef=EC.enlever_carac_accent(clef.lower())
    clef=liste_clef(texte,clef)
    texte_final_decoder=""
    tableau_cryptage="abcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyzacdefghijklmnopqrstuvwxyzabdefghijklmnopqrstuvwxyzabcefghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdeghijklmnopqrstuvwxyzabcdefhijklmnopqrstuvwxyzabcdefgijklmnopqrstuvwxyzabcdefghjklmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyzabcdefghijlmnopqrstuvwxyzabcdefghijkmnopqrstuvwxyzabcdefghijklnopqrstuvwxyzabcdefghijklmopqrstuvwxyzabcdefghijklmnpqrstuvwxyzabcdefghijklmnoqrstuvwxyzabcdefghijklmnoprstuvwxyzabcdefghijklmnopqstuvwxyzabcdefghijklmnopqrtuvwxyzabcdefghijklmnopqrsuvwxyzabcdefghijklmnopqrstvwxyzabcdefghijklmnopqrstuxyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwxzabcdefghijklmnopqrstuvwxy"
    for increment,carac in enumerate(texte) :
        if clef[increment]!=" " :
            x=0
            y=ord(clef[increment])-97
            if y<0 :
                y=0
            while tableau_cryptage[y*26+x]!=carac :
                x=x+1
            texte_final_decoder+=tableau_cryptage[x]
        else :
            texte_final_decoder+=carac
    OpenWrite.ecrire_fichier(chemin_final,texte_final_coder)

