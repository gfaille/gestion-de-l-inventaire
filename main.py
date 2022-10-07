import fonction
import os

while True :

    print("taper (1) pour s'inscrire    taper (2) pour se connecter")

    choix_login_sign = int(input())

    if choix_login_sign == 1 :
        
        fonction.creation_compte(1)

    elif choix_login_sign == 2 :

        while True :

            print("utilisateur taper (1)")
            print("admin taper (2)")

            connexion = int(input())

            if connexion == 1 :

                fonction.connexion_user()
                
            elif connexion == 2 :

                fonction.connexion_admin()
            
            else :
                print("veuillez entrez un chiffre valide")
                pass
    
    else :
        print("veuillez entrez un chiffre valide")
        pass
    