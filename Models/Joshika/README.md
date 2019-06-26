# Notes-Separator

## Aim of project

In a student's life notes are very useful during exam time, which are often found in any average college's student's phone in the form of images. But after exams are over, they are of no use. Also our gallery section is filled with random scattered images which take unwanted extra space. Notes-separator is programmed to classify the notes and the non-notes images.

---

## Dataset

Dataset that is used to train the model can be found here <https://drive.google.com/folderview?id=1aM19cJwlfLTzQnE8y6K-gdKuWfCyf0YC>.
The above dataset contains total of 900 images (aprox.) 
1. 800 notes images (aprox.).
2. 100 non-notes images (aprox).

Size of each image has to be resized to 128*128

---

## Libraries used

1. Numpy
2. Tensorflow
3. Matplotlib (for visualizing images and other plots)
4. CV2 
5. OS
6. Keras

---

## Model Inputs and features

1. The model showed maximum accuracy when the learning rate was set to 0.003.
2. It consist of **4 convolution layers**. Number of nuerons in each layer from top to bottom are as follows 32,64,64,128. With **ReLU** used as activation function with padding and strides used occasionally.
3. Results are then flattened to be fed into **DNN**.
4. There are **2 Dense fully connected layers** each consisting of 64 and 40 neurons respectively.
5. Lastly **1 more dense layer** consisting of single neuron has been used for the output with **sigmoid** as activation function.


---

## Accuracy 
 
* Test acc. **90%**
* Training acc. **99%**
* Validation acc. **98%**


---

## Application

**Notes-Separator has a great role to play in a student's life, more into 'managing it'. The project is a great example of the use of machine learning in day to day life.**


---

## Learning Experience

This project helped me to learn the following.
1. CNN and DNN
2. Agumentation technique
3. Optimizers
4. Organising the dataset
5. Hyperparameter tuning
