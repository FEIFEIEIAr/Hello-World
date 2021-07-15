%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sklearn
import sys
import cv2
import tensorflow as tf
from tensorflow import keras
import random


# using dataset of 10-monkey-species from kaggle
train_dir = "../input/10-monkey-species/training/training"
valid_dir = "../input/10-monkey-species/validation/validation"
label_file = "../input/10-monkey-species/monkey_labels.txt

cols = ['Label','Latin Name', 'Common Name','Train Images', 'Validation Images']
labels = pd.read_csv(label_file, names=cols, skiprows=1)
labels

def show_imgs(class_names, n_images_per_class):
    n_rows = len(class_names)
    n_cols = n_images_per_class
    plt.figure(figsize = (n_cols * 1.4, n_rows * 1.6))
    for row in range(len(class_names)):
        imgdir = os.path.join(train_dir, class_names[row])
        for col in range(n_cols):
            index = n_cols * row + col 
            imgfile = random.choice(os.listdir(imgdir))
            img = cv2.imread(os.path.join(imgdir, imgfile))
            plt.subplot(n_rows, n_cols, index+1)
            plt.imshow(img)
            plt.axis('off')
            plt.title(class_names[row])
    plt.show()

def plot_learning_curves(history, label):
    data = {}
    data[label] = history.history[label]
    data['val_'+label] = history.history['val_'+label]
    pd.DataFrame(data).plot(figsize=(8, 5))
    plt.grid(True)
    plt.show()
    
show_imgs(['n{}'.format(n) for n in range(10)], 10)

height = 128
width = 128
channels = 3
batch_size = 128
num_classes = 10

train_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale = 1./255,
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = 'nearest',
)
train_generator = train_datagen.flow_from_directory(train_dir,
                                                   target_size = (height, width),
                                                   batch_size = batch_size,
                                                   seed = 7008,
                                                   shuffle = True,
                                                   class_mode = "categorical")
valid_datagen = keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)
valid_generator = valid_datagen.flow_from_directory(valid_dir,
                                                    target_size = (height, width),
                                                    batch_size = batch_size,
                                                    seed = 7008,
                                                    shuffle = False,
                                                    class_mode = "categorical")

train_num = train_generator.samples
valid_num = valid_generator.samples


model = keras.models.Sequential([
    keras.layers.Conv2D(filters=32, kernel_size=3, padding='same',
                        activation='relu', input_shape=[width, height, channels]),
    keras.layers.Conv2D(filters=32, kernel_size=3, padding='same',
                        activation='relu'),
    keras.layers.MaxPool2D(pool_size=2),
    
    keras.layers.Conv2D(filters=64, kernel_size=3, padding='same',
                        activation='relu'),
    keras.layers.Conv2D(filters=64, kernel_size=3, padding='same',
                        activation='relu'),
    keras.layers.MaxPool2D(pool_size=2),
    
    keras.layers.Conv2D(filters=128, kernel_size=3, padding='same',
                        activation='relu'),
    keras.layers.Conv2D(filters=128, kernel_size=3, padding='same',
                        activation='relu'),
    keras.layers.MaxPool2D(pool_size=2),
  
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(num_classes, activation='softmax'),
])

model.compile(loss="categorical_crossentropy",
              optimizer="adam", metrics=['accuracy'])
model.summary()

earlyStop = keras.callbacks.EarlyStopping(
    monitor='val_loss', min_delta=0, patience=8, verbose=0,
    mode='auto', baseline=None, restore_best_weights=False
)
epochs = 50
history = model.fit(train_generator,
                    steps_per_epoch = train_num // batch_size,
                    epochs = epochs,
                    validation_data = valid_generator,
                    validation_steps = valid_num // batch_size,
                    callbacks=[earlyStop])

    
plot_learning_curves(history, 'accuracy')
plot_learning_curves(history, 'loss')    
model.evaluate(valid_generator)
