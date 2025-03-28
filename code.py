#ici pour le code 
# voie a suivre : 
# - ouvrir le fichier germinal_nettoye.txt, 
# - ajouter chaque mot a un dictionnaire avec comme cle le mot et comme valeur le nombre de fois ou il est apparu 
# - comparer le dictionnaire avec le les fichiers "cl_...."
# - écrire le nom du fichier auquel il y a le plus de similitude 

#ex 1 

def occurrences(chaine) :

    mots = chaine.split()  # Séparer la chaîne en mots
    compteur = {}  # Dictionnaire pour stocker les occurrences
    
    for mot in mots:
        if mot in compteur:
            compteur[mot] = compteur[mot] + 1  # Incrémente si le mot est déjà présent
        else:
            compteur[mot] = 1  # Ajoute le mot au dictionnaire
    
    return compteur


texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
print(occurrences(texte))

#ex 2

def occ_max(dico, longueur):
    max_mot = None
    max_occ = 0
    
    for mot, occ in dico.items():
        if len(mot) == longueur and occ > max_occ:
            max_mot = mot
            max_occ = occ
    
    return max_mot, max_occ

# Exemple d'utilisation
texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
dico = occurrences(texte)
print(occ_max(dico, 6))

#ex 1 
 
def occurrences(chaine) :
    """
    Transforme une chaine de caractère en dictionnaire contenant le nombre d'occurrences de chaque mot
    @parm chaine : chaine de caractère 
    @return : dictionnaire où les clés sont des mots et les valeurs
    sont des entiers strictement positif correspondant aux nombres d'occurrences de chaque mot 
    """
    mots = chaine.split()  # Séparer la chaîne en mots
    compteur = {}  # Dictionnaire pour stocker les occurrences
     
    for mot in mots:
        if mot in compteur:
            compteur[mot] = compteur[mot] + 1  # Incrémente si le mot est déjà présent
        else:
            compteur[mot] = 1  # Ajoute le mot au dictionnaire
     
    return compteur
 
 
texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
print(occurrences(texte))
 
#ex 2
 
def occ_max(dico, longueur):
    """
    Donne le mot de longueur donnée en paramètre avec le nombre d’occurrences maximal 
    et le nombre d’occurrences dans un dictionnaire
    @parm dico : dictionnaire python où les clés sont des mots et les valeurs sont 
    des entiers strictement positif correspondant aux le nombre de fois où apparaît le mot
    @parm longueur : entier strictement positif, longueur du mot à rechercher dans le dictionnaire
    @return : tuple avec le mot ayant la longueur souhaité et son nombre d'occurrences.
    """
    max_mot = None
    max_occ = 0
     
    for mot, occ in dico.items():
        if len(mot) == longueur and occ > max_occ:
            max_mot = mot
            max_occ = occ
     
    return max_mot, max_occ
 
# Exemple d'utilisation
texte = "coucou coucou c est le coucou qui dit coucou ne dit pas bonjour ne dit pas au revoir même pour se revoir"
dico = occurrences(texte)
print(occ_max(dico, 6))


def nettoyage(nom_texte):
    """
    Cette fonction lit le un fichier texte, supprime la ponctuation et convertit le texte en minuscules
    @param nom_texte : nom du fichier texte à nettoyer
    @return : fichier où le texte nettoyé a été enregistré
    """
    ponctuation = ["'", '"', "(", ")", ",", ";", ":", ".", "?", "!", "‘", "«", "»", "_", "-"]
    fichierInit = open(nom_texte, "r", encoding="utf-8")
    fichierCopie = open("C:/Users/Nolan/Desktop/projet analyse sémantique/copie.txt", "w", encoding="utf-8")
    
    for ligne in fichierInit:
        texte_nettoye = ""
        for caractere in ligne:
            if caractere in ponctuation:
                texte_nettoye = texte_nettoye + " "  
            else:
                texte_nettoye = texte_nettoye + caractere 
        
        fichierCopie.write(texte_nettoye.lower())
    
    fichierInit.close()
    fichierCopie.close()
    return "copie.txt"

print (nettoyage("C:/Users/Nolan/Desktop/projet analyse sémantique/germinal.txt"))


def mots_frequents(nom_texte):
    """
    lit un fichier texte, extrait les mots qui ont une longueur maximale de 10 caractères
    et retourne le mot le plus fréquent ainsi que sa fréquence d'apparition.
    @param nom_texte : nom du fichier texte à analyser
    """
    nom_texte = open("copie.txt", "r", encoding="utf-8")
    occurrences = {}
    for mot in mots:
        if len(mot) <= 10:
            if mot in occurrences:
                occurrences[mot] = occurrences[mot] + 1
            else:
                occurrences[mot] = 1
    
    max_occurrences = 0
    mot_max = ""
    for mot, freq in occurrences.items():
        if freq > max_occurrences:
            mot_max = mot
            max_occurrences = freq
    
    return mot_max, max_occurrences
