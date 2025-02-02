#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import torch
import random
import os

def set_seed(seed=42):
    """Set seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    

def save_model(model, filename="ddqn_model.pth"):
    """Save trained model to a file."""
    torch.save(model.state_dict(), filename)
    print(f"Model saved to {filename}")
    

def load_model(model, filename="ddqn_model.pth"):
    """Load trained model from a file."""
    if os.path.exists(filename):
        model.load_state_dict(torch.load(filename))
        model.eval()
        print(f"Model loaded from {filename}")
    else:
        print("No saved model found.")
    return model

def epsilon_decay(epsilon, decay_rate=0.995, min_epsilon=0.01):
    """Decay epsilon for exploration-exploitation balance."""
    return max(min_epsilon, epsilon * decay_rate)

def soft_update(target_model, source_model, tau=0.001):
    """Soft update target network parameters."""
    for target_param, source_param in zip(target_model.parameters(), source_model.parameters()):
        target_param.data.copy_(tau * source_param.data + (1.0 - tau) * target_param.data)

