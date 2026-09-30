
def mat_mat_mult(a, b):
    a_x = len(a[0])
    a_y = len(a)
    b_x = len(b[0])
    b_y = len(b)
    if (a_x != b_y and a_y != b_x):
        print('Ошибка размерностей!')
    else:
        ans_mat = [[0 for i in range(b_x)] for j in range(a_y)]
        for i in range(len(ans_mat)):
            for j in range(len(ans_mat[0])):
                for k in range(a_x):
                    ans_mat[i][j] += a[i][k] * b[k][j]
        return ans_mat
        
        
def mat_vec_mult(matr, vec):
    res = []
    for i in range(len(matr)):
        ans = 0
        for j in range(len(matr[i])):
            ans += matr[i][j] * vec[j] 
        res.append(ans)
    return res

        
def matrix_trace(matr):
    sum = 0
    N = len(matr[0])
    for i in range(N):
        sum += matr[i][i]    
    return(sum)

def dot_product(a, b):
    if len(a) != len(b):
        print('Ошибка размерности!')
    else:
        ans = 0
        for i in range(len(a)):
            ans += a[i] * b[i]
        return ans
    
    
def hist(vec, num_bins):
    hi, lo = max(vec), min(vec)
    interval_width = (hi - lo) / num_bins
    bins = [0 for i in range(num_bins)]
    for i in range(len(vec)):
        idx = min(int((vec[i] - lo) / interval_width), num_bins - 1)
        bins[idx] += 1
    return bins
    
    
def conv(vec, kern):
    if (len(kern) > len(vec)):
        print('Ошибка размерности!')
    else:
        res = [0 for i in range(len(vec) - len(kern) + 1)]
        for i in range(len(vec) - len(kern) + 1):
            for j in range(len(kern)):
                res[i] += vec[i + j] * kern[j]
        return res     
    
def work_with_files(file_name, option, data = ''):
    if (option == 'r'):
        f = open(file_name,'r')  # открыть файл из рабочей директории в режиме чтения
        print(f.read())
        f.close()
    elif (option == 'w'):
        f = open(file_name,'w')  # открыть файл из рабочей директории в режиме чтения
        f.write(data)
        f.close()
    else:
        print('Неизвестная опция!')
        

        
    
    
    
# if __name__ == "__main__":
    # a = np.array([[2, -3, 1], [5, 4, -2]])
    # b = np.array([[-7, 5], [2, -1], [4, 3]])
    # print(mat_mat_mult(a, b))
    
    # print(mat_vec_mult([[1, 2, 3], [4, 5, 6]], [1, 1, 1]))
    
    # print(dot_product([1, 2, 3], [4, 5, 6]))

    # print(hist([1, 1.8, 3, 4, 5], 5))
    
    # print(conv([1, 2, 3, 4, 6], [-1, 0, -1]))
    
    # work_with_files('test.txt', 'w', '123\n123')