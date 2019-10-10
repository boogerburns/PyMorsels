def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        combined.append(row)
    return combined
