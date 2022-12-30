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
    # print('------------------------------')
    # for line in mat:
        # print(line)
    sumM = 0
    for i in range(len(mat)):
        line = mat[i]
        minimum = 99999999
        for j in range(len(mat[i])):
            element = mat[i][j]
            if not isinstance(element,int) :
                pass
            else:
                if element<minimum:
                    minimum = element
        sumM += minimum
        for j in range(len(line)):
            if not isinstance(mat[i][j], int): pass
            else: mat[i][j] -= minimum
        # print(line)
    # print(mat)
    # print("................................................")
    for i in range(len(mat)):
        minimum = 999999999
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
    #print(sumM)
    return sumM,mat

def regret(matrix):
    mat = copy.deepcopy(matrix)
    regretList = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0 : pass
            else:
                line = mat[i].copy()
                line.remove(mat[i][j])
                line = [x for x in line if x != '.']
                if len(line)==0:
                    minLine = 0
                else:
                    minLine = min(line)
                col = [mat[a][j] for a in range(len(matrix))]
                col.remove(mat[i][j])
                col = [x for x in col if x!='.']
                if len(col)==0:
                    minCol = 0
                else:
                    # print(f'mat\n  {mat} \n \n col {col} \n \n ')
                    minCol = min(col)
                regretList.append([i,j,minLine+minCol])
    max = 0
    for element in regretList:
        if element[2] >= max:
            regretMax = element
            max = regretMax[2]
    if len(mat[0])>2:
        mat[regretMax[1]][regretMax[0]] = '.'
        # print(f'chemin inv\n  {mat}\n \n  regret {regretList} \n MAx')
    
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
            
    return regretMax,matReduit
    
def little(matrix : list, val = 0):
    sumM,newMat = sumMin(matrix)
    regretMax,Mat = regret(newMat)
    print('-----------------')
    print('val :',val)
    print('matrice :',matrix)
    racine = sumM
    if regretMax[2] != 0:
        gauche = [regretMax[0],regretMax[1],racine+regretMax[2],False]    
        tree = [gauche,racine,[regretMax[0],regretMax[1],little(Mat,racine),True]]
        print(tree)
    
    
    
    
    # return newMat,tree,val

# def recurLittle(matrix:list)->list:
#     tree = []
#     recurLittle(matrix, tree,0)
        
little(matrix)

