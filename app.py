import nearestNeighbor

# código para ler o arquivo contendo a matriz
with open('tsp_data/teste.txt', 'r') as matrixTxt:
    lines = matrixTxt.readlines()
        
matrix = [[0] * len(lines) for _ in range(len(lines))]

for i, line in enumerate(lines):
    values = [int(x) for x in line.split()]
    matrix[i] = values
    
sum = nearestNeighbor.nearestNeighbor(matrix)

print(sum)