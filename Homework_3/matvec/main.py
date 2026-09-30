from matvec import *
import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # разница между конечным и начальным временем
        elapsed_time = end_time - start_time
        with open('res.txt', 'a') as f:
            print(func.__name__, ':', file = f)
            print(args, file = f)
            print('res =', result, file = f)
            print('Elapsed time: ', elapsed_time, file = f)
            print('\n', file = f)
            f.close()
        return result
    return wrapper

mat_mat_mult = calc_time(mat_mat_mult)
mat_vec_mult = calc_time(mat_vec_mult)
matrix_trace = calc_time(matrix_trace)
dot_product = calc_time(dot_product)
hist = calc_time(hist)
conv = calc_time(conv)

a = [[2, -3, 1], [5, 4, -2]]
b = [[-7, 5], [2, -1], [4, 3]]
mat_mat_mult(a, b)

a = [[1, 2, 3], [4, 5, 6]]
b = [1, 1, 1]
mat_vec_mult(a, b)


a = [[1, 2], [3, 4]]
matrix_trace(a)



a = [1, 2, 3]
b = [4, 5, 6]
dot_product(a, b)

a = [1, 1.8, 3, 4, 5]
b = 5
hist(a, b)    

a = [1, 2, 3, 4, 6]
b = [1, 0, 1]
conv(a, b)

    
    
    
    