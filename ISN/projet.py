import random
from random import randint #pour pouvoir faire une fonction aleatoire
import tkinter as tk
from PIL import Image, ImageTk



def lectureQuesRep(borneQuesRep):
    fichier = open(borneQuesRep, "r")
    listeQuestion = []
    for ligne in fichier:
        listeQuestion.append(ligne)
    return listeQuestion

def aleaQues(borneQuesRep): #ordre aleatoire de questions
    listeQuestion = lectureQuesRep(borneQuesRep)
    random.shuffle(listeQuestion)
    return listeQuestion

"""def separQues(listeQuestion): #affiche le premier element de la liste qui est les parametres de la question
    paramQues = []
    for paramQues in listeQuestion:
        paramQues = paramQues.strip('\n')#enlever retour a la ligne
        paramQues = paramQues.split(';') #separer elements pour transformer chaine de caractere en liste
    return paramQues"""

def choixQues(paramQues): #affiche le premier element de la liste qui est la question
    question = paramQues.split(';')
    return question

def affichage(question): #affiche le premier element de la liste qui est la question
        print(question[0]) #affiche la question
        print(question[1]) #affiche les propositions
        print(question[2]) #affiche les propositions
        if question[3] != "": #si il n'y a pas de proposition n'affiche rien(evite un espace)
            print(question[3]) #affiche les propositions
        if question[4] != "": #si il n'y a pas de proposition n'affiche rien(evite un espace)
            print(question[4]) #affiche les propositions

def afficheRep(question): #pouvoir ecrire sa reponse et dis si la reponse est vraies ou fausse
    """dire ce que fait la fonction ... """
    """reponse = input("Quel est votre réponse?")"""
    if testReponse(question,reponse) == True:
        print("Bonne réponse!")
    else:
        print("FAUX!")
    print(question[6])
    return reponse

def testReponse(question, reponse): #verifie si la reponse est juste ou fausse
        if reponse == question[5]:
            return True
        else:
            return False


def pointsrepFausses(reponse, repFausses): #nombre reponses fausses
    if testReponse(question,reponse) == False:
        repFausses = repFausses+1
        return repFausses
    else:
        repFausses = repFausses
        return repFausses

def singPlur(repFausses): #accord avec le mot faute(s) dans la phrase finale
    if repFausses <= 1:
        return "faute"
    else:
        return "fautes"


def afficher_image(x):


    image = Image.open(x)
    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(window, width = image.size[0], height = image.size[1])
    canvas.create_image(0,0, anchor = tk.NW, image=photo)
    canvas.pack()
    window.mainloop()

borneQuesRep = "quesRep.txt"
# test fonctions
nbQues = 0
repFausses = 0
lectureQuesRep(borneQuesRep)
listeQuestion = aleaQues(borneQuesRep)

"""while nbQues != 10:

    numQuestion = randint(1,len(listeQuestion)) #choix aleatoire de la question
    paramQues = listeQuestion[numQuestion-1] #prendre un nombre aleatoire entre les differentes questions
    question = choixQues(paramQues)
    x = question[7]
    afficher_image(x)
    affichage(question)
    listeQuestion.remove(paramQues) #enleve une question de la liste une fois qu'elle a Ã©tÃ© posÃ©e

    reponse = afficheRep(question)
    testReponse(question, reponse)
    repFausses = pointsrepFausses(reponse, repFausses)
    nbQues = nbQues+1
accordfautes = singPlur(repFausses)
print("Vous avez fait", repFausses, accordfautes,"sur", nbQues, "questions")"""


numQuestion = randint(1,len(listeQuestion)) #choix aleatoire de la question
paramQues = listeQuestion[numQuestion-1] #prendre un nombre aleatoire entre les differentes questions
question = choixQues(paramQues)
x = question[7]

window = tk.Tk()

def consigne():
    t = tk.Label(window, text="Pour répondre écrivez le numéro de votre réponse, si vous avez plusieurs choix à faire ne pas mettre d'espace entre les numéros.")
    t.pack()


def validation():
    print (reponse.get())


def rr(reponse):
    if reponse == 1:
        h = tk.Label(window, "jbi")
        h.pack()
    else:
        m = tk.Label(window, "uihu")
        m.pack()


while nbQues != 10:
    question = choixQues(paramQues)
    image = Image.open(x)
    photo = ImageTk.PhotoImage(image)

    consigne = tk.Button(window, text="Consignes", command=consigne)
    consigne.pack()

    canvas = tk.Canvas(window, width = image.size[0], height = image.size[1])
    canvas.create_image(0,0, anchor = tk.NW, image=photo)
    canvas.pack()



    q = tk.Label(window, text=question[0])
    q.pack()
    a = tk.Label(window, text=question[1])
    a.pack()
    b = tk.Label(window, text=question[2])
    b.pack()
    if question[3] != "":
        c = tk.Label(window, text=question[3])
        c.pack()
    if question[4] != "":
        d = tk.Label(window, text=question[4])
        d.pack()
    reponse = tk.Entry(window, width=40)
    reponse.pack()

    validation = tk.Button(window, text="Confirmer")
    validation.pack()





    window.mainloop()

""" justif = tk.Label(root, text=question[6])
justif.pack()"""
""", command=rr(reponse)"""