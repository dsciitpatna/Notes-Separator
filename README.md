<<<<<<< HEAD
# Notes Seperator
Notes Seperator Project under Machine Learning and AI society of **Developer Students Club - IIT Patna**.

## Motivation
Generally, during exams we take many images from notes of other people to study from. And once exams are over, it is a tedious job to find each of the images again and delete them one by one from our gallery.
This is the very motivation for this project - To develop an algorithm that can classify a given image as "image from notes" and "image not from notes".

## Impact
This project will help students to automatically remove images of notes from there gallery automatically without the user looking for any particular image .

## Aim
The aim of the project is to autonomously detect whether a given image is taken from some notes or not. To achieve this, we will use **Convolutional Neural Networks** as our tool.
We will be using different CNN architectures and choose the one with maximum accuracy parameters.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4xUyot0A495vomnp-aAmH7OCrV9AFDQhcoEr2JTmVV0ASl-C7PA)    **Image not from notes**


![](https://qrfellows.files.wordpress.com/2013/11/20120621_1107271.jpg?w=225&h=300)    **Image from notes**

## Prerequisites
1. Basic Deep Learning concepts.
2. Basics of Convolutional Neural Networks.
3. Tools
* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* Basic python libraries used in ML ([Scikit-learn](https://scikit-learn.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)).

## Resources
Plenty of resources can be found at [this link](https://aquarius31.github.io/ml/).

## Dataset
The datset used for this model can be found [here](https://drive.google.com/folderview?id=1aM19cJwlfLTzQnE8y6K-gdKuWfCyf0YC). 


## Further Works
Further we may deploy the model on Google’s API or make an app that will automatically detect such images and will remove from your phone.

## Communication

Our chat channel is to be found on Gitter [here](https://gitter.im/dsciitpatna/NotesSeparator?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

## Mentors
* [Piyush Tiwary](https://github.com/aquarius31) (**Project Lead**).
* [Anubhav Jangra](https://github.com/love-san).
* [Shreyash Gedkar](https://github.com/shreyash8).
* [Rahul Grover](https://github.com/rahulgrover99).
=======
﻿#Note separator

#Aim
In a student's life notes are very useful during exam time .But after exams are over, they are of no use also our gallery section is filled with random scattered images which take's extra space and even the gallery looks bad .Note separator is programmed to detect notes images automatically and to delete the notes images.

#Dataset
Dataset that is used to train the model can be found at https://drive.google.com/open?id=1y-YYS6_XE_ClmshJPhKNIiixedT6Rnkn. The above dataset contains total of 1500 images (aprox.)

850 notes images (aprox.).
650 non-notes images (aprox).
Size of each image is -->300X300, later reduced to 150x150.

#Libraries used
Tensorflow (high level keras api is used)
numpy
Matplotlib (for visualizing images and other plots)
CV2 and OS

#Model Inputs and features
The model showed maximum accuracy when the learning rate was reduced to 0.001.
It consist of 5 convolution layers. Number of nuerons in each layer from top to bottom are as follows 16,32,64,64,64. With RELU used as activation function in each layer followed by a maxpooling layer and a dropout of 0.2(initial 2 layers).
Results are then flattened to be fed into DNN.
There is 1 Dense fully connected layer consisting of 512 nuerons .
Lastly 1 more dense layer consisting of single nueron for the output with sigmoid as activation function.
Since dataset was small techniques like Data Agumentation had to be used.

#Accuracy
Test acc. 75%
Training acc. 88.68%

#Application
Note Seperator has a great role to play in a student's life, more into 'managing it'. The project is a great example of use of machine learning in day to day life.

#Learning Experience
This project helped me to learn the following.

CNN and DNN
Agumentation technique
Optimizers
Using callbacks
Confusion matrix
Use of PIL (python imaging library)

Further details regarding the project can be found [here](https://staticjunkk.github.io/Note-Seperator/)
>>>>>>> upstream/master
