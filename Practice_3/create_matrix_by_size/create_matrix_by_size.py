# b
import random 

def create_matrix_by_size(M, N):
    m = [[random.random() for i in range(N)] for j in range(M)]
    print(m)
   

# create_matrix_by_size(3, 2)
