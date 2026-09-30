import numpy as np

def processing(image, alpha, beta):
    corr_image = [[0 for i in range(len(image[0]))] for j in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            corr_image[i][j] = alpha * image[i][j] + beta
    return np.array(corr_image)