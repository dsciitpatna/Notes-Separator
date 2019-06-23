#importing all the libraries that we'll require in the process

import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import matplotlib.pyplot as plt
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


#normalising the data
x = x/255.0

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

test_img = test_img/255.0


#Creating validation data
 
#Set datadir to the validation data folder
datadir = (r"    ")
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
validation_data = []
def create_validation_data():
    for category in categories:
        path = os.path.join(datadir, category)      #gets us the path to iterate over both categories
        class_num = categories.index(category)      #assigns 0 and 1 to notes and non-notes
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)    #reading each image using cv2
                plt.imshow(img_arr, cmap = "gray")
                #plt.show()
                validation_data.append([new_arr, class_num])
            except exception as e:                #precaution for broken images
                pass
create_validation_data()        

print(len(validation_data))
import random
random.shuffle(validation_data)

val_img =[]
val_label = []
for features, labels in validation_data:
    val_img.append(features)
    val_label.append(labels)


val_img = np.array(val_img).reshape(-1, img_size, img_size, 1)
print(val_img.shape)
val_img = val_img/255.0


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
             




#Training the model
model.fit(x, y, batch_size =16, epochs = 500)

#Testing the model
model.evaluate(test_img, test_label)

#saving the weights and model
model.save("model.h5")
model.save_weights("weights.h5")