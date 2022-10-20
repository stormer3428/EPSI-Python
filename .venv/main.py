
"""
001 - Déclarer des variables
•    Notions abordées : les variables.
On commence simple avec ce premier exercice, qui consiste à déclarer différents types de variables.
La variable 'prenom' qui doit contenir la chaîne de caractère Pierre.
La variable 'age' qui doit contenir le nombre 20.
La variable 'majeur' qui doit contenir un boolean vrai.
La variable 'compte_en_banque' qui doit contenir le nombre décimal 20135,384.
La variable 'amis' qui doit contenir une liste contenant trois chaînes de caractères : Marie, Julien et Adrien.
La variable 'parents' qui doit contenir un tuple contenant deux chaînes de caractères : Marc et Caroline.
"""

import argparse
from ctypes import sizeof
from random import random


def Exo_1():
    print("Exo_1")
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.384
    amis = ["Marie", "Julien", "Adrien"]
    print(prenom, age, majeur, compte_en_banque, amis)
Exo_1()

def Exo_2():
    print("Exo_2")
    print("yavais que la solution et pas l'énoncé ; -;)")
Exo_2()

"""
    nombre = 15
    print("Le nombre est " + nombre)
"""

def Exo_3():
    print("Exo_3")
    nombre = 15
    print("Le nombre est " + str(nombre))
Exo_3()

""""
le 004 trop facile voici le 005 :

Dans cet exercice, nous allons utiliser les nouvelles fonctionnalités de Python 3, afin de printer les 3 variables a, b et c, séparées par un symbole d'addition (+).
Votre script doit donc afficher : 2 + 6 + 3.
a = 2
b = 6
c = 3
"""

def Exo_5():
    print("Exo_5")
    a=2
    b=6
    c=3
    print(a, "+", b, "+", c)
Exo_5()

"""
007 - Vérifier si une variable est d'un certain type
•    Notions abordées : les variables.
Dans cet exercice, vous allez devoir vérifier que la variable 'prenom' est bien une chaîne de caractères.
La variable prenom est définie au début du script par une chaîne de caractère.
Votre script doit donc printer une première fois la phrase "La variable est une chaîne de caractères".
La variable prenom est ensuite redéfinie et assignée au nombre 0.
Vous devez donc tester de nouveau votre condition mais cette fois-ci, votre script ne doit pas printer la phrase.

"""

def checkIfStr(prenom):
    print(prenom, type(prenom))
    if(str(type(prenom)) == "<class 'str'>"):
        print("prenom est un chaine de caractères")
    else:
        print("prenom n'est pas une chaine de caractères")

def Exo_7():
    print("Exo_7")
    prenom = "Pierre"
    checkIfStr(prenom)
    # INSÉRER VOTRE CONDITION ICI.
    # Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère. Ici c'est le cas,
    # votre condition doit donc être vraie et printer la phrase "La variable est une chaîne de caractères".
    
    prenom = 0
    checkIfStr(prenom)
    # INSÉRER VOTRE CONDITION DE NOUVEAU
    # Cette fois-ci, la variable n'est pas égale à une chaîne de caractère. Votre condition doit donc être fausse et 
    # la phrase ne doit pas s'afficher.
Exo_7()

def Exo_7_Bis():
    print("Exo_7_Bis")
    toTest = 3.621
    print("Voici la variable")
    print(toTest)
    print("quel type souhaitez vous tester?")
    #TODO Permettre a l'utilisateur de choisir le type a tester directement depuis la console
    input = "TODO"#l'input de l'utilisateur
    if(str(type(toTest)) == "<class '" + input + "'>"):
        print("La variable est bel et bien de type", input)
    else:
        print("La variable n'est pas de type", input, "mais de type", str(type(toTest))[8:-2]) 
#on extrait le type de la chaine <class 'str'>, avec un index négatif car la longueur du type peut varier, eg : float, int
Exo_7_Bis()

def Exo_Parcourir_Liste():
    print("Exo_Parcourir_Liste")
    liste12 = ["pomme","poire","cerise"]
    for i in range(len(liste12)):
        print(i, liste12[i])
Exo_Parcourir_Liste()

