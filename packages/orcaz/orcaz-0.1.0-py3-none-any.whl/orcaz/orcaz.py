#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# **********************************************************************************************************************
# File: orca.py
# Project: Optimized Registration through Conditional Adversarial networks (ORCA)
# Author: Zacharias Chalampalakis | Lalith Kumar Shiyam Sundar | Sebastian Gutschmayer
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 04.07.5023
# Version: 0.1.0
# Email: zacharias.chalampalakis@meduniwien.ac.at, lalith.shiyamsundar@meduniwien.ac.at
# **********************************************************************************************************************

# Importing required libraries
import logging
import sys
import emoji
import os

from datetime import datetime

import warnings
warnings.filterwarnings('ignore', category=UserWarning, message='TypedStorage is deprecated')

import resource
rlimit = resource.getrlimit(resource.RLIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_NOFILE, (4096, rlimit[1]))

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO,
                    filename=datetime.now().strftime('orca-%H-%M-%d-%m-%Y.log'),
                    filemode='w')
# uncomment the following line to print the logs to the console
#logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

def main():

    logging.info("----------------------------------------------------------------------------------------------------")
    logging.info("                                         STARTING ORCA 0.1.0                                        ")
    logging.info("----------------------------------------------------------------------------------------------------")
    logging.info(' ')

    # ----------------------------------
    # DOWNLOADING THE BINARIES
    # ----------------------------------


if __name__ == '__main__':
  main()
