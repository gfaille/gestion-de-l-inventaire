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

                    """ boucle while affiche l'ecran d'accueil 

                        affiche :
                        le nombre de pc prêter
                        le nombre de ticket en cour
                        le nombre de ticket terminé

                        demande a l'utilisateur :
                        créer un nouvelle ordinateur (ajout un ordinateur dans la base de données)
                        assigne un pc a un utilisateur
                        voir ses ticket en cour (en détail)  
                        quitter
                    """
                    
                    print("Statistique : ")
                    print("------------------------")
                    print("Nombre de pc en prêts : ", crud.calcul_pc())
                    print("Nombre de ticket en cours : ", crud.tickets("En cours"))
                    print("Nombre de ticket terminés : ", crud.tickets("terminé"))
                    print("------------------------")
                    commande = input("P: crée un nouveau ordinateur,    A: ajoute un pc a un utilisateur,   \nT: voir vos tickets,    Q: quitter ")

                    if commande == "p" :

                        """ si command est égal a "p" alors

                            on efface se qui précéde dans la console (pour une meilleur affichage)
                            demande a l'admin combien de pc qu'il veut créer

                            boucle for qui repete selon le nombre de pc qui veut créer
                                fonction qui ajout les pc 
                        """
                        
                        os.system("clear")
                        nb_pc = int(input("combien de pc voulez-vous crée : "))

                        for _ in range(nb_pc) :
                            fonction.ajout_ordinnateur()
                    
                    elif commande == "a" :

                        """ si command est égal a "a" alors

                            on efface se qui précéde dans la console (pour une meilleur affichage)
                            affiche les utilisateur et les ordinateur
                            demande combien de pc seront assigner a un utilisateur

                            boucle for qui repete selon le nombre de pc qui veut assigné a un utilisateur 
                                fonction pour assigné un pc a un utilisateur
                        """
                        
                        os.system("clear")
                        print(crud.select_user_admin(), crud.select_ordinateur())
                        pc_pret = int(input("combien d'utilisateur seront assigner a un ordinateur "))

                        for _ in range(pc_pret) :
                            fonction.ajout_pc_user()
                        
                        time.sleep(2)
                    
                    elif commande == "t" :

                        """ si command est égal a "t" alors

                            on efface se qui précéde dans la console (pour une meilleur affichage)
                            affiche "tickets en cours :" et une séparation
                        """

                        os.system("clear")
                        print("Ticket en cours :")
                        print("------------------------")

                        while True :

                            """ boucle while pour afficher les tickets en cours

                                variable qui contient ce que retourne la fonction ticket_en_cours

                                variable qui contient une liste avec une boucle for pour avoir que les id
                                affiche la liste des id
                                demande a l'admin d'entrez le numéro du ticket ou de quitter
                            """
                            
                            liste = fonction.tickets_en_cours()

                            liste_id = [str(id[0]) for id in liste]
                            print(liste_id)
                            command = input("Entrez le numéro du ticket pour voir ce ticket en détail (Q : quitter) ")

                            if command in liste_id :

                                """ si command est égal à l'id de la liste alors

                                    on efface se qui précéde dans la console (pour une meilleur affichage)

                                    stocke dans une variable :
                                    se qui est selection dans le crud 
                                    command entrez par l'admin en entier (pour éviter tout probleme)

                                    affiche :
                                    le numéro du pc
                                    la marque du pc

                                    boucle for qui repete selon la longeur de la liste
                                        affiche la liste (une fois l'id puis le message)
                                    
                                    demande a l'utilisateur :
                                    écrire un message
                                    cloturer le ticket 
                                    quitter
                                """

                                os.system("clear")

                                resultat_pc = crud.select_carnet()
                                command = int(command)
                                chat = crud.chat(command)

                                print("Numéro PC :", resultat_pc[command-1][0])
                                print("Marque PC : ", resultat_pc[command-1][1])
                                for i in range(len(liste[0])):
                                    print(liste[command-1][i])
                                    print("------------------------")
                                for j in range(len(chat)) :
                                    print(chat[j][0])
                                    print("------------------------")
                                
                                commande = input("m : ecrire un message, c : cloturer un ticket, q : quitter ")

                                if commande == "m" :

                                    """ si commande est égal à "m" alors

                                        stocke dans des variables :
                                        liste [command-1][0] pour avoir la bonne ligne et colone (id)

                                        fonction pour avoir le prenom de l'utilisateur
                                        message ecrit par l'admin

                                        demande a l'admin d'envoyer ou annuler
                                    """
                                    
                                    id_ticket = liste[command-1][0]
                                    
                                    prenom_user = fonction.select_id_user(command-1)
                                    chat_bot = input("Entrez votre message ici : ")
                                    
                                    envoi = input("e : envoyer, a : annuler ")
                                    
                                    if envoi == "e" :

                                        """ si envoi est égal à "e" alors 

                                            envoi les donner dans le crud pour enregistre dans la base de données 
                                        """
                                        crud.chat_ticket(id_ticket, prenom_user, chat_bot)

                                    elif envoi == "a" :

                                        """ si envoi est égal à "a" alors

                                            sorti de la boucle
                                        """
                                        break

                                    else :

                                        #sinon affiche message d'erreur
                                        fonction.afficher_erreur()
                                    

                                elif commande == "c":

                                    """ si commande est égal à "c" alors

                                        stocke dans une variable :
                                        liste [command-1][0] pour avoir la bonne ligne et colone (id)

                                        envoi l'id pour mettre a jour la base de données
                                    """

                                    id_ticket = liste[command-1][0]
                                    
                                    crud.mise_a_jour(id_ticket)


                                elif commande == "q" :

                                    """ si envoi est égal à "q" alors

                                        sorti de la boucle
                                    """

                                    break

                                else :

                                    #sinon affiche message d'erreur
                                    fonction.afficher_erreur()

                            elif command == "q" :

                                """ si envoi est égal à "q" alors

                                    sorti de la boucle
                                """

                                break

                            else :

                                #sinon affiche message d'erreur
                                fonction.afficher_erreur()

                    elif commande == "q" :

                        """ si envoi est égal à "q" alors

                            arrêt total
                        """
                        exit()

                    else :

                        #sinon affiche message d'erreur
                        fonction.afficher_erreur()
            
            else :

                #ecran accueil utilisateur
                while True :

                    """ boucle while qui affiche l'ecran d'accueil utilisateur

                        efface se qui precede
                        affiche les ordinateur qui sont assigner a l'utilisateur

                        si commande est egal a "t" alors
                            efface se qui precede
                            appel la fonction ticket (pour creer un ticket)
                        
                        est si commande est egal a "v" alors
                            une boucle while
                                efface se qui precede
                                variable qui stocke et affiche les ticket de l'utilisateur
                                variable qui stocke les id des ticket en str
                                demande a l'utilisateur d'entrez la reference du pc
                                
                                si command est dans la liste_id alors
                                    efface se qui precede
                                        on stocke dans des variable :
                                        - l'index de liste_id 
                                        - le ticket selectionner
                                        - le carnet de l'utilisateur
                                        - le chat ticket
                                    affiche ses ticket et le chat
                                    on demande soit decrire un message ou fermer

                                    si commande est egal a "m" alors
                                        on stocke l'id du ticket
                                        le prenom de l'utilisateur
                                        le message entrez par l'utilisateur

                                        on demande a l'utilisateur de l'envoyer ou l'annuler

                                        si commande est egal a "e" alors 
                                            envoi le message dans la bdd
                                        est si commande est egal a "a" alors
                                            annule le message

                        est si commande est egal a "q" alors
                            on break
                        sinon affiche l'erreur 
                    """
                    
                    os.system("clear")
                    print("ordinateur qui vous est assigner ")
                    result = crud.select_carnet_user(user[0])

                    for i in range(len(result)):
                        print(result[i])   
                    
                    commande = input("t : créer un ticket, v : voir ses ticket q : quitter ")

                    if commande == "t" :

                        os.system("clear")
                        fonction.ticket()
                    
                    elif commande == "v":
                        
                        while True :

                            os.system("clear")
                            liste = fonction.ticket_user(user[0])

                            liste_id = [str(id[0]) for id in liste]
                            print(liste_id)
                            command = input("entrez la refence du pc, q : quitter ")


                            if command in liste_id :

                                os.system("clear")
                                ref_pc = liste_id.index(command)
                                resultat = crud.select_ticket_user(liste_id[ref_pc])
                                resultat_pc = crud.select_carnet_user(user[0])
                                chat = crud.chat(resultat[0][0])

                                print(resultat_pc[ref_pc][0])
                                print(resultat_pc[ref_pc][2])

                                for i in range(len(resultat[0])):
                                        print(resultat[0][i])
                                        print("------------------------")

                                for j in range(len(chat)) :
                                    print(chat[j][0])
                                    print("------------------------")
                                
                                commande = input("m : ecrire un message, q : quitter ")

                                if commande == "m" :

                                    id_ticket = resultat[0][0]
                                    prenom_user = user[2]
                                    chat_bot = input("Entrez votre message ici : ")
                                    
                                    envoi = input("e : envoyer, a : annuler ")
                                    
                                    if envoi == "e" :

                                        """ si envoi est égal à "e" alors 

                                            envoi les donner dans le crud pour enregistre dans la base de données 
                                        """
                                        crud.chat_ticket(id_ticket, prenom_user, chat_bot)
                                        print("message bien envoyer")
                                        break

                                    elif envoi == "a" :

                                        """ si envoi est égal à "a" alors

                                            sorti de la boucle
                                        """
                                        break

                                    else :

                                        #sinon affiche message d'erreur
                                        fonction.afficher_erreur()

                                elif commande == "q" :
                                    break

                            else :
                                fonction.afficher_erreur()
                        
                    elif commande == "q" :

                        """ si envoi est égal à "q" alors

                            arrêt total
                        """
                        exit()

                    else :
                        fonction.afficher_erreur()

    elif commande == 3 :
        quitter = False

    else :
        fonction.afficher_erreur()
    