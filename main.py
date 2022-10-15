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

                os.system("clear")
                #écran accueil admin
                while True :
                    
                    print("Statistique : ")
                    print("------------------------")
                    print("Nombre de pc en prêts : ", crud.calcul_pc())
                    print("Nombre de ticket en cours : ", crud.tickets("En cours"))
                    print("Nombre de ticket terminés : ", crud.tickets("terminé"))
                    print("------------------------")
                    commande = input("P: crée un nouveau ordinateur,    A: ajoute un pc a un utilisateur,   \nT: voir vos tickets,    Q: quitter ")

                    if commande == "p" :
                        
                        os.system("clear")
                        nb_pc = int(input("combien de pc voulez-vous crée"))

                        for _ in range(nb_pc) :
                            fonction.ajout_ordinnateur()
                    
                    elif commande == "a" :
                        
                        os.system("clear")
                        print(crud.select_user_admin(), crud.select_ordinateur())
                        pc_pret = int(input("combien d'utilisateur seront assigner a un ordinateur "))

                        for _ in range(pc_pret) :
                            fonction.ajout_pc_user()
                        
                        time.sleep(2)
                    
                    elif commande == "t" :

                        os.system("clear")
                        print("Ticket en cours :")
                        print("------------------------")

                        while True :
                            
                            liste = fonction.tickets_en_cours()

                            liste_id = [str(id[0]) for id in liste]
                            print(liste_id)
                            command = input("Entrez le numéro du ticket pour voir ce ticket en détail (Q : quitter) ")

                            if command in liste_id :

                                os.system("clear")

                                resultat_pc = crud.select_carnet()
                                command = int(command)

                                print("Numéro PC :", resultat_pc[command-1][0])
                                print("Marque PC : ", resultat_pc[command-1][1])
                                for i in range(len(liste[0])):
                                    print(liste[command-1][i])
                                    print("------------------------")
                                
                                commande = input("m : ecrire un message, c : cloturer un ticket, q : quitter ")

                                if commande == "m" :
                                    
                                    id_ticket = liste[command-1][0]
                                    
                                    prenom_user = fonction.select_id_user(command-1)
                                    chat_bot = input("Entrez votre message ici : ")
                                    
                                    envoi = input("e : envoyer, a : annuler ")
                                    
                                    if envoi == "e" :
                                        crud.chat_ticket(id_ticket, prenom_user, chat_bot)

                                    elif envoi == "a" :
                                        break

                                    else :
                                        fonction.afficher_erreur()
                                    

                                elif commande == "c":
                                    pass

                                elif commande == "q" :
                                    pass

                                else :
                                    fonction.afficher_erreur()

                            elif command == "q" :
                                break

                            else :
                                fonction.afficher_erreur()

                    elif commande == "q" :
                        break

                    else :
                        fonction.afficher_erreur()
            
            else :

                #ecran accueil utilisateur
                while True :
                    pass

    elif commande == 3 :
        quitter = False

    else :
        fonction.afficher_erreur()
    