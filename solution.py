"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np

"""
3 - Kwadrat
"""
def square(size, side, start):
    #pass
    image = np.zeros((size,size)).astype(np.uint8)
    image[0:size,0:size] = 0
    image[start[0]:start[0]+side,start[1]:start[1]+side]=255
    return image

"""
3 - Koło
"""
def midcircle(size):
    #pass
    image = np.zeros((size[0],size[1])).astype(np.uint8)
    image[0:size[0],0:size[1]] = 0
    if(size[0]<size[1]):
        r=size[0]/4
    else:
        r=size[1]/4
    
    for i in range(size[0]):
        for j in range(size[1]):
            if((i-size[0]/2)**2+(j-size[1]/2)**2<=r**2):
                image[i,j]=255
                
    return image
    

"""
3 - Szachownica.
"""
def checkerboard(size):
    #pass
    image = np.zeros((size,size)).astype(np.uint8)
    image[0:size,0:size] = 0
    side = size//8
    for i in range(0,8):
        for j in range(0,8):
            if(i%2 == 1 and j%2 == 1 or i%2 == 0 and j%2 == 0):
                image[i*side:(i+1)*side,j*side:(j+1)*side]=255
    return image

"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    src = source.shape
    dst = new_size

    y_src, x_src = src
    x_dst, y_dst = dst

    r_x = x_src / x_dst
    r_y = y_src / y_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy, ix) in np.ndindex(image.shape):
        image[iy, ix] = source[int(iy*r_y), int(ix*r_x)]

    return image

"""
5 - Interpolacja dwuliniowa
"""
def bilinear_interpolation(source, new_size):
    y_src, x_src = source.shape
    x_dst, y_dst = new_size

    r_x = x_src / x_dst
    r_y = y_src / y_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy, ix) in np.ndindex(image.shape):
        y = r_y * iy
        x = r_x * ix

        y_floor = int(np.floor(y))
        y_ceil = int(np.ceil(y))

        x_floor = int(np.floor(x))
        x_ceil = int(np.ceil(x))

        values = [
            source[y_floor, x_floor],
            source[y_ceil, x_floor],
            source[y_floor, x_ceil],
            source[y_ceil, x_ceil],
        ]

        x_fraction = x - np.floor(x)
        y_fraction = y - np.floor(y)

        a = x_fraction
        b = y_fraction

        fa0 = (1-a)*values[0] + a*values[2]
        fa1 = (1-a)*values[1] + a*values[3]

        fab = (1-b)*fa0 + b*fa1
        image[iy, ix] = int(fab)

    return image
