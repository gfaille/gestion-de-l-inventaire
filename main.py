import fonction
import crud
import os

Quitter = False

while True :

    # écran d'inscription / connexion
    os.system("clear")
    print("taper (1) pour s'inscrire\n taper (2) pour se connecter")

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
                    print("Nombre de pc en prêts : " + crud.calcul_pc())
                    print("Nombre de ticket en cours : " + crud.ticket_en_cours("en cours"))
                    print("Nombre de ticket terminés : " + crud.ticket_en_cours("terminé"))
            
            else :

                #ecran accueil utilisateur
                while True :
                    pass

    else :
        fonction.afficher_erreur()
    