import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import cv2
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from PIL import Image
from keras.preprocessing.image import img_to_array
#from keras.preprocessing.image import load_img
#from keras.utils import np_utils

# Here we are simply storing the labels of the images in parasitized_data and uninfected_data

parasitized_data = os.listdir('C:/<prefix_path>/cell_images/Parasitized/')
print(parasitized_data[:10]) #printing first 10 image's labels of parasitized_data

uninfected_data = os.listdir('C:/<prefix_path>/cell_images/Uninfected/')
print('\n')
print(uninfected_data[:10]) #printing first 10 image's labels of uninfected_data

# Here we are resizing the images and storing the image data into a list called 'data' and labels are stored in list called 'labels'

data = []
labels = []
for img in parasitized_data:
    try:
        img_read = plt.imread('C:/<prefix_path>/slop/cell_images/Parasitized/' + "/" + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(1)
    except:
        None
        
for img in uninfected_data:
    try:
        img_read = plt.imread('C:/<prefix_path>/slop/cell_images/Uninfected/' + "/" + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(0)
    except:
        None
        
# Taking a short test to check if we are able to retrieve images from data

plt.imshow(data[794])
plt.show()

# convertion of list into numpy array for faster processing
image_data = np.array(data)
labels = np.array(labels)

#shuffling contents image_data and labels respectively
idx = np.arange(image_data.shape[0])
np.random.shuffle(idx)
image_data = image_data[idx]
labels = labels[idx]