# d
def print_matrix(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(f'{matr[i][j]:^5}', end = '')
        print()    
    
# print_matrix([[1, 2, 3], [4, 5, 6]])
    