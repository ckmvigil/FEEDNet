# -*- coding: utf-8 -*-
# yet to be modified
import sys
sys.path.append("../src")

from tqdm import tqdm 
from config import *
from utils import *
import numpy as np
import logging
import os

def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be trained (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('[Info] Generating Images, Masks from raw data')

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, filename = os.path.join(LOG_DIR, 'app.log'), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

    sys.stdout = LoggerWriter(logging.info)
    sys.stderr = LoggerWriter(logging.error)

    main()