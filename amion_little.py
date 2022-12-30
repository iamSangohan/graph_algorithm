import copy
count = 0
matrix = [['.',780,320,580,480,660],
          [780,'.',700,460,300,200],
          [320,700,'.',380,820,630],
          [580,460,380,'.',750,310],
          [480,300,820,750,'.',500],
          [660,200,630,310,500,'.']
        ]

liste_solution = []  

def sumMin(matrix:list):
    global count
    count+=1
    mat = copy.deepcopy(matrix)
    sumM = 0
    for i in range(len(mat)):
        line = mat[i]
        minimum = 99999999
        for j in range(len(mat[i])):
            element = mat[i][j]
            if not isinstance(element,int) :
                pass
            else:
                if element < minimum:
                    minimum = element
        if minimum == 99999999:
            continue
        sumM += minimum
        for j in range(len(line)):
            if not isinstance(mat[i][j], int): pass
            else: mat[i][j] -= minimum
            
    for i in range(len(mat)):
        minimum = 999999999
        for j in range(len(mat)):
            elementCol = mat[j][i]
            if not isinstance(elementCol, int) :
                pass
            else:
                if elementCol < minimum:
                    minimum = elementCol
        if minimum == 999999999:
            continue
        if minimum == 0:
            pass
        else:
            sumM += minimum
            for j in range(len(mat)):
                if not isinstance(mat[j][i], int): pass
                else:
                    mat[j][i] -= minimum
    return sumM,mat

def regret(matrix, liste_solution:list[list], val):
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
                    minCol = min(col)
                regretList.append([i,j,minLine+minCol])
    max = 0
    regretMax = []
    # print('La liste des regrets de cette etape est :', regretList)
    for element in regretList:
        if element[2] > max:
            regretMax = element
            max = regretMax[2]
    if max == 0:
        for element in regretList:
            if element[2] == max:
                regretMax = element
                max = regretMax[2]
    # print(mat)
    
    #Suppression de la ligne et la colonne du regret
    # print('le regret max :', regretMax)
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
    
    if count == 1:
        liste_solution.append([regretMax[0],regretMax[1],val+regretMax[2]+sumMin(matrix)[0]])
    else:
        liste_solution.append([regretMax[0],regretMax[1],liste_solution[-1][2]+sumMin(matrix)[0]])
    print('liste :', liste_solution)
    if liste_solution:
        initial = liste_solution[0]
        dernier = liste_solution[-1]
        x=dernier[1]
        y=initial[0]
        matReduit[x][y] = '.'
    return regretMax,matReduit

#
#
#Credit au compte github "fleury12"
def ranger(solution:list[list], indice):
    a=solution[indice]
    j=indice+1
    while j< len(solution):
        if a[1]== solution[j][0]:
            break
        j=j+1
    return j

def little(matrix : list[list]):
    
    # print('------------------')
    # print('matrix :', matrix)
    sumM,newMat = sumMin(matrix)
    # print('Somme min :', sumM)
    regretMax,Mat= regret(newMat, liste_solution, sumM)
    # print('regret max :', regretMax)
    # print('somme min:', sumM) 
    if regretMax[2] != 0:
        little(Mat)
        
#
#
#Credit au compte github "fleury12"
def ordonner(liste_solution):      
    i=0
    while i< len(liste_solution)-1:
        a= ranger(liste_solution,i)
        b= liste_solution.pop(a)
        liste_solution.insert(i+1, b)
        i=i+1
    return liste_solution

def chemin(liste_solution):
    tab_chemin = []
    for soltuion in liste_solution:
        tab_chemin.append(' '+str(soltuion[0])+'_'+str(soltuion[1])+' ')
    
    return ''.join(tab_chemin)

little(matrix)
print("La matrice de depart est :" ,matrix)
print("Liste des solutions dans le desordre :",liste_solution)
print(f'Liste des solutions dans le ordre{ordonner(liste_solution)}')
print(f'Chemin {chemin(ordonner(liste_solution))}')