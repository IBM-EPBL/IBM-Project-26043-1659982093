#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen=ImageDataGenerator(rescale=1)


# In[11]:


x_train= train_datagen.flow_from_directory(r'C:\Users\LENOVO\Downloads\Data Collection\Dataset Plant Disease\fruit-dataset\fruit-dataset\train',target_size=(128,128),batch_size=32,class_mode='categorical')
x_test= test_datagen.flow_from_directory(r'C:\Users\LENOVO\Downloads\Data Collection\Dataset Plant Disease\fruit-dataset\fruit-dataset\test',target_size=(128,128),batch_size=32,class_mode='categorical')


# In[12]:


x_train=train_datagen.flow_from_directory(r'C:\Users\LENOVO\Downloads\Data Collection\Dataset Plant Disease\Veg-dataset\Veg-dataset\train_set',target_size=(128,128),batch_size=2,class_mode='categorical')
x_test=test_datagen.flow_from_directory(r'C:\Users\LENOVO\Downloads\Data Collection\Dataset Plant Disease\Veg-dataset\Veg-dataset\test_set',target_size=(128,128),batch_size=2,class_mode='categorical')


# In[ ]:




