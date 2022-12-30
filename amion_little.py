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
            if mat[i][j] != 0 : pass
            else:
                line = mat[i].copy()
                line.remove('.'),line.remove(mat[i][j])
                minLine = min(line)
                col = [mat[a][j] for a in range(len(matrix))]
                col.remove('.'), col.remove(mat[i][j])  
                minCol = min(col)
                regretList.append([i,j,minLine+minCol])
    max = 0
    for element in regretList:
        if element[2] > max:
            regretMax = element
            max = regretMax[2]
    
    return regretMax

def little(matrix : list):
    ## tree = [g,r,d]
    tree = []
    val,newMat = sumMin(matrix)
    regretMax = regret(newMat)
    tree.append([[val+regretMax[2]],val,tree])
    print(tree)
    
little(matrix)