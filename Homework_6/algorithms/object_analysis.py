"""
Шаблонный метод (Template method)
"""
import cv2
import matplotlib.pyplot as plt 
import numpy as np
import random as rng

class ObjectAnalysis(object):
    def template_method(self, image):

        image = self.noise_filtering(image)
        data = self.segmentation(image)
        data = self.object_parameters(data)

        return data

    def noise_filtering(self, image):
        raise NotImplementedError()

    def segmentation(self, data):
        raise NotImplementedError()

    def object_parameters(self, data):
        (image, data) = data
        (numLabels, labels, stats, centroids) = data
        x = []
        y = []
        w = []
        h = []
        area = []
        for i in range(1, numLabels):
            # extract the connected component statistics for the current
            # label
            x.append(stats[i, cv2.CC_STAT_LEFT])
            y.append(stats[i, cv2.CC_STAT_TOP])
            w.append(stats[i, cv2.CC_STAT_WIDTH])
            h.append(stats[i, cv2.CC_STAT_HEIGHT])
            area.append(stats[i, cv2.CC_STAT_AREA])

        return (x, y, w, h, area)


class BinaryImage(ObjectAnalysis):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        median = cv2.medianBlur(image, 5)
        return median

    def segmentation(self, image):
        output = cv2.connectedComponentsWithStats(
            image,
            4, # connectivity
            cv2.CV_32S)
        return (image, output)

class MonochromeImage(BinaryImage):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        blurred = cv2.GaussianBlur(image, (15, 15), 0)
        plt.imshow(image, cmap = 'gray')
        plt.show()
        plt.imshow(blurred, cmap = 'gray')
        plt.show()
        return blurred

    def segmentation(self, image):
        edges = cv2.Canny(image, 50, 100)
        output = cv2.connectedComponentsWithStats(
            edges,
            4, 
            cv2.CV_32S)
        plt.imshow(image, cmap = 'gray')
        plt.show()
        plt.imshow(edges, cmap = 'gray')
        plt.show()
        return (image, output)

class ColorImage(MonochromeImage):
    def __init__(self):
        pass

    def segmentation(self, image):
        bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(bw, 40, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        dist = cv2.distanceTransform(bw, cv2.DIST_L2, 3)
        cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
        _, dist = cv2.threshold(dist, 0.4, 1.0, cv2.THRESH_BINARY)
        
        kernel1 = np.ones((3,3), dtype=np.uint8)
        dist = cv2.dilate(dist, kernel1)
        dist_8u = dist.astype('uint8')
        contours, _ = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        markers = np.zeros(dist.shape, dtype=np.int32)
        for i in range(len(contours)):
            cv2.drawContours(markers, contours, i, (i+1), -1)
        cv2.circle(markers, (5,5), 3, (255,255,255), -1)
        
        cv2.watershed(image, markers)
        
        markers[markers == -1] = 0
        output = cv2.connectedComponentsWithStats(
            markers, 
            4, 
            cv2.CV_32S)
        return (image, output)
        
 

"""
Декоратор - структурный паттерн
"""

class FilteredAnalysis(ObjectAnalysis):
    def __init__(self, obj):
        self._proc = obj

    def template_method(self, image):
        (_x, _y, _w, _h, _area) = self._proc.template_method(image)
        x = []
        y = []
        w = []
        h = []
        area = []
        moments_list = []

        for i in range(len(_area)):
            if _area[i] > 10 and _area[i] < 2500:
                x.append(_x[i])
                y.append(_y[i])
                w.append(_w[i])
                h.append(_h[i])
                area.append(_area[i])

                mask = np.zeros((h[-1], w[-1]), dtype = np.uint8)
                
                mask.fill(255)
                mu = cv2.moments(mask)
                moments_list.append(mu)
                
                if mu['m00'] != 0:
                    cx = mu['m10'] / (mu['m00'] + 1e-5)
                    cy = mu['m01'] / (mu['m00'] + 1e-5)
                else:
                    cx, cy = 0, 0
                    
                print(f" * Object[{i}] - Area (M_00) = {mu['m00']:.2f} - Center: ({cx:.2f}, {cy:.2f})")
        
        return (x,y,w,h,moments_list)


if __name__== '__main__':
    print("Binary Image Processing")
    bin_segm = BinaryImage()
    (x,y,w,h,area) = bin_segm.template_method(cv2.imread('./data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
            print([x[i], y[i], w[i],h[i],area[i]])

    print("Decorated Binary Image Processing")
    filt_bin = FilteredAnalysis(BinaryImage())
    (x, y, w, h, area) = filt_bin.template_method(cv2.imread('./data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
            print([x[i], y[i], w[i],h[i],area[i]])

    print("\nMonochrome Image Processing (Gaussian + Canny)")
    mono_segm = MonochromeImage()
    (x, y, w, h, area) = mono_segm.template_method(cv2.imread('./data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])