# g
def find_conv(img, kern):
    img_x = len(img[0])
    img_y = len(img)
    kern_x = len(kern[0])
    kern_y = len(kern)
    ans = [[0 for i in range(img_x - kern_x + 1)] for j in range(img_y - kern_y + 1)]
    for i in range(img_y - kern_y + 1):
        for j in range(img_x - kern_x + 1):
            res = 0
            for k in range(kern_y):
                for l in range(kern_x):
                    res += kern[k][l] * img[i+k][j+l]
            ans[i][j] = res
    return ans


# find_conv([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0], [0, 1]])
