def transpose (matrix):
    new_matrix = []
    if len(matrix) != 0:
        for n in range(len(matrix[0])):
            new_matrix.append([])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[j].append(matrix[i][j])

    return new_matrix

def powers (matrix, start, end):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(start, end + 1):
            new_matrix[i].append(matrix[i]**j)
    return new_matrix

def matmul (matrix1, matrix2):
    new_matrix = []
    
    for i in range(len(matrix1)):
        new_matrix.append([])
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            new_matrix[i].append(sum)
    return new_matrix

def invert (matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a*d - b*c

    new_matrix = [[d/det, -b/det], [-c/det, a/det]]

    return new_matrix

def