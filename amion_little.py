import copy

matrix = [['.',780,320,580,480,660],
          [780,'.',700,460,300,200],
          [320,700,'.',380,820,630],
          [580,460,380,'.',750,310],
          [480,300,820,750,'.',500],
          [660,200,630,310,500,'.']
        ]

def sumMin(matrix:list):
    mat = copy.deepcopy(matrix)
    sumM = 0
    for i in range(len(mat)):
        line = mat[i]
        minimum = 99999999
        for j in range(len(mat[i])):
            #On recherche le min de chaque ligne de la matrice 
            element = mat[i][j]
            if not isinstance(element,int) :
                pass
            else:
                if element<minimum:
                    minimum = element
        #On additionne tous les min des lignes de la matrice 
        sumM += minimum
        #On retire le min sur toute la ligne 
        for j in range(len(line)):
            if not isinstance(mat[i][j], int): pass
            else: mat[i][j] -= minimum
        # print(line)
    # print(mat)
    # print("................................................")
    for i in range(len(mat)):
        minimum = 999999999
        #On fait pareil pour les colonnes
        for j in range(len(mat)):
            elementCol = mat[j][i]
            if not isinstance(elementCol, int) :
                pass
            else:
                if elementCol<minimum:
                    minimum = elementCol
        if minimum == 0:
            pass
        else:
            sumM += minimum
            for j in range(len(mat)):
                if not isinstance(mat[j][i], int): pass
                else:
                    # print(mat[j][i])
                    mat[j][i] -= minimum
                    # print(mat[j][i])
    return sumM,mat

def regret(matrix):
    mat = copy.deepcopy(matrix)
    regretList = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0 :
                #On met tous les elements de la ligne dans un tableau puis on prend le min
                line = mat[i].copy()
                line.remove(mat[i][j])
                line = [x for x in line if x != '.']
                minLine = min(line)
                #On met tous les elements de la colonne dans un tableau puis on prend le min
                col = [mat[a][j] for a in range(len(matrix))] 
                col.remove(mat[i][j])
                col = [x for x in col if x != '.']
                minCol = min(col)
                regretList.append([i,j,minLine+minCol])
    max_value = 0
    regretMax = []
    #print(regretList)
    for element in regretList:
        if element[2] > max_value:
            regretMax = element
            max_value = regretMax[2]
    print(regretMax)      
    #Suppression de la ligne et la colonne du regret
    col = regretMax[1]
    line = regretMax[0]
    matReduit = copy.deepcopy(matrix)
    for i in range(len(matReduit)):
        if i == line:
            for j in range(len(matReduit[i])):
                matReduit[i][j] = "."
        for j in range(len(matReduit[i])):
            if j == col:
                matReduit[i][j] = "."
    
    return regretMax, mat

mat = sumMin(matrix)[1]
print(regret(mat)[1])

def little(matrix : list):
    ## tree = [g,r,d]
    tree = []
    t = {}
    val,newMat = sumMin(matrix)
    regretMax = regret(newMat)
    tree["valeur"]

    t[str(regretMax[0])+str(regretMax[1])+'_'] = val+regretMax[2]
    tree[val] = [t,tree]
    # tree.append([[val+regretMax[2]],val,tree])
    print(tree)

little(matrix)

# def ajouter_noeud(arbre, valeur):
#     if arbre is None:
#         arbre = {}
#         arbre['valeur'] = valeur #Valeur va etre un tableau avec les sommets et la valeur du trajet
#         arbre['gauche'] = None
#         arbre['droit'] = None
#     elif valeur < arbre['valeur']:
#         arbre['gauche'] = ajouter_noeud(arbre['gauche'], valeur)
#     else:
#         arbre['droit'] = ajouter_noeud(arbre['droit'], valeur)
#     return arbre