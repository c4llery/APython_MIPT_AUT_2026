import time
from Practice_3.create_matrix_by_size.create_matrix_by_size import create_matrix_by_size
from Practice_3.create_vector_by_size.create_vector_by_size import create_vector_by_size
from Practice_3.find_conv.find_conv import find_conv
from Practice_3.matrix_vector_multiply.matrix_vector_multiply import matrix_vector_multiply
from Practice_3.print_matrix.print_matrix import print_matrix
from Practice_3.print_vector.print_vector import print_vector
from Practice_3.find_sum_diag_elems.find_sum_diag_elems import find_sum_diag_elems



def calc_time(func):
    def wrapper(*args, **kwargs):
        print()
        print(func.__name__)
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # разница между конечным и начальным временем
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)
        print()
        return result
    return wrapper

create_vector_by_size = calc_time(create_vector_by_size)
create_matrix_by_size = calc_time(create_matrix_by_size)
find_conv = calc_time(find_conv)
matrix_vector_multiply = calc_time(matrix_vector_multiply)
print_matrix = calc_time(print_matrix)
print_vector = calc_time(print_vector)
find_sum_diag_elems = calc_time(find_sum_diag_elems)

create_vector_by_size(3)
create_matrix_by_size(3, 2)
find_conv([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0], [0, 1]])
matrix_vector_multiply([[1, 2, 3], [4, 5, 6]], [1, 1, 1])
print_matrix([[1, 2, 3], [4, 5, 6]])
print_vector([1, 2, 3])
find_sum_diag_elems([[1, 2, 3], [4, 5, 6], [7, 8, 9]])





