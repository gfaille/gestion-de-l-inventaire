import fonction
import crud
import os
import time

quitter = True

while quitter :

    # écran d'inscription / connexion
    os.system("clear")
    print(" taper (1) pour s'inscrire\n taper (2) pour se connecter \n taper (3) pour quitter")

    commande = int(input())

    if commande == 1 :
        
        fonction.creation_user()

    elif commande == 2 :
        
        user = fonction.connexion_user()
        
        if user == None :

            fonction.afficher_erreur()

        else :

            if user[1] == 1 :

                #écran accueil admin
                while True :
                    
                    print("Statistique : ")
                    print("Nombre de pc en prêts : ", crud.calcul_pc())
                    print("Nombre de ticket en cours : ", crud.ticket_en_cours("en cours"))
                    print("Nombre de ticket terminés : ", crud.ticket_en_cours("terminé"))
                    
                    commande = input("P: crée un nouveau ordinateur,    A: ajoute un pc a un utilisateur,   \nT: voir vos tickets,    Q: quitter ")

                    if commande == "p" :
                        
                        nb_pc = int(input("combien de pc voulez-vous crée"))

                        for _ in range(nb_pc) :
                            fonction.ajout_ordinnateur()
                    
                    elif commande == "a" :
                        
                        print(crud.select_user_admin(), crud.select_ordinateur())

                        fonction.ajout_pc_user()
                        
                        time.sleep(20)
                    
                    elif commande == "t" :
                        pass

                    elif commande == "q" :
                        break

                    else :
                        pass
            
            else :

                #ecran accueil utilisateur
                while True :
                    pass

    elif commande == 3 :
        quitter = False

    else :
        fonction.afficher_erreur()
    