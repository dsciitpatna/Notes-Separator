# Note separator

# Aim
In a student's life notes are very useful during exam time .But after exams are over, they are of no use also our gallery section is filled with random scattered images which take's extra space and even the gallery looks bad .Note separator is programmed to detect notes images automatically and to delete the notes images.

# Dataset
Dataset that is used to train the model can be found at [Dataset link](https://drive.google.com/open?id=1y-YYS6_XE_ClmshJPhKNIiixedT6Rnkn). The above dataset contains total of 1500 images (aprox.)

850 notes images (aprox.).

650 non-notes images (aprox).

Size of each image is -->300X300, later reduced to 150x150.

# Libraries used
Tensorflow (high level keras api is used)

numpy

Matplotlib (for visualizing images and other plots)

CV2 and OS

# Model Inputs and features
The model showed maximum accuracy when the learning rate was reduced to 0.001.
It consist of 5 convolution layers. Number of nuerons in each layer from top to bottom are as follows 16,32,64,64,64. With RELU used as activation function in each layer followed by a maxpooling layer and a dropout of 0.2(initial 2 layers).
Results are then flattened to be fed into DNN.
There is 1 Dense fully connected layer consisting of 512 nuerons .
Lastly 1 more dense layer consisting of single nueron for the output with sigmoid as activation function.
Since dataset was small techniques like Data Agumentation had to be used.

# Accuracy
Test acc. 75%

Training acc. 88.68%

# Application
Note Seperator has a great role to play in a student's life, more into 'managing it'. The project is a great example of use of machine learning in day to day life.

# Learning Experience
This project helped me to learn the following.

CNN and DNN

Agumentation technique

Optimizers

Using callbacks

Use of PIL (python imaging library)


Further details regarding the project can be found [here](https://staticjunkk.github.io/Note-Seperator/)
