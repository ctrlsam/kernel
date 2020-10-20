import numpy as np
from PIL import Image

blur = [
    [0.06250, 0.1250, 0.0625],
    [0.125,   0.25,   0.125],
    [0.0625,  0.125,  0.0625]
]

def get_grayscale_pixels(img_path):
    img = Image.open(img_path)
    img = img.convert('L')
    return np.asarray(img)

def get_new_pixel_value(matrix):
    pixel_value = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            pixel_value += matrix[x][y] * blur[x][y]
    return pixel_value

if __name__ == '__main__':
    pixels = get_grayscale_pixels('dog.jpg')
    new_image = np.empty(pixels.shape)

    for y in range(len(pixels[0])):
        for x in range(len(pixels)):
        
            new_image[x,y] = pixels[x][y]

            try:

                matrix = [
                    [ pixels[x-1][y+1], pixels[x][y+1], pixels[x+1][y+1] ],
                    [ pixels[x-1][y],   pixels[x][y],   pixels[x+1][y]   ],
                    [ pixels[x-1][y-1], pixels[x][y-1], pixels[x+1][y-1] ]
                ]

                #new_image[x,y] = get_new_pixel_value(matrix)
                pass

            except IndexError:
                print('skipped')
                continue
            

    img = Image.fromarray(new_image, 'L')
    img.save('my.png')
    img.show()