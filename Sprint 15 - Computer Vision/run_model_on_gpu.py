
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    
    """
    It loads the train part of dataset from path
    """
    
    train_datagen = ImageDataGenerator(validation_split=0.2,
                                      rescale= 1 / 255,
                                      vertical_flip=True,
                                      horizontal_flip=True,
                                      rotation_range=20,
                                      width_shift_range=0.2,
                                      zoom_range=0.2,
                                      height_shift_range=0.2)

    train_datagen_flow = train_datagen.flow_from_dataframe( # automatically search for the image in directory
        dataframe=labels,
        directory='/datasets/faces/final_files/', # path
        x_col='file_name',
        y_col='real_age',
        target_size=(150, 150),
        batch_size=32,
        class_mode='raw', # raw target values for regression task
        subset='training',
        seed=12345)

    return train_datagen_flow


def load_test(path):
    
    """
    It loads the validation/test part of dataset from path
    """
    
    test_datagen = ImageDataGenerator(validation_split=0.2,
                                      rescale= 1 / 255)

    test_datagen_flow = test_datagen.flow_from_dataframe( # automatically search for the image in directory
        dataframe=labels,
        directory='/datasets/faces/final_files/', # path
        x_col='file_name',
        y_col='real_age',
        target_size=(150, 150),
        batch_size=32,
        class_mode='raw', # raw target values for regression task
        subset='validation',
        seed=12345)

    return test_datagen_flow


def create_model(input_shape):
    
    """
    It defines the model
    """
    
    backbone = ResNet50(input_shape=input_shape,
                    weights='imagenet',
                    include_top=False)

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation="relu"))

    optimizer = Adam(lr=0.0001)
    model.compile(optimizer=optimizer, 
                  loss='mse',
                  metrics=['mae'])

    return model


def train_model(model, 
                train_data, 
                test_data,
                batch_size=None, 
                epochs=20,
                steps_per_epoch=None, 
                validation_steps=None):
    

    """
    Trains the model given the parameters
    """
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size, 
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2)

    return model


