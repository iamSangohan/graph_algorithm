
n = 5
matrice_adjacence = [[0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 1],
                    [0, 0, 1, 1, 0]]
colors = ['rouge', 'bleu', 'jaune', 'gris', 'noir']

def degre(matrice):
    taille = len(matrice)
    liste = []
    
    for i in range(taille):
        degre = 0
        for j in range(taille):
            if matrice[i][j]==1:
                degre += 1
        liste.append([degre, i, ''])
    #Trie la liste obtenue en fonction du premier (les degres) puis l'ordre normal s'il y a egalité
    liste_trie = sorted(liste, key=lambda x: (x[0], -x[1]), reverse=True)
    #print(liste_trie)
    
    return liste_trie
    
liste = degre(matrice_adjacence)
    
    
def colorier(matrice, liste, colors):
    #Tant que tous les somments ne sont pas encore coloriés
    while any(not bool(elem[2]) for elem in liste):
        for couleur in colors:
            for i in liste:
                if i[2]=='':
                    i[2] = couleur
                    for j in liste:
                        if matrice[i[1]][j[1]] == 0:
                            if j[2]=='':
                                j[2] = couleur
                    break
            
    #print(liste)
    return liste

print('Les couleurs à utiliser sont : ', colors)
print('Nous devons colorier le graphe suivant : ', matrice_adjacence)
print('La liste decroissante des degres est : ', liste)
print('Le resultat final est : ', colorier(matrice_adjacence, liste, colors))