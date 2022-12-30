import copy
# le nombre de sommet
#j'ai réprésenté l'infini par (0,0)

#cette fonction me permet de représenter infini par (0,0)
def mettre_infini(mat):
    i=0
    while i<len(mat):
        j=0
        while j<len(mat):
            if i==j:
                mat[i][j]=(0,0)
            j=j+1
        i=i+1
    return mat


#cette fonction me permet de déterminer les min des ligne et de faire la soustraction
#je m'arange à ignoré les (0,0)
def soustraire_min_ligne(mat:list[list]):
    i=0
    min=0
    # regrets_liste=[]
    while i<len(mat):
        j=0
        min_ligne=999999
        k=0
        while j<len(mat[i]):
            if type(mat[i][j])== int:
                k=k+1
                if min_ligne> mat[i][j]:
                    min_ligne= copy.deepcopy(mat[i][j])
            j=j+1
        if k==0:
            i=i+1
    
        else:
            j=0
            while j<len(mat[i]):
                if type(mat[i][j])== int:
                    mat[i][j]= mat[i][j]-min_ligne
                j=j+1
            i=i+1
            min=min+min_ligne
            print(f"le min des lignes est {min_ligne}")
    return mat, min #, regrets_liste
#cette fonction me permet de déterminer les min des colones et de faire la soustraction
def soustraire_colone( mat:list[list]):
    i=0
    min=0
    
    while i< len(mat[0]):
        k=0
        min_colonne=99999
        j=0
        print(f"colone:{i}")
        while j< len(mat):
            if type(mat[j][i])== int:
                k=k+1
                if min_colonne>mat[j][i]:
                    min_colonne=copy.deepcopy(mat[j][i])
            j=j+1
        print(f"k= {k}")
        if k==0:
            i=i+1
        else:
            j=0
            while j< len(mat):
                if type(mat[j][i])== int:
                    mat[j][i]=mat[j][i]-min_colonne
                j=j+1
            i=i+1
            print(f"le min est {min_colonne}\n")
            min= min+min_colonne
    return mat,min #,liste_regrets

#on va calculer les regrets
#je cherche min des ligne sauf le zero considéré 
def minimum_ligne(mat:list,indice_ligne, indice_colone):
    min=99999
    i=0
    n=0
    print(f"ligne: {indice_ligne}")
    while i< len(mat[indice_ligne]):
        print(f"elemet:{mat[indice_ligne][i]}")
        print(i)
        if i!=indice_colone  :
            print(f"different de l'indice")
            if (type(mat[indice_ligne][i]) == int) :
                n=n+1
                print(f"type int")
                if (mat[indice_ligne][i]<min) :
                    print("lien")
                    min= mat[indice_ligne][i]
            elif (type(mat[indice_ligne][i]) == list):
                n=n+1
                min=0
        
        i=i+1
    if n==0:
        return (0,0)
    else:
        print(f"le min de la linge {indice_ligne} est {min}")
        return min
#je cherche min des colones sauf le zero considéré 
def minimum_colone(mat:list, indice, ligne_indice):
    min=9999
    j=0
    n=0
    while j< len(mat):
        if (type(mat[j][indice])== int and min>mat[j][indice]) and j!= ligne_indice  :
            min=copy.deepcopy(mat[j][indice])
            n=n+1
        elif type(mat[j][indice])== list and j!= ligne_indice:
            print("list1")
            min=0 
            n=n+1
        j=j+1
    if n==0:
        return (0,0)
    else:
        print(f"le min de la colone {indice} est {min}")
        return min

#les deux fonction suivante me permetrons de créer les (0,0) / infini après calcul du regret
def suprime_colone(mat:list[list], indice):
    i=0
    while i<len(mat):
        mat[i][indice]=(0,0)
        i=i+1
    return mat
def suprime_ligne(mat:list[list],indice):
    i=0
    while i< len(mat[indice]):
        mat[indice][i]= (0,0)
        i=i+1
    return mat




#voici la fonction qui utlise les deux précédente pour calculer le regret

def regret(mat:list, liste_regret:list[tuple], liste_solution:list[list]):
    k=0
    j=0
    #la liste regret me permet d'avoir la position des zéros dans la matrice
    while k< len(liste_regret):
        print(f"\nzero considéré{liste_regret[k]}")
        print(mat)
        i=liste_regret[k][0]
        j=liste_regret[k][1]
        min_des_ligne= minimum_ligne(mat,i,j)
        min_des_col= minimum_colone(mat,j,i)
        if (type( min_des_ligne)!= tuple and  type( min_des_col)!= tuple ):
            a=copy.deepcopy(min_des_ligne+min_des_col)
            mat[i][j]= [copy.deepcopy(a)]
            print(f"regret calculé : {a}")
            liste_regret[k]= liste_regret[k] + (a,)
            print(f"le regret final {liste_regret[k]}")
            k=k+1
        else:
            j=20
            break
    if j!=20 :
        k=0
        max_regret=0
        indice_regret=(0,0)
        print(f"rrrrrrrrr{liste_regret}")
        #la liste de regret me permet de garder la position de tous les zéro considéré
        while k< len(liste_regret):
            if max_regret< liste_regret[k][2]:
                max_regret=liste_regret[k][2]
                indice_regret=(liste_regret[k][0],liste_regret[k][1])
            elif max_regret== liste_regret[k][2]:
                if liste_regret[k][1]<indice_regret[1]:
                    max_regret=liste_regret[k][2]
                    indice_regret=(liste_regret[k][0],liste_regret[k][1])
            k=k+1
        #je vais remplacer tous les regret par zero sauf le max
        print(f"je remplace les zero par les regrets")
        print(f"\n la matrice avec regret: {mat}\n le,regret max {max_regret} \n indice est {indice_regret}\nliste des regrets {liste_regret}")
        element_liste_regret = indice_regret + (max_regret,)
        for element in liste_regret:
            if element != element_liste_regret:
                i=element[0]
                j= element[1]
                mat[i][j]=0
        print(f"\n la matrice avec regret final: {mat}\n")
        #je vais suprimer la ligne et colone du regret
        #par supression je vais remplacer tous les éléments de la ligne et de la colone par (0,0)
        #supression ligne
        mat=suprime_ligne(mat,indice_regret[0])
        #supression colone
        print(f"{mat}\n")
        mat=suprime_colone(mat,indice_regret[1])
        print(indice_regret)
        #on va mettre à l'infini(ici je represente l'infini par un tuple(0,0)) les chemin aboutissant à une sous tournée
        #par exemple si on avait suprimmer la ligne N et la colone B, on doit mette à l'infini BN
        print(f"\n{indice_regret[1]} \n{indice_regret[0]}")
        print(mat)
        liste_solution.append(element_liste_regret)
        initial = liste_solution[0]
        dernier = liste_solution[-1]
        x=dernier[1]
        y=initial[0]
        mat[x][y]=(0,0)
        print(f"\n après suppression on a: {mat}")
        
        return mat, element_liste_regret,liste_solution
    else:
        return 0
