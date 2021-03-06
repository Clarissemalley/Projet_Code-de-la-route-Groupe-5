import random
from random import randint #pour pouvoir faire une fonction aleatoire
import tkinter as tk
from PIL import Image, ImageTk



def lectureQuesRep(borneQuesRep):
    """Ouvre le fichier des bornes de réponses et renvoie une liste dont chaque élément correspond à une question et ses paramétres"""
    fichier = open(borneQuesRep, "r") #ouvre le ficher borne de questions
    listeQuestion = [] #créer une liste vide
    for ligne in fichier:
        listeQuestion.append(ligne)#chaque du fichier est transformé en un element de liste et est envoyé dans la liste vide
    return listeQuestion #renvoie la liste

def aleaQues(borneQuesRep):
    """choisi un élément aléatoire de la liste et le renvoie"""
    listeQuestion = lectureQuesRep(borneQuesRep)
    random.shuffle(listeQuestion)#choisis aleatoirement un element de la liste
    return listeQuestion #renvoie la liste

def choixQues(paramQues):
    """renvoie une liste dont chaque élément correspond a un paramètre"""
    question = paramQues.split(';') #créer un nouvel element a la liste lorqu'il y a un point virgule dans le texte
    return question

def testReponse(question, reponse):
        """verifie si la reponse est juste, renvoie True ou fausse et renvoie False"""
        if reponse == question[5]:
            return True
        else:
            return False


def pointsrepFausses(reponse, repFausses):
    """si la reponse a la question posé est fausse, le nombre reponses fausse augment de 1, sinon le nombre de reponse fausse ne change pas"""
    if testReponse(question,reponse) == False:
        repFausses = repFausses+1
        return repFausses
    else:
        repFausses = repFausses
        return repFausses


def consigne():
    """si le bouton est actionné, ecrit les consignes"""
    t = tk.Label(window, text="Pour répondre écrivez le numéro de votre réponse, si vous avez plusieurs choix à faire ne pas mettre d'espace entre les numéros.")#créer une zone de text
    t.pack()#permet d'afficher le text


def choixQuestion():
    global numQuestion, paramQues, question
    numQuestion = randint(1,len(listeQuestion)) #prendre un nombre aleatoire entre 1 et la longuer de la liste pour choisir une question
    paramQues = listeQuestion[numQuestion-1] #
    question = choixQues(paramQues) #separe la liste de fonction a ce que chaque element correspond a un parametre de la question (question, propositions, reponse justification, nom de l'image)
    listeQuestion.remove(paramQues) #enleve la question choisie de la liste pour ne pas qu'elle soit reposée


def changePhoto():
    """affiche une image"""
    global image, photo
    nomImg = question[7] #selectionne le dernier element de la liste question qui est le nom de l'image
    image = Image.open(nomImg) #ouvre/lit l'image
    photo = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width = image.size[0], height = image.size[1]) #créer une zone dans la fenetrepour contenir l'image
    canvas.create_image(0,0, anchor = tk.NW, image=photo) #met l'image dans le canvas
    canvas.pack() #affiche le canvas


def affichageQues():
    """affiche la question et les prositions"""
    q = tk.Label(window, text=question[0]) #créer une zone de text
    q.pack() #permet d'afficher le text dans la fenetre
    a = tk.Label(window, text=question[1])#créer une zone de text
    a.pack()#permet d'afficher le text dans la fenetre
    b = tk.Label(window, text=question[2])#créer une zone de text
    b.pack()#permet d'afficher le text dans la fenetre
    if question[3] != "":
        c = tk.Label(window, text=question[3])#créer une zone de text
        c.pack()#permet d'afficher le text dans la fenetre
    if question[4] != "":
        d = tk.Label(window, text=question[4])#créer une zone de text
        d.pack()#permet d'afficher le text dans la fenetre
    reponse = tk.Entry(window, width=40) #créer une entrée pour pouvoir ecrire sa reponse
    reponse.pack() #affiche l'entrée
    validation = tk.Button(window, text="Confirmer", command=changeQues)#créer un bouton pour confirmer sa reponse et passer a une autre question en activant la fonction changeQues
    validation.pack() #permt d'afficher le bouton


def changeQues():
    global window
    window.destroy() #ferme la fenetre
    window = tk.Tk() #ouvre une nouvelle fenetre
    choixQuestion() #choisi une nouvelle question
    changePhoto() #affche l'image correspondant a la nouvelle question
    affichageQues()#affiche la question et les propositions correspondant al la nouvelle question


borneQuesRep = "quesRep.txt"
nbQues = 0
repFausses = 0
lectureQuesRep(borneQuesRep)
listeQuestion = aleaQues(borneQuesRep)

window = tk.Tk() #ouvre une fenetre
choixQuestion()#choisi une question aleatoirement
changePhoto() #affiche l'image correspondant a la question
affichageQues() #affiche la question et les propositions

window.mainloop()