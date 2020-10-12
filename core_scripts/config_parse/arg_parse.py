#!/usr/bin/env python
"""
config_parse

Argument parse

"""
from __future__ import absolute_import

import os
import sys
import argparse

import core_scripts.other_tools.list_tools as nii_list_tools
import core_scripts.other_tools.display as nii_display

__author__ = "Xin Wang"
__email__ = "wangxin@nii.ac.jp"
__copyright__ = "Copyright 2020, Xin Wang"



#############################################################
# argparser
#
def f_args_parsed(argument_input = None):
    """ Arg_parse
    """
    
    parser = argparse.ArgumentParser(
        description='General argument parse')
    
    ######
    # lib
    mes = 'module of model definition (default model, model.py will be loaded)'
    parser.add_argument('--module-model', type=str, default="model", help=mes)

    mes = 'module of configuration (default config, config.py will be loaded)'
    parser.add_argument('--module-config', type=str, default="config", 
                        help=mes)
    
    ######
    # Training settings    
    mes = 'batch size for training/inference (default: 1)'
    parser.add_argument('--batch-size', type=int, default=1, help=mes)
    
    mes = 'number of epochs to train (default: 50)'
    parser.add_argument('--epochs', type=int, default=50, help=mes)
    
    mes = 'number of no-best epochs for early stopping (default: 5)'
    parser.add_argument('--no-best-epochs', type=int, default=5, help=mes)
    
    parser.add_argument('--lr', type=float, default=0.0001, 
                        help='learning rate (default: 0.0001)')
    
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    
    parser.add_argument('--seed', type=int, default=1, 
                        help='random seed (default: 1)')
    
    mes = 'turn model.eval() on validation set (default: false)'
    parser.add_argument('--eval-mode-for-validation', \
                        action='store_true', default=False, help=mes)

    mes = 'if model.forward(input, target), please set this option on. '
    mes += 'This is used for autoregressive model, auto-encoder, and so on. '
    mes += 'When --model-forward-with-file-name is also on, '
    mes += 'model.forward(input, target, file_name) should be defined'
    parser.add_argument('--model-forward-with-target', \
                        action='store_true', default=False, help=mes)

    mes = 'if model.forward(input, file_name), please set option on. '
    mes += 'This is used with forward requires file name of the data. '
    mes += 'When --model-forward-with-target is also on, '
    mes += 'model.forward(input, target, file_name) should be defined'
    parser.add_argument('--model-forward-with-file-name', \
                        action='store_true', default=False, help=mes)
    
    parser.add_argument('--shuffle', action='store_false', \
                        default=True, 
                        help='shuffle data? (default true)')

    mes = 'number of parallel workers to load data (default: 0)'
    parser.add_argument('--num-workers', type=int, default=0, help=mes)

    mes = 'use DataParallel to levarage multiple GPU (default: False)'
    parser.add_argument('--multi-gpu-data-parallel', \
                        action='store_true', default=False, help=mes)

    ######
    # options to save model / checkpoint
    parser.add_argument('--save-model-dir', type=str, \
                        default="./", \
                        help='save model to this direcotry (default ./)')
    
    mes = 'do not save model after every epoch (default: False)'
    parser.add_argument('--not-save-each-epoch', action='store_true', \
                        default=False, help=mes)

    mes = 'name prefix of saved model (default: epoch)'
    parser.add_argument('--save-epoch-name', type=str, default="epoch", \
                        help=mes)

    mes = 'name of trained model (default: trained_network)'
    parser.add_argument('--save-trained-name', type=str, \
                        default="trained_network", help=mes)
    
    parser.add_argument('--save-model-ext', type=str, default=".pt",
                        help='extension name of model (default: .pt)')
    
    #######
    # options to load model
    mes = 'a trained model for inference or resume training '
    parser.add_argument('--trained-model', type=str, \
                        default="", help=mes + "(default: '')")

    mes = 'do not load previous training error information.'
    mes += " Load only model para. and optimizer state  (default: false)"
    parser.add_argument('--ignore-training-history-in-trained-model', 
                        action='store_true', \
                        default=False, help=mes)    

    mes = 'do not load previous training statistics in optimizer.'
    mes += " (default: false)"
    parser.add_argument('--ignore-optimizer-statistics-in-trained-model', 
                        action='store_true', \
                        default=False, help=mes)    

    mes = 'run inference mode (default: False, run training script)'
    parser.add_argument('--inference', action='store_true', \
                        default=False, help=mes)    
    #######
    # options to output
    mes = 'path to save generated data (default: ./output)'
    parser.add_argument('--output-dir', type=str, default="./output", \
                        help=mes)
    mes = 'which optimizer to use (Adam | SGD, default: Adam)'
    parser.add_argument('--optimizer', type=str, default='Adam', help=mes)
    
    mes = 'verbose level 0: nothing; 1: print error per utterance'
    mes = mes + ' (default: 1)'
    parser.add_argument('--verbose', type=int, default=1,
                        help=mes)

    #######
    # options for user defined 
    mes = 'a temporary flag without specific purpose.'
    mes += 'User should define args.temp_flag only for temporary usage.'
    parser.add_argument('--temp-flag', type=str, default='', help=mes)
    
    #
    # done
    if argument_input is not None:
        return parser.parse_args(argument_input)
    else:
        return parser.parse_args()


if __name__ == "__main__":
    pass
    
