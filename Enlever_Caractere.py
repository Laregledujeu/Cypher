def enlever_carac_accent(texte_initial) :
    """Permet de remplacer les lettres avec accents par les lettres correspondante sans accents'enlever_carac_accent(char)' """
    if "é" in texte_initial or "è" in texte_initial  or "à" in texte_initial or "ù" in texte_initial :      #si il y a une lettre avec un accent dans le texte
        texte=""
        for lettre in texte_initial :
            if lettre in "éè" :       # si lettre est dans la chaine de caractere alors elle perd son accent
                texte+="e" # alors elle perd son accent
            elif lettre in "à" :
                texte+="a"
            elif lettre in "ù" :
                texte+="u"
            else :
                texte=texte+lettre
        return(texte)
    else :
        return(texte_initial) #si le texte ne contient pas d'accent alors je retourne le texte qui n'est pas modifier
