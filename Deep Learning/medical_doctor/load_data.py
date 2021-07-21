# HYJ
# TIME: 2021-7-21 11:14
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm
import os
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow as tf


def load_data():
    labels = ['glioma_tumor','no_tumor','meningioma_tumor','pituitary_tumor']
    X_train = []
    y_train = []
    image_size = 150
    for i in labels:
        folderPath = os.path.join('data', 'Training', i)
        for j in tqdm(os.listdir(folderPath)):
            img = cv2.imread(os.path.join(folderPath, j))
            img = cv2.resize(img, (image_size, image_size))
            X_train.append(img)
            y_train.append(i)

    for i in labels:
        folderPath = os.path.join('data', 'Testing', i)
        for j in tqdm(os.listdir(folderPath)):
            img = cv2.imread(os.path.join(folderPath, j))
            img = cv2.resize(img, (image_size, image_size))
            X_train.append(img)
            y_train.append(i)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    X_train, y_train = shuffle(X_train,y_train, random_state=101)

    datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True)

    datagen.fit(X_train)
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1, random_state=101)

    y_train_new = []
    for i in y_train:
        y_train_new.append(labels.index(i))
    y_train = y_train_new
    y_train = tf.keras.utils.to_categorical(y_train)

    y_test_new = []
    for i in y_test:
        y_test_new.append(labels.index(i))
    y_test = y_test_new
    y_test = tf.keras.utils.to_categorical(y_test)

    return X_train, X_test, y_train, y_test, labels