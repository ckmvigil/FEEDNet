# -*- coding: utf-8 -*-
import sys
sys.path.append("../src")
sys.path.append("../src/data/")

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import tensorflow as tf
from dataloader import *
from tqdm import tqdm
from config import *
from utils import *
from loss import *
import numpy as np
import argparse
import logging
import os

def main():
    """ testing performance of model. 
    """
    train_ds, test_ds = getData(DATASET)
    model = tf.keras.models.load_model(os.path.join(WEIGHTS_DIR, 'best_model.h5'), custom_objects = {"diceCoef": diceCoef, "bceDiceLoss": bceDiceLoss})
    

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, filename = os.path.join(LOG_DIR, 'app.log'), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

    sys.stdout = LoggerWriter(logging.info)
    sys.stderr = LoggerWriter(logging.error)

    main()