#cette fonction me permet de trouver les zéro dans la matrice et 
#les conserve dan une liste afin de pouvoir caluculer le regret après
def trouve_regret(matrice:list[list]):
    liste=[]
    i=0  
    while i<len(matrice):
        j=0
        while j< len(matrice[i]):
            if type( matrice[i][j]== int):
                if matrice[i][j]== 0:
                    liste.append((i,j))
            j=j+1
        i=i+1
    return liste

#cette fonction compte le nombre d'infini dans la matrice
def compte(mat):
    i=0
    n=0
    while i< len(mat):
        j=0
        while j< len(mat):
            if type(mat[i][j])==tuple:
                n=n+1
            j=j+1
        i=i+1
    return n

#cette fonction me rammen la position du prochain itinérair à prendre à par tir 
#de du chemin de l'indice dans la liste solution
def ranger(solution:list[list], indice):
    a=solution[indice]
    j=indice+1
    while j< len(solution):
        if a[1]== solution[j][0]:
            break
        j=j+1
    return j
# voici l'algorithme générale de little
#il faut mettre le nombre de sommet en paramettre
def algorthme_little(matrice:list, nombre_sommet):
    list_regret=[]
    liste_solution=[]
    tableau= mettre_infini(matrice)
    nb= compte(matrice)
    n=0
    itération= nombre_sommet*nombre_sommet -3
    #le nombre maximal d'infini est n*n
    #or nous nous arreton losrqu'il y a 3 zéro dans la matrice
    #d'ou la condition d'arret nb < itération
    while nb < itération:
        n=n+1
        print(f"*****************************************étape taille: {n}")
        print(tableau)
        #je fais la soustractio des lignes
        soust_col= soustraire_min_ligne(tableau)
        print(f"min_ligne= {soust_col[1]}\n  {soust_col[0]}")
        minimum= soust_col[1]
        #je fais la soustractio des lignes
        soust_ligne= soustraire_colone(tableau)
        list_regret= trouve_regret(soust_ligne[0])
        minimum= minimum +soust_ligne[1]
        print(f"\nmin_colone= {soust_ligne[1]} regret:{list_regret}\n {soust_ligne[0]}")
        #je calcul le regret
        resultat= regret(soust_ligne[0], list_regret, liste_solution)
        #je verifie si j'ai affaire à une linge ou colonne suprimée
        if type(resultat)== tuple:
            matrice=resultat[0]
            print(liste_solution)
            if n<2:
                #pour le premier element je prend juste la somme min_col et min_ligne
                distance=minimum
                final=list(resultat[1])
                final[2]=distance
                liste_solution=resultat[2]
                liste_solution.pop(-1)
                liste_solution.append(final)
            else:
                #pour le reste, je prend le précedent et j'ajoute la somme des min_ligne et min_col
                a= list( liste_solution[-2])
                print(a)
                print(minimum)
                distance= minimum+a[2]
                print(distance)
                b = list( liste_solution[-1])
                b[2]= distance
                liste_solution[-1]= copy.deepcopy(b)
            print(f"liste des solution : {liste_solution}\n{distance}")
            list_regret.clear()
        else:
            pass
        tableau= matrice
        minimum=0
        nb= compte(tableau)
    #on va ajouter les derniere solution qui sont dans la matrice
    #elle sont toute null
    i=0
    while i< len(matrice):
        j=0
        while j< len(matrice):
            if matrice[i][j]==0:
                a= (i,j)
                a= a +(liste_solution[-1][2],)
                liste_solution.append(list(a))
            j=j+1
        i=i+1
    print(f"\nla solution non rangée\n {liste_solution}")
    #on va maintenant déterminer le chemin adequat
    i=0
    while i< len(liste_solution)-1:
        a= ranger(liste_solution,i)
        b= liste_solution.pop(a)
        liste_solution.insert(i+1, b)
        i=i+1
    print(f"solution final: {liste_solution}")
    print("le chemin final est \n")
    for elem in liste_solution:
        print(f" {elem[0]}_{elem[1]} ", end="")

Matrice_adj = [[0, 780, 320, 580, 480,660],
     [780, 0, 700, 460, 300,200],
     [320,700, 0, 380, 820,630],
     [580, 460, 380, 0,750,310],
     [480, 300, 820, 750,0,500],
     [660, 200, 630, 310,500,0]]
algorthme_little(Matrice_adj,6)
