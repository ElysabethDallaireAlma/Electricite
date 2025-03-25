
def obtenir_donnees(numero_quartier):
    match numero_quartier:
        case 1: # Quartier des Peintres
            # Amperage maximum / Nombre de sorties maximum / Prises (A) / Interrupteurs (Nombre et A)

            # Inscription des données du quartier (chaque maison)
            maison_1 = [ [20, 6, [0.5, 0.25, 0.15], [[2, 0.02], [4, 0.15]]],        # Disjoncteur #1
                        [16, 8, [1, 2, 0.5, 5], [[10, 0.5], [2, 2.5], [5, 0.25]]],  # Disjoncteur #2
                        [20, 6, [2, 1], [[2, 1.5]]]]                                # Disjoncteur #3
            
            # Initialisation des variables de contenu
            maisons_du_quartier = [maison_1]
            modele_disjoncteurs = [[]]
            
        case 2: # Quartier des Oiseaux

            # Inscription des données du quartier (chaque maison)
            maison_1 = [ [20, 6, [0.25, 0.5, 0.5], [[1, 30], [2, 0.1]]], [20, 6, [1, 2, 0.5, 5], [[10, 0.5], [2, 2.5], [5, 0.25]]]]
            maison_2 = [ [16, 8, [1, 2, 0.5, 2, 0.1, 0.8], [[45, 0.01]]], [16, 8, [3], [[1, 1], [2, 0.2], [3, 0.05]]]]

            # Initialisation des variables de contenu
            maisons_du_quartier = [maison_1, maison_2]
            modele_disjoncteurs = [[], []]

        case 3: # Quartier des Écrivains

            # Inscription des données du quartier (chaque maison)
            maison_1 = [ [20, 12, [2, 1, 0.75, 0.25, 0.10, 0.85, 0.25], [[1, 1], [2, 0.8]]], [16, 8, [3, 0.5], [[5, 0.85], [6, 1]]]]
            maison_2 = [ [32, 1, [], [[1, 25]]], [20, 1, [4.5], []], [20, 12, [3, 1, 1, 1], [[5, 0.75]]], [20, 6, [0.8, 0.25], [[1, 2], [2, 0.15]]], [16, 8, [2, 0.33, 0.45, 1, 0.11, 0.89, 0.23], []]]
            maison_3 = [ [32, 1, [30], []], [20, 1, [], [[10, 1],[3, 2]]], [16, 8, [3, 2, 1], [[5, 1.5]]]]
            maison_4 = [ [20, 12, [1, 2, 0.5, 5, 0.1, 0.8], [[45, 0.01]]], [16, 8, [3], [[1, 1], [2, 0.2], [3, 0.05]]], [20, 6, [3, 1], [[2, 0.5]]], [32, 1, [16], []], [20, 1, [], [[1, 20]]]]
            
            # Initialisation des variables de contenu
            maisons_du_quartier = [maison_1, maison_2, maison_3, maison_4]
            modele_disjoncteurs = [[], [], [], []]
        
        case 4: # Quartier Saint-Jacques

            # Inscription des données du quartier (chaque maison)
            maison_1 = [[20, 1, [19], []], [16, 8, [1, 4, 0.5, 0.25], [[4, 0.1]]]]
            maison_2 = [[20, 6, [1, 1, 1, 1, 1, 1], []], [16, 8, [5], [[2, 4], [1, 4]]], [32, 1, [15], [[1, 17]]]]
            maison_3 = [[20, 1, [], []]]
            maison_4 = [[20, 6, [0.5, 0.1, 0.025], [[4, 5]]], [16, 8, [1, 2, 8, 15], [[3, 4]]], [20, 6, [10, 1, 1], [[2, 2]]], [16, 8, [2, 2, 2, 2, 2], [[3, 2]]]]
            maison_5 = [[16, 8, [2, 1, 1, 2], [[2, 4], [2, 8]]], [20, 1, [8], [[2, 1]]], [20, 12, [3, 2, 1], [[4, 0.5], [5, 0.25]]]]
            maison_6 = [[32, 1, [25, 45], [[1, 0.5]]], [20, 12, [0.8, 0.25, 0.075, 0.15, 0.25, 0.3], [[4, 0.25], [2, 0.85]]]]
            maison_7 = [[20, 6, [5, 1, 2, 0.5, 0.28], [[4, 0.10], [3, 0.25]]], [20, 1, [15], []], [20, 12, [2, 1, 2, 1, 5], [[4, 75]]], [16, 8, [2, 0.5, 0.15, 0.25, 2], [[4, 0.25]]]]
            maison_8 = [[20, 12, [0.25, 0.25, 0.25, 0.25], [[6, 1]]], [16, 8, [1, 10], []], [32, 1, [], [[1, 33]]]]
            maison_9 = [[20, 12, [0.8, 0.25, 0.75, 0.45, 1, 3, 0.25, 0.05], [[3, 2], [4, 0.15]]]]
            maison_10 = [[20, 12, [12], []], [16,8, [2, 4], [[3, 8]]], [32, 1, [2], [[1, 30]]], [20, 1, [], [[2, 10]]], [20, 6, [1, 2, 3, 4], [[1, 5]]]]
            
            # Initialisation des variables de contenu
            maisons_du_quartier = [maison_1, maison_2, maison_3, maison_4, maison_5, maison_6, maison_7, maison_8, maison_9, maison_10]
            modele_disjoncteurs = [[], [], [], [], [], [], [], [], [], []]
        
        case _: # Quartier par défaut
            print("Choix invalide. Cas par défaut")
            maison_1 = [ [20, 6, [1, 0.8], [[1, 0.5], [3, 1]]], [16, 8, [3, 4, 0.8, 0.25], [[12, 0.05], [6, 1.25]]]]
            maisons_du_quartier = [maison_1]
            modele_disjoncteurs = [[]]

    return maisons_du_quartier, modele_disjoncteurs
