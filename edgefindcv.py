import cv2

class EdgeFinder:
    def __init__(self, image, filter_size=1, threshold1=0, threshold2=0):          #defining default values
        self.image = image
        self._filter_size = filter_size
        self._threshold1 = threshold1
        self._threshold2 = threshold2

        cv2.namedWindow('edges')

        cv2.createTrackbar('threshold1', 'edges', self._threshold1, 127)        
		#self._threshold1 is the default vaule and 127 is the max value of threshold1 variable
        cv2.createTrackbar('threshold2', 'edges', self._threshold2, 255)
        cv2.createTrackbar('filter_size', 'edges', self._filter_size, 25)

        self._render()           #render is defined below
        cv2.waitKey(0)
        cv2.destroyWindow('edges')
        
		#getting values from user (if necessary)
    def threshold1(self):
        return self._threshold1
    def threshold2(self):
        return self._threshold2
    def filterSize(self):
        return self._filter_size
    def edgeImage(self):
        return self._edge_img
    def smoothedImage(self):
        return self._smoothed_img

    def _render(self):
	    #smoothing the image, sigmaX and sigmaY are the standard deviations in the X and Y directions
        self._smoothed_img = cv2.GaussianBlur(self.image, (self._filter_size, self._filter_size), sigmaX=0, sigmaY=0)
        #canny edge detecion, self._threshold1 and self._threshold2 are the min and max values respectively		
        self._edge_img = cv2.Canny(self._smoothed_img, self._threshold1, self._threshold2) 
        cv2.imshow('smoothed', self._smoothed_img)
        cv2.imshow('edges', self._edge_img)