matrice_adjacence = [[0, 2, 5, 0, 0],
                    [2, 0, 3, 2, 0],
                    [5, 3, 0, 5, 1],
                    [0, 2, 5, 0, 3],
                    [0, 0, 1, 3, 0]]

def has_cycle(taille, edges):
    #Vérifier que taille est bien un entier
    if not isinstance(taille, int):
        raise TypeError("taille doit être un entier")
    
    #Tableau pour noter les noeuds deja visités
    visited = [False for _ in range(taille)]
  
    #Fonction récursive de parcours en profondeur
    def dfs(node, parent):
        #Marquer le noeud comme visité
        visited[node] = True
        
        #Parcourir les voisins du noeud
        for a, b, _ in edges:
            if a == node:
                neighbor = b
            elif b == node:
                neighbor = a
            else:
                continue
            if neighbor < 0 or neighbor >= taille:
                continue
            if not visited[neighbor]:
                #On ontinue le parcours en profondeur si le voisin n'a pas été visité
                if dfs(neighbor, node):
                    return True
            #Si le voisin a déjà été visité et n'est pas le parent, il y a un cycle
            elif neighbor != parent:
                return True
        return False
    
    #Parcourir tous les noeuds du graphe
    for node in range(taille):
        if not visited[node]:
        #Continuer le parcours en profondeur à partir de ce noeud s'il n'a pas été visité
            if dfs(node, -1):
                return True
    return False
             
    
def kruskal(matrice):
    #Onn va creer une liste d'arrete avec leur poids en supprimer les arretes de poids 0
    liste_arrete = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != 0:
                liste_arrete.append((i, j, matrice[i][j]))
    #print('Non triée', liste_arrete)
    #Maintenant on va les trier dans l'ordre croissant 
    liste_arrete = sorted(liste_arrete, key=lambda x:(x[2]) , reverse=False)
    #print('Triée :', liste_arrete)
    liste_acm = []
    for arrete in liste_arrete:
        #Cette condition permet de verifier si l'arrete n'existe pas deja dans la liste 
        if any(bool((arrete[0]==elem[0] or arrete[0]==elem[1]) and (arrete[1]==elem[0] or arrete[1]==elem[1])) for elem in liste_acm)==False:
            liste_acm.append(arrete)
            if has_cycle(len(liste_acm), liste_acm)==True:
                liste_acm.remove(arrete)
    #print('ACM : ', liste_acm)
    
    return liste_acm
    
acm = kruskal(matrice_adjacence)

def degre_impair(liste):
    liste_sommets = []
    # print('liste : ', liste)
    for i in range(len(liste)+1): 
        # print('---------')  
        # print(i) 
        total = 0
        for j in range(len(liste)):
            # print(liste[j])
            if liste[j][0] == i or liste[j][1] == i:
                # print('OK')
                total += 1
        liste_sommets.append([i, total])
    # print('degre', liste_sommets)
    sommets_impairs = [sommet for sommet in liste_sommets if sommet[1] % 2 == 1]
    # print('Sommets impairs:', sommets_impairs)
    
    return sommets_impairs


degre_i = degre_impair(acm)

def couplage_min(matrice, sommets):
    for i in sommets:
        a = i[1]
        liste = []
        for j in sommets[0]:
            liste.append(matrice[a][j])
        liste.sort(reverse=False)
        
#BON JE SUIS BLOQUE SUR LE COUPLAGE. JE REPRENDS CA BIENTOT