from __future__ import division
from numpy import array, zeros, abs
from numpy.fft import fft2, ifft2           #this is for discrete fourier transform (fft2 is for 2D data and ifft2 is inverse fourier transform on 2D data)
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def gaussian(im):
    b = array([[2, 4,  5,  4,  2],
               [4, 9,  12, 9,  4],
               [5, 12, 15, 12, 5],
               [4, 9,  12, 9,  4],
               [2, 4,  5,  4,  2]]) / 156;
    k = zeros(im.shape)
    k[:b.shape[0], :b.shape[1]] = b
    fim = fft2(im)
    fk = fft2(k)
    fil_im = ifft2(fim * fk)
    return abs(fil_im).astype(int)       #returning numpy array with absolute interger values

if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:                                  #counting the length of arguments
        print "Usage: python %s <image>" % argv[0]
        exit()
    im = array(Image.open(argv[1]))                    #taking input
    im = im[:, :, 0]
    gray()                                             #changing to grey 
    subplot(1, 2, 1)                                   #creating a plot to obtain image
    imshow(im)
    axis('off')
    title('Original')
    subplot(1, 2, 2)
    imshow(gaussian(im))                               #gaussian function is called here   
    axis('off')
    title('Filtered')
    show()