def Exo_Tri_Alphabetique():
    print("Exo_Tri_Alphabetique")
    alphabet = "abcdefghijklmnopqrstuvwxyz"                         #Utilisé comme référence, peut inclure n'importe quoi en soi et n'a pas forcément besoin d'etre dans l'ordre
    chaine = "pomme, abricot, cerise, fraise, orange, abricots"     #notre liste a trier
    tableau = chaine.split(", ")                                    #on la convertit en vraie liste, ne pas oublier l'espace dans le séparateur
    scores = []                                                     #on va trier les mots en leur accordant un score, le plus petit le score le plus proche du début

    #la facon dont l'algo va calculer les scores et en accordant un score de 1-24 a la dernière lettre, puis de 24**2-24 a l'avant dernière, etc
    # /!\ mais attention, on veut que la première lettre est la même importance pour tout les mots, on va donc partir du début
    #et pour cela il nous faut savoir de quel puissance on doit partir, et pour savoir cela il nous faut la taille du mot le plus long de la liste

    max_amplitude = 0
    for mot in tableau:                 #on parcoure le tableau
        if(max_amplitude < len(mot)):   #si le mot est plus long
            max_amplitude = len(mot)    #on met a jour la taille amx

    #maintenant qu'on a tout ce qu'il nous faut, c'est l'heure de faire notre calcul

    for mot in tableau:                                                         #on parcoure le tableau a nouveau
        score = 0
        for index_lettre in range(len(mot)):                                    #on cycle sur l'index car on a besoin de calculer l'amplitude de cette lettre 
            magnitude = (len(alphabet)+1) ** (max_amplitude - index_lettre)     #qui dépend directement de son placement dans le mot
            lettre = mot[index_lettre]
            score += magnitude * alphabet.index(lettre)                         #et on incrémente le score du mot par celui de la lettre, calculé grace a son amplitude et son placement dans l'alphabet
        print("score du mot", mot, score)
        scores.append(score)                                                    #on ajout le score du mot au meme endroit que celui ci
    sorted = []
    
    #maintenant que les scores sont calculés, il nous faut les trier du plus petit au plus grand
    
    while len(tableau) > 0:                             #on vide le tableau du mot au plus grand score jussqu'a qu'il soit vide
        highest_score = 0                               #il nous faut stocker le score max trouvé
        highest_index = -1                              #ainsi que son index
        for index in range(len(tableau)):               #on parcoure (encore) le tableau
            score = scores[index]                       #on récupère son score
            if(score > highest_score):                  #si il est plus grand que le plus grand trouve jusqu'a présent
                highest_score = score                   #on met a jour le score
                highest_index = index                   #et l'index
        sorted.insert(0, tableau.pop(highest_index))    #on transvase le mot du tableau non trié au trié
        scores.pop(highest_index)                       #et on oublie pas de supprimer son score
    print(sorted)                                       #✨Tout trié! ✨
Exo_Tri_Alphabetique()

#import math
def Exercice_calcul_volume_sphere():
    print("Exercice_calcul_volume_sphere")
    #pi = math.pi
    pi = 3.14159265359
    rayon = 15.0
    volume = (4.0 * pi / 30) * (rayon ** 3)
    print(volume)
Exercice_calcul_volume_sphere()

def Exercice_10_a_100():
    print("Exercice_10_a_100")
    liste = list(range(10,101))
    print(liste)
Exercice_10_a_100()

def Exercice_liste_pair_1_200():
    print("Exercice_liste_pair_1_200")
    liste = []
    for i in range(201):
        if(i % 2 == 0):
            liste.append(i)
    print(liste)
Exercice_liste_pair_1_200()

def Exercice_de():
    print("Exercice_de")
    nombre_lancer = 1000
    lancers = []
    for i in range(nombre_lancer):
        de = int(random() * 6) + 1
        lancers.append(de)
    # print(lancers)
    for i in range(1,7):
        count = lancers.count(i)
        print("le dé est tombé", count, "fois sur", i)
    moyenne = sum(lancers)/len(lancers)
    print("la moyenne des dés est de", moyenne)
Exercice_de()

def Exercice_nb_lettres():
    print("Exercice_nb_lettres")
    lettre = "a"
    phrase = "Salut a tous les amis, c'est David lafarge pokemon"
    nb = phrase.lower().count(lettre.lower())
    print("la letre \"", lettre, "\" apparait", nb, "fois dans la phrase \"", phrase,"\"")
Exercice_nb_lettres()

def lettre_plus_fréquente():
    print("lettre_plus_fréquente")
    alphabet = "azertyuiopqsdfghjklmwxcvbn"
    phrase = "Lorem ipsum sit amet dolor"
    
    frequences = []
    for lettre in alphabet:
        frequence = phrase.lower().count(lettre.lower())
        frequences.append(frequence)
        print("fréquence de la lettre", lettre, frequence)
    
    lettre_plus_fréquente = ""
    frequence_max = 0
    for i in range(len(alphabet)):
        frequence = frequences[i]
        if frequence > frequence_max:
            frequence_max = frequence
            lettre_plus_fréquente = alphabet[i]
    print(phrase)
    print("la lettre la plus fréquente est \"", lettre_plus_fréquente, "\" avec une fréquence de", frequence_max)
lettre_plus_fréquente()

def Exercice_insertion_char_entre():
    phrase = "Bonjour je suis une phrase"
    print(phrase)
    phrase = "i".join(phrase)   
    print(phrase)
Exercice_insertion_char_entre()