# graph_algorithm
Implementation des algorithmes de Welsh and Powell, de Christofides et de Little

----------------------WELSH and POWELL----------------------

Welsh and Powell est un algorithme de coloration de graphe. Il permet de determiner le nombre chromatique d'un graphe donné

  -1e etape : On va classer les sommets de la matrice par ordre decroissant de leur degré 
  
  -2e etape : En parcourant la liste faites a l'etape 1, on va attribuer une couleur non encore attribuée au premier sommet non encore colorié. Puis on se crée petit liste des sommets non adjacent a notre sommet colorié et on va colorier avec la meme couleur les sommets non coloriés et non adjacents a un sommet qui a deja cette coouleur
  
  -3e etape : S'il y a encore des sommets non encore coloriés alors on repart a l'etape 2
Cet algo a été implementé en python.
