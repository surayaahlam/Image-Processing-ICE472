# -*- coding: utf-8 -*-
"""ICE472 LAB-2 (Basic Image Manipulations in Python).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dQOF_jc1wxt3ythEzMBpu-OGXlWln1Vg

##ICE472: Digital Speech & Image Processing
### Summer 2020
# Experiment 2: Basic Image Manipulations in Python


**Name:** Suraya Ahlam

**Student ID:** 2016-1-50-014

## Assignment:

**(1) Running this notebook and producing the outputs.**

### Library Imports
"""

import skimage                        # Imort the Scikit-image Library
from skimage import data              # For loading data from skimage library
import matplotlib.pyplot as plt       # For plotting the image
from skimage import io                # For I/O Operations
from skimage.transform import resize  # Resize Function

"""Lets load a sample camera image from the scikit image **data** library and store it into a variable called **camera**"""

camera = data.camera()

"""Lets check the type of the image using the function **type()**. Usually images are stored as **numpy.ndarray** format."""

type(camera)

"""The dimensions/spatial resolution of the image is returned by the attribute image.**shape**"""

camera.shape

"""Lets check what actually comprises the image? The pixel values."""

camera

"""Let's visualize the image using **plt.imshow()** function followed by the function **plt.show()**"""

plt.imshow(camera)
plt.show()

"""Since this is a black and white image, the function **imshow()** needs an argument **cmap = 'gray'** to render it properly."""

plt.imshow(camera, cmap = 'gray')
plt.show()

"""### Let's Read a color image

You can read in the image by uploading the image 'hello.png' to the **Files** Tab on the left. Then read the image using the **io.imread()** function.
"""

hello = io.imread('hello.png')

"""If you are unable to upload files (mobile users),
You can use a link to load the image.
Here the image link is: https://raw.githubusercontent.com/suhailnajeeb/ete-ice-472/master/experiment-1/hello.png
"""

hello = io.imread('https://raw.githubusercontent.com/suhailnajeeb/ete-ice-472/master/experiment-1/hello.png')

type(hello)

hello.shape

"""As you can see, the last value of the **shape** i.e. the dimension of the matrix **hello** is 3, which indicates that this is a color image. Let's also take a look at the image:"""

hello

plt.imshow(hello)
plt.show()

"""### Resizing Image:"""

astro_img = data.astronaut()

astro_img.shape

plt.imshow(astro_img)

"""the **resize** function is used to resize the image to a certain new shape. For example, here we resize the image to the new shape: **(128, 128, 3)**"""

resized_img = resize(astro_img, (128, 128, 3))
plt.imshow(resized_img)
plt.show()

"""### Slicing/Cropping an Image:"""

plt.imshow(astro_img)
plt.show()

"""We can also crop an image file using its **indices**. For example, ```img[0:200, 100:300]``` crops the image from 0 to 200 pixels along x axis and 100 to 300 along y axis."""

cropped_img = astro_img[0:200, 100:300]
plt.imshow(cropped_img)
plt.show()

"""### Storing Image to File:

The **io.imsave()** function is used to store the image. The first argument is the file name & the second argument is the image array to be stored.
"""

io.imsave('astro_face.jpg', cropped_img)

"""**(2) Choose any image you wish (you can either upload the image file or you can load it with a link) and perform the following operations:**

## Solution to Problem (2):
"""

import skimage
from skimage import data
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize

"""Loading the image into python"""

flower = io.imread('flower.jpg')

"""Checking the shape of the image"""

flower.shape

"""Displaying the image"""

plt.imshow(flower)
plt.show()

"""Resizing the image into 1/2 of its original shape"""

resized_flower = resize(flower, (flower.shape[0]//2, flower.shape[1]//2, 3))

"""Showing the image on screen"""

plt.imshow(resized_flower)
plt.show()

"""Croping a portion of the image"""

cropped_flower = flower[0:400, 0:600]

"""Showing the cropped image on screen"""

plt.imshow(cropped_flower)
plt.show()

"""Saving the image into an image file named 'output.jpg'"""

io.imsave('output.jpg', cropped_flower)

"""## Discussion:

In this experiment, I have learn about basic image manipulations in python. I have learn the python libraries for image manipulation. I have learn how to load a sample image from scikit image data library, upload image and use a link to load image. I learn how to see the shape of the image where I can see either the image is 2-dimentional or 3-dimentional. If it is 2-dimentional then it is black & white image and if it is 3-dimentional then it is color image. I also have learn how to resize, crop, visualize and save an image. At last, now I can do any kind of image manipulations in python.
"""