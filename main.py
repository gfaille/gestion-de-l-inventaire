import fonction
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

            if user[2] == 1 :

                #écran accueil admin
                while True :
                    pass
            
            else :

                #ecran accueil utilisateur
                while True :
                    pass

    else :
        fonction.afficher_erreur()
    