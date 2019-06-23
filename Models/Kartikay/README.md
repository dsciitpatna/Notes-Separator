# Note separator

## Aim

In a student's life notes are very useful during exam time .But after exams are over, they are of no use also our gallery section is filled with random scattered images which take's extra space and even the gallery looks bad .Note separator is programmed to detect notes images automatically and to delete the notes images.

---

## Dataset

Dataset that is used to train the model can be found at <https://drive.google.com/open?id=1y-YYS6_XE_ClmshJPhKNIiixedT6Rnkn>.
The above dataset contains total of 1500 images (aprox.) 
1. 850 notes images (aprox.).
2. 650 non-notes images (aprox).

Size of each image is -->300X300

---

## Libraries used

1. Tensorflow (high level keras api is used)
2. Scikit learn
3. Matplotlib (for visualizing images and other plots)
4. CV2 and OS

---

## Model Inputs and features

1. The model showed maximum accuracy when the learning rate was reduced to 0.01.
2. It consist of **5 convolution layers**. Number of nuerons in each layer from top to bottom are as follows 32,64,128,256,512. With **RELU** used as activation function and **l2 regularizer** in each layer.
3. Results are then flattened to be fed into **DNN**.
4. There are **2 Dense fully connected layer** each consisting of 50 nuerons .
5. Lastly **1 more dense layer** consisting of single nueron for the output with **sigmoid** as activation function.
6. Since dataset was small techniques like **Data Agumentation** had to be used.


---

## Accuracy 
 
* Test acc. **87%**
* Training acc. **97%**
* Validation acc. **95%**


---

## Application

**Note Seperator has a great role to play in a student's life, more into 'managing it'. The project is a great example of use of machine learning in day to day life.**


---

## Learning Experience

This project helped me to learn the following.
1. CNN and DNN
2. Agumentation technique
3. Optimizers
4. Using callbacks
5. Confusion matrix
6. Use of PIL (python imaging library)



       
 

