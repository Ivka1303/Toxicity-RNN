"""
Utilities for various small tasks.
"""

import os
import matplotlib.pyplot as plt
import torch
import argparse

def change_str(name):
    """
    Replaces specific characters in a string (spaces, commas, semicolons, periods, and brackets) 
    with an underscore, and removes apostrophes.
    Parameters:
    - name (str): The string to be modified.
    Returns:
    str: The modified string with replaced and removed characters.
    """
    changed = ''
    for i in range(len(name)):
        if name[i]=='{' or name[i]=='}' or name[i]=='.' or name[i]==':' \
                or name[i]==',' or name[i]==' ':
            changed += '_'
        elif name[i]=='\'':
            changed += ''
        else:
            changed += name[i]
    return changed


def make_dir(name):
    """
    Creates a new directory with the given name if it does not already exist.
    Parameters:
    - name (str): The name of the directory to be created.
    """
    if not os.path.exists(name):
        os.makedirs(name)


def use_gpu():
    """
    Configures the training to use GPU resources if available and not disabled.
    Returns:
    argparse.Namespace: A namespace object containing the device configuration.
    """
    # if the system supports CUDA, utilize it for faster computation.
    parser = argparse.ArgumentParser(description='Set device')
    parser.add_argument('--disable-cuda', action='store_true',
                        help='Disable CUDA')
    args = parser.parse_args()
    args.device = None

    if not args.disable_cuda and torch.cuda.is_available():
        args.device = torch.device('cuda:0')
    else:
        args.device = torch.device('cpu:0')

    return args
