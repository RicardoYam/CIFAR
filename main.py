import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

cifar = tf.keras.datasets.cifar10.load_data()
print(cifar)