import os 
import numpy as np
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import glob
import random
from natsort import natsorted

from util.utils import *
from models.m_rBCR import *
from util.loss_func import *
from util.metrics import *
from util.data import *

def multi_input(w_img, o_img):
    
    w_0, o_0 = w_img, o_img
    w_2, o_2 = w_0[:, ::2, ::2, :], o_0[:, ::2, ::2, :]
    w_4, o_4 = w_0[:, ::4, ::4, :], o_0[:, ::4, ::4, :]
    
    return [w_0, w_2, w_4], [o_0, o_2, o_4]

def train_m_rBCR(steps=2000, ckPth='./checkpoints/m_rBCR'):
    
    train_img_datagen, val_img_datagen = data_prep()
    model = model_m_rBCR()
    
    NUM_STEPS = steps
    best_val_loss = float('inf')
    patience = 5 # Number of epochs to wait for improvement
    wait = 0

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)  # You can adjust the learning rate

    # Define a checkpoint to save model weights
    checkpoint = tf.train.Checkpoint(model=model)
    checkpoint_manager = tf.train.CheckpointManager(checkpoint, ckPth, max_to_keep=5)

    for step in range(NUM_STEPS):
        w_train, o_train = train_img_datagen.__next__()
        w_train_list, o_train_list = multi_input(w_train, o_train)

        with tf.GradientTape() as tape:
            # Forward pass
            predictions = model(w_train_list)

            # Calculate the loss manually
            loss = loss_function_mimo(o_train_list, predictions)
            metric = metrics_func_mimo(o_train_list, predictions)

        # Compute gradients
        gradients = tape.gradient(loss, model.trainable_variables)

        # Update the model's weights
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

        if step % 50 == 0:
            print(step, loss, metric)
            # Save the model weights using the Checkpoint
            checkpoint_manager.save()

        if step % 100 == 0:
            w_eval, o_eval = val_img_datagen.__next__()
            w_eval_list, o_eval_list = multi_input(w_eval, o_eval)
            val_predictions = model(w_eval_list)

            # Calculate the validation loss manually
            val_loss = loss_function_mimo(o_eval_list, val_predictions)
            val_metric = metrics_func_mimo(o_eval_list, val_predictions)

            if val_loss < best_val_loss:
                best_val_loss = val_loss
                wait = 0
                print('Validation best loss:', step, best_val_loss, val_metric)
                checkpoint_manager.save()
            else:
                wait += 1

            if wait >= patience:
                print("Early stopping due to no improvement in validation loss.", step)
                checkpoint_manager.save()
                break
                
# train_m_rBCR()

