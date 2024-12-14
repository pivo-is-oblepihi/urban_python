def get_matrix (n,m,value):
    matrix = []
    s = []
    for j in range(m):
        s.append(value)
    for i in range(n):
        matrix.append(s)
    return matrix
result=get_matrix(0,2,13)
print(result)