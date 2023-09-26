import math

# Computes the transpose of a matrix
def transpose (matrix):
    new_matrix = []
    # If the matrix is not empty
    if len(matrix) != 0:
        # For each column in the matrix create a new row
        for n in range(len(matrix[0])):
            new_matrix.append([])
        
        # For each row in the matrix append the values to the new matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[j].append(matrix[i][j])

    return new_matrix

# Computes the powers of a matrix
def powers (matrix, start, end):
    new_matrix = []
    # For each row in the matrix
    for i in range(len(matrix)):
        new_matrix.append([])
        # For each column in the matrix
        for j in range(start, end + 1):
            # Add the power of the matrix to the new matrix
            new_matrix[i].append(math.pow(matrix[i], j))
    return new_matrix

# Computes the product of two matrices
def matmul (matrix1, matrix2):
    new_matrix = []
    
    # For each row in the first matrix
    for i in range(len(matrix1)):
        new_matrix.append([])
        # Loop through first matrix row
        for j in range(len(matrix2[0])):
            sum = 0
            
            # For each column in the second matrix
            for k in range(len(matrix2)):
                # Add the product of the two matrices to the new matrix
                sum += matrix1[i][k] * matrix2[k][j]
            new_matrix[i].append(sum)
    return new_matrix

# Computes the inverse of a matrix
def invert (matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # Compute the determinant
    det = a*d - b*c

    # Compute the new matrix
    new_matrix = [[d/det, -b/det], [-c/det, a/det]]

    return new_matrix

# Loads a matrix from a file
def loadtxt (file):
    new_matrix = []
    inp_file = open(file)

    # For each line in the file
    for line in inp_file:
        new_matrix.append([])
        stripped_line = line.strip()
        splitted_line = stripped_line.split()

        # For each number in the line
        for num in splitted_line:
            # Add the number to the new matrix
            new_matrix[-1].append(float(num))

    inp_file.close()
    return new_matrix