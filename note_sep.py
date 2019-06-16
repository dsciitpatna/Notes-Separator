#importing all the libraries that we'll require in the process

import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
!pip install matplotlib 
import matplotlib.pyplot as plt
!pip install opencv-python
import cv2

#set the datadir to the path with the training images
datadir = (r"   ")

#creating the categories that will act as labels for our seperator
categories = ["notes", "non-notes"]

for category in categories:
    path = os.path.join(datadir, category)      #gets us the path to iterate over both categories
    for img in os.listdir(path):
        img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)    #reading each image using cv2
        plt.imshow(img_arr, cmap = "gray")
        plt.show()
        break
    break
    
print(img_arr.shape)

#reshaping the images to 150*150 shape using CV2
img_size = 150
new_arr = cv2.resize(img_arr,(img_size, img_size))

#Creating the training data
training_data = []
def create_training_data():
    for category in categories:
        path = os.path.join(datadir, category)      #gets us the path to iterate over both categories
        class_num = categories.index(category)      #assigns 0 and 1 to notes and non-notes
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)    #reading each image using cv2
                plt.imshow(img_arr, cmap = "gray")
                #plt.show()
                training_data.append([new_arr, class_num])
            except exception as e:                #precaution for broken images
                pass
create_training_data()        

#Shuffling the images
print(len(training_data))
import random
random.shuffle(training_data)   #shuffling the notes and non-notes data for better training

x = []
y = []
#x for features and y for labels

for features, labels in training_data:
    x.append(features)
    y.append(labels)

#While using Keras, x has to be a numpy array
x = np.array(x).reshape(-1, img_size, img_size, 1)
print(x.shape)

import pickle                            #using pickle to save the data
pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("x.pickle", "rb")
x = pickle.load(pickle_in)
pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

#normalising the data
x = x/255.0

#defining the model
model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(128,(3,3), activation = 'relu', input_shape = x.shape[1:]),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation = 'relu'),
        tf.keras.layers.Dense(1, activation = 'sigmoid')
        ])
        
        
from tensorflow.keras.optimizers import SGD
model.compile(optimizer = SGD(lr = 0.05),
             loss = 'binary_crossentropy',
             metrics= ['accuracy'])
             
#now set datadir to the path where the test images are located
datadir = (r"    ")

#Creating the test data in the same way as done for training data
categories = ["notes", "non-notes"]

for category in categories:
    path = os.path.join(datadir, category)      #gets us the path to iterate over both categories
    for img in os.listdir(path):
        img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)    #reading each image using cv2
        plt.imshow(img_arr, cmap = "gray")
        plt.show()
        break
    break
img_size = 150
new_arr = cv2.resize(img_arr,(img_size, img_size))
test_data = []
def create_test_data():
    for category in categories:
        path = os.path.join(datadir, category)      #gets us the path to iterate over both categories
        class_num = categories.index(category)      #assigns 0 and 1 to notes and non-notes
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)    #reading each image using cv2
                plt.imshow(img_arr, cmap = "gray")
                #plt.show()
                test_data.append([new_arr, class_num])
            except exception as e:                #precaution for broken images
                pass
create_test_data()        

print(len(test_data))
import random
random.shuffle(test_data)

test_img =[]
test_label = []

for features, labels in test_data:
    test_img.append(features)
    test_label.append(labels)

test_img = np.array(test_img).reshape(-1, img_size, img_size, 1)
print(test_img.shape)    

import pickle                            #using pickle to save the data
pickle_out = open("test_img.pickle", "wb")
pickle.dump(test_img, pickle_out)
pickle_out.close()

pickle_out = open("test_label.pickle", "wb")
pickle.dump(test_label, pickle_out)
pickle_out.close()

pickle_in = open("test_img.pickle", "rb")
test_img = pickle.load(pickle_in)
pickle_in = open("test_label.pickle", "rb")
test_label = pickle.load(pickle_in)

test_img = test_img/255.0

#Training the model
model.fit(x, y, batch_size =16, epochs = 500)

#Testing the model
model.evaluate(test_img, test_label)
