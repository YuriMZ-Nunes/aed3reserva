""" def cheapEdge(matrix):
    
    vertexLen = len(matrix[0])
    cicle = []
    vertexCicle = set()
    
    currentVertex = 0
    vertexCicle.add(currentVertex)
    cicle.append(currentVertex)
    
    while len(vertexCicle) < vertexLen:
        minIndex = None
        min = float('inf')
        
        for v in range(vertexLen):
            if v not in cicle:
                for u in cicle:
                    if matrix[u][v] < min:
                        
    
    
    return 0 """