import random,time
import chrono 
# variables de jeux
nbr_joueurs=0
liste_de_mot=[]
user_names=[]
loser=''

#variables logiques
game_over=False
temps_d_attente=3

nbr_joueurs = int(input("chhal ntoma?: "))
for nbr in range (nbr_joueurs):
    nom_joueur=input("le3ab "+str(nbr+1)+" 3tini smyatkom :")
    user_names.append(nom_joueur)

    

saisi=True
while (saisi):
    mot = input("3tini klma (ila saliti dir 0):")
    if mot!="0":
        liste_de_mot.append(mot)
    else:
        saisi=False
# print("hado homa lklmat liktbto: "+liste_de_mot)

reserve=0
nbr_de_mots=len(liste_de_mot)
if nbr_de_mots in range (1,6):
    reserve=(nbr_de_mots*30)
else:
    reserve=150
game_chrono = chrono.Chrono(reserve)
game_chrono.start()

while (not game_over):
# loop sur usrs
    # user now plays
    # user gets random word
    # timer start
    # timer stops if input matches r_w
    for user in user_names:
        print("noubet: "+user)
        klma_lmosta3mil=random.choice(liste_de_mot)
        print("hahya lklma dyalk ktbha mora matchuf start: "+klma_lmosta3mil)
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        print("start")
        game_chrono.start()
        user_input=input("=> ")
        if user_input==klma_lmosta3mil:
            game_chrono.pause()
            print("yeay kat3rf tktb")
            loser=user
        else:
            game_over= True
            loser=user

            print("sir t3awed t7diri a "+loser)
            break

    if(game_chrono.is_finished()):
        game_over = True
        print("mcha 3lik tran a "+loser)




