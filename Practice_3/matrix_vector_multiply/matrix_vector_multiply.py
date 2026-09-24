# c 
def matrix_vector_multiply(matr, vec):
    res = []
    for i in range(len(matr)):
        ans = 0
        for j in range(len(matr[i])):
            ans += matr[i][j] * vec[j] 
        res.append(ans)
    return res


# matrix_vector_multiply([[1, 2, 3], [4, 5, 6]], [1, 1, 1])