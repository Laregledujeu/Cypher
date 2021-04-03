import Cryptage_Decryptage as Cd
import Cryptage_Decryptage_Polybe as Cdp
import Cryptage_Decryptage_Affine as Cda
import Cryptage_Decryptage_Vigenere as Cdv

import tkinter as t #pour faire la fenetre
import tkinter.ttk as ttk #pour pouvoir faire la liste deroulante
import tkinter.filedialog as tf #pour faire le selecteur de fichier 
import tkinter.messagebox as tm #pour faire les messages d'erreur


liste_codage_possible=["Cesar","Polybe (avec ou sans clef)","Affine","Vigenere"] #je declare la liste qui contient tous les noms des codages possibles

selection_fichier=lambda label:label.config(text=tf.askopenfilename(title="Choisir le fichier :",initialdir="D:\\",filetypes=[("Fichier texte","*.txt"),("All","*")],multiple=False))
#je declare que le texte du label devient le chemin du repertoire choisi par l'utilisateur, que la fenetre s'ouvre dans le repertoire D: qui choisi des .txt et que 1 seul fichier

def choix_codage_decodage() :
    """Fonction qui declare que il ne peut il y avoir que 1 seul bouton allumer 'choix_codage_decodage()' """
    if choix.get=="c" :
        bouton_d.deselect()
    elif choix.get=="d" : #si d est selectionner
        bouton_c.deselect() # deselectionne l'autre bouton

def valider() :
    cle=variable_saisie.get() #je declare que la cle est egale a ce que l'utilisateur a ecrit dans le champ de saisie
    cle=list(cle) #je transforme la cle en liste
    for i in range(cle.count(" ")) : #je repete la boucle le nombre " " dans la cle
        del cle[cle.index(" ")] #je suprime le permier espace de la chaine
    cle="".join(cle) #je transforme la cle en chaine de caractere et elle n'a plus d'espace
    if cle=="" and liste_choix.get()!="Polybe (avec ou sans clef)" :
        tm.showerror("Erreur","La cle ' ' est incorrecte.")
    if liste_choix.get()=="Vigenere" : #si la longeur de cle est egale ou plus grand a 2 et qu'il n'y a pas de chiffre dans la cle alors je code avec le vigenere
        if choix.get()=="c" : #si le choix de l'utilisateur est le codage
            Cdv.cryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction crytage du module Codage_Decodage_Vigenere avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
        elif choix.get()=="d" : #si le choix de l'utilisateur est le decodage
            Cdv.decryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction decrytage du module Codage_Decodage_Vigenere avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
    elif liste_choix.get()=="Affine" : # si l'utilisateur a choisi "affine"
        a,b=cle.split(";") #je separe la cle en 2 la partie 1 est a et la partie 2 est b
        a,b=int(a),int(b) #je les int car c'est des chaine de caractere et moi je veux des nombres
        if choix.get()=="c" : #si le choix de l'utilisateur est le codage
            Cda.cryptage(a,b,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction crytage du module Codage_Decodage_Affine avec la cle a puis le cle b puis le texte du label fichier source et le texte du label fichier destinataireataire
        elif choix.get()=="d" : #si le choix de l'utilisateur est le decodage
            Cda.decryptage(a,b,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction decrytage du module Codage_Decodage_Affine avec la cle a puis le cle b puis le texte du label fichier source et le texte du label fichier destinataireataire
    elif liste_choix.get()=="Cesar" : #si l'utilisateur a choisi "cesar"
        if type(cle)=='int' : #si c'est un nombre
            cle=chr(97+cle) #je remplace la cle par le lettre correspondant de l'alphabet
            if cle>26 : #si c'est superieur
                cle=cle%26 #alors modulo 26
        if choix.get()=="c" : #si le choix de l'utilisateur est le codage
            Cd.cryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction crytage du module Codage_Decodage avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
        elif choix.get()=="d": #si le choix de l'utilisateur est le decodage
            Cd.decryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction decrytage du module Codage_Decodage avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
    elif liste_choix.get()=="Polybe (avec ou sans clef)" : #si l'utilisateur a choisi "Polybe (avec ou sans clef)"
        if choix.get()=="c" : #si le choix de l'utilisateur est le codage
            Cdp.cryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction crytage du module Codage_Decodage_Polybe avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
        elif choix.get()=="d" : #si le choix de l'utilisateur est le decodage et que la cle n'est pas vide
            Cdp.decryptage(cle,label_fichier_source.cget('text'),label_fichier_destinataire.cget('text'))
            #j'appelle la fonction decrytage du module Codage_Decodage_Polybe avec la cle puis le texte du label fichier source et le texte du label fichier destinataireataire
    else : #si le choix ne correspond a rien alors retourne error
        tm.showerror("Erreur","le codage ' "+liste_choix.get()+" ' est incorrecte.")
        return(0)
    tm.showinfo("Cypher","Le programme a bien ete execute")

quitter=lambda : fenetre.destroy() #fonction qui permet de detruire la fenetre

fenetre=t.Tk() #je creer la fenetre
fenetre.title("Cypher") #je lui donne un titre
fenetre.resizable(width=False,height=False) #je declare que la fenetre ne peut pas etre redimensionner
choix=t.StringVar() #je declare que choix est du type <class tkinter>
choix.set("c") # declare que le bouton allumer est Coder

bouton_c = t.Radiobutton(fenetre,variable=choix,value="c",text="Coder",command=choix_codage_decodage).grid(row=0) #j'intialise et fais apparaitre le bouton_c
bouton_d = t.Radiobutton(fenetre,variable=choix,value="d",text="Decoder",command=choix_codage_decodage).grid(row=0,column=1)
liste_choix=ttk.Combobox(fenetre,value=liste_codage_possible) #j'initalise un widget qu est une liste deroulante, les valeurs possibles sont les valeurs de la liste liste_codage_possible
liste_choix.grid(row=3,column=0,columnspan=2) #j'affiche la liste deroulante
cadre=t.LabelFrame(fenetre,text=" Selection des fichiers ") #un texte
cadre.grid(row=4,column=0,columnspan=2) #affichage du texte

texte_fichier_source=t.Label(cadre,text="Fichier source :").grid(row=6,column=0) #encore un texte puis affichage
bouton=t.Button(cadre,text="Modifier",command=lambda: selection_fichier(label_fichier_source)).grid(row=6,column=1) #bouton qui permet de modifier le fichier source
#il appelle la fonction selection_fichier et c'est elle qui renomme le label_fichier_source
label_fichier_source=t.Label(cadre,text=" ex (G:/Python/Programmes/Cesar/Fichier_original.txt)") #le label du fichier source
label_fichier_source.grid(row=7,column=0) #affichage du label_fichier_source

texte_fichier_destinataire=t.Label(cadre,text="Fichier destiataire :").grid(row=9,column=0) #label puis affichage
bouton=t.Button(cadre,text="Modifier",command=lambda: selection_fichier(label_fichier_destinataire)).grid(row=9,column=1) #bouton qui permet de modifier le fichier destinataire
#il appelle la fonction selection_fichier et c'est elle qui renomme le label_fichier_destinataire
label_fichier_destinataire=t.Label(cadre,text=" ex (G:/Python/Programmes/Cesar/Fichier_final.txt)") #le label du fichier destinataire
label_fichier_destinataire.grid(row=10,column=0) #affichage

label_cle=t.Label(fenetre,text="Cle :").grid(row=10,column=0) #texte devant le champ de saisie
variable_saisie=t.StringVar() #variable_saisie est une class tkinter
variable_saisie.set("") #je declare que de base il y a ecrit "" dans le champ de saisie
saisie=t.Entry(fenetre,textvariable=variable_saisie).grid(row=10,column=1) #je declare et affiche la champ de saisie
bouton_executer=t.Button(fenetre,text="Executer",command=lambda :valider()).grid(row=11) #bouton pour excuter le programme
bouton_fermer=t.Button(fenetre,text="Fermer",command=quitter).grid(row=11,column=1) #bouton pour quitter
fenetre.mainloop() # on affiche la fenetre