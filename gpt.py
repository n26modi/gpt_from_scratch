import torch 
import torch.nn as nn
import torch.nn.functional as F

# small hyperparameter config for cpu runs
batch_size    = 32
block_size    = 8
n_embd        = 32
n_head        = 4
n_layer       = 3
dropout       = 0.0
learning_rate = 1e-3
max_iters     = 5000

torch.manual_seed(31)

# read input text
with open('input.txt', 'r') as f:
    text = f.read()

# create a set of all unique characters in the text
chars = sorted(set(text))

#create a mapping from each unique character to an integer (index)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch fpr i,ch in enumarate(chars)} 

