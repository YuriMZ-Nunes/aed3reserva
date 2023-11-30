from sys import maxsize
INT_MAX = maxsize

# métodos heurísticos
    ## heurística construtiva inserção do vizinho mais proxima
    
def nearestNeighbor(matrix):
    
    visited = [] # contem o index dos vertices que ja foram visitados
    sum = 0
    minIndex = 0
    origin = 0

    # True  se o peso for menor que o menor armazenado até então,
    #       se o vertice ja foi visitado,
    #       se o vertice não for a origem
    def checkEdge(edge, min, i, visited):
        return edge < min and i not in visited  and i != 0

    # True se o for esta no ultimo vertice da matriz
    def checkLastVertex(i, vertex):
        return i == len(vertex)

    # inicializa o vertice, o minimo e o index do minimo a cada iteração para a comparação
    def initEdgeToCompair(matrix):
        return  matrix, INT_MAX, 0
        
    for i in range(len(matrix[0])):
        vertex, min, minIndex = initEdgeToCompair(matrix[minIndex])
        
        if checkLastVertex(i, vertex):
            sum += vertex[0]

        for j in range(len(vertex)):
            if vertex[j] != 0:
                if checkEdge(vertex[j], min, j, visited):
                    min = vertex[j]
                    minIndex = j
                    
        visited.append(minIndex)
        sum += vertex[minIndex]

    return sum
            
            
            
    





