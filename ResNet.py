# -*- coding: utf-8 -*-
"""ResNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCyMo5jmiYJSEYYLrrjYwT7IecQAGjJZ
"""

# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kwH7AY1A9IptupyTe0cg2giarg0f3aGm
"""

from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.datasets import mnist
import keras.layers as layers
# from keras.layers import Dense, Dropout, Flatten, BatchNormalization
#from keras.layers import Conv2D, MaxPooling2D, concatenate
from keras import backend as K
from keras.models import Model
from keras.initializers import glorot_uniform

batch_size = 128
num_classes = 10
epochs = 10

# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
print(input_shape)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

img_input = layers.Input(shape=input_shape)

model = layers.ZeroPadding2D(padding=(3,3))(img_input)
model = layers.Conv2D(64, kernel_size=(7,7), strides=(2,2), padding='valid', kernel_initializer='glorot_normal')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)
model = layers.ZeroPadding2D(padding=(1,1))(model)
model = layers.MaxPooling2D((3,3), strides=(2,2))(model)

model_shortcut = model
# convulutional block
model = layers.Conv2D(64, kernel_size=(1,1), strides=(2,2), kernel_initializer=glorot_uniform(seed=None), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(64, 3, strides=(1,1), kernel_initializer=glorot_uniform(seed=None), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(256, kernel_size=(1,1), strides=(1,1), kernel_initializer=glorot_uniform(seed=None), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
shortcut = layers.Conv2D(256, kernel_size=(1,1), strides=(2,2), kernel_initializer=glorot_uniform(seed=None), padding='valid')(model_shortcut)
shortcut = layers.BatchNormalization(axis=3, momentum=0.9)(shortcut)

model = layers.add([model, shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#identity block
model = layers.Conv2D(64, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(64, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0),padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(256, kernel_size=(1,1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0),padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.add([model, model_shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#identity block
model = layers.Conv2D(64, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(64, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(256, kernel_size=(1,1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.add([model, model_shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#convolutional block
model = layers.Conv2D(128, kernel_size=(3, 3), strides=(2,2), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(128, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(512, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
shortcut = layers.Conv2D(512, kernel_size=(1, 1), strides=(2,2), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model_shortcut)
shortcut = layers.BatchNormalization(axis=3, momentum=0.9)(shortcut)

model = layers.add([model, shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#identity block
model = layers.Conv2D(128, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(128, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(512, kernel_size=(1,1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.add([model, model_shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#identity block
model = layers.Conv2D(128, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(128, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(512, kernel_size=(1,1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.add([model, model_shortcut])
model = layers.Activation('relu')(model)

model_shortcut = model
#identity block
model = layers.Conv2D(128, kernel_size=(1, 1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(128, 3, strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='same')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.Activation('relu')(model)

model = layers.Conv2D(512, kernel_size=(1,1), strides=(1, 1), kernel_initializer=glorot_uniform(seed=0), padding='valid')(model)
model = layers.BatchNormalization(axis=3, momentum=0.9)(model)
model = layers.add([model, model_shortcut])
model = layers.Activation('relu')(model)

model = layers.GlobalAveragePooling2D(name='avg_pool')(model)
output = layers.Dense(num_classes, activation='softmax')(model)
model = Model(inputs=img_input, outputs=output, name='resnet')

model.summary()

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size, validation_split = 0.1,
          epochs=epochs,
          verbose=1)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])