# Initialisation des données
etudiants = []
cours = []

while True:
    # Affichage du menu [cite: 1, 2]
    print("\n=== MENU GESTION ÉTUDIANTS ===")
    print("1. Enregistrer un étudiant")
    print("2. Enregistrer la liste des cours")
    print("3. Saisir / modifier les notes")
    print("4. Calculer les moyennes et décisions")
    print("5. Afficher tous les étudiants")
    print("6. Rechercher un étudiant")
    print("7. Statistiques")
    print("8. Classement")
    print("9. Quitter")
    
    choix = input("Votre choix : ")

    # OPTION 1 : Enregistrer un étudiant [cite: 3, 4, 5]
    if choix == "1":
        while True:
            mat = input("Matricule : ").strip()
            if not mat: continue # Obligatoire [cite: 4]
            # Vérifier si existe déjà [cite: 3, 5]
            existe = False
            for e in etudiants:
                if e["matricule"] == mat: existe = True
            if existe: 
                print("Erreur : Matricule déjà utilisé")
                break
            
            nom = input("Nom : ").strip()
            prenom = input("Prénom : ").strip()
            if not nom or not prenom: continue # Obligatoire [cite: 4]
            
            sexe = input("Sexe (M/F) : ").upper()
            while sexe not in ["M", "F"]:
                sexe = input("Sexe invalide (M/F) : ").upper()
            
            try:
                age = int(input("Âge : "))
                if age <= 0: raise ValueError
            except:
                print("Âge invalide")
                continue
                
            # Création du dictionnaire 
            nouvel_etudiant = {
                "matricule": mat, "nom": nom, "prenom": prenom,
                "sexe": sexe, "age": age, "notes": {},
                "moyenne": 0.0, "decision": "Non calculée"
            }
            etudiants.append(nouvel_etudiant)
            print("Étudiant enregistré !")
            break

    # OPTION 2 : Enregistrer les cours [cite: 6, 7, 8]
    elif choix == "2":
        mode = "1"
        if cours:
            print("1. Remplacer la liste / 2. Étendre la liste")
            mode = input("Choix : ")
        
        if mode == "1": cours = []
        
        try:
            nb = int(input("Nombre de cours à ajouter : "))
            for i in range(nb):
                while True:
                    nom_c = input(f"Nom du cours {i+1} : ").strip()
                    if nom_c and nom_c not in cours:
                        cours.append(nom_c)
                        break
                    print("Nom vide ou déjà existant")
        except: print("Entrée invalide")

    # OPTION 3 : Saisir/Modifier les notes [cite: 9, 10, 11, 12]
    elif choix == "3":
        if not cours: # Bloqué si pas de cours 
            print("Erreur : Enregistrez d'abord des cours (Option 2)")
            continue
            
        mat = input("Matricule de l'étudiant : ")
        cible = None
        for e in etudiants:
            if e["matricule"] == mat: cible = e
            
        if not cible:
            print("Étudiant non trouvé")
        else:
            print(f"Cours disponibles : {cours}")
            for c in cours:
                # Gestion de la modification [cite: 11]
                if c in cible["notes"]:
                    print(f"Note existante pour {c} : {cible['notes'][c]}")
                    rep = input("Remplacer ? (O/N) : ").upper()
                    if rep != "O": continue
                
                # Validation de la note [cite: 10]
                while True:
                    try:
                        n = float(input(f"Note pour {c} (0-20) : "))
                        if 0 <= n <= 20:
                            cible["notes"][c] = n
                            break
                        else: print("La note doit être entre 0 et 20")
                    except: print("Saisie invalide")

    # OPTION 4 : Moyennes et Décisions
    elif choix == "4":
        if not etudiants or not cours:
            print("Données insuffisantes")
        else:
            for e in etudiants:
                if len(e["notes"]) == len(cours):
                    moy = sum(e["notes"].values()) / len(cours)
                    e["moyenne"] = round(moy, 2)
                    e["decision"] = "Admis" if moy >= 10 else "Ajourné"
            print("Calculs terminés")

    # OPTION 5 : Afficher tous les étudiants
    elif choix == "5":
        print(f"{'Mat':<10} {'Nom':<15} {'Moy':<6} {'Décision'}")
        for e in etudiants:
            print(f"{e['matricule']:<10} {e['nom']:<15} {e['moyenne']:<6} {e['decision']}")

    # OPTION 6 : Rechercher un étudiant
    elif choix == "6":
        mat = input("Matricule à rechercher : ")
        for e in etudiants:
            if e["matricule"] == mat:
                print(f"Trouvé : {e['nom']} {e['prenom']} - {e['decision']}")

    # OPTION 7 : Statistiques
    elif choix == "7":
        if etudiants:
            admis = [e for e in etudiants if e["decision"] == "Admis"]
            taux = (len(admis) / len(etudiants)) * 100
            print(f"Taux de réussite : {taux:.2f}%")

    # OPTION 8 : Classement
    elif choix == "8":
        if etudiants:
            tri = sorted(etudiants, key=lambda x: x["moyenne"], reverse=True)
            print("TOP :", tri[0]["nom"])
            print("DERNIER :", tri[-1]["nom"])

    # OPTION 9 : Quitter [cite: 1]
    elif choix == "9":
        print("Au revoir !")
        break
    
    else:
        print("Choix invalide, recommencez.")
