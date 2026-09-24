# f
def find_sum_diag_elems(matr):
    sum = 0
    N = len(matr[0])
    for i in range(N):
        sum += matr[i][i]
    
    return(sum)


# find_sum_diag_elems([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
