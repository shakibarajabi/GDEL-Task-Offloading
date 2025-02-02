#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def compute_capacity(C_max, L_max, L_i, theta_i, theta_max):
    """Computes computational capacity of node i."""
    return C_max * np.exp(-L_i / L_max) * np.cos((np.pi / 2) * (theta_i / theta_max))

def task_processing_time(S_task, C_i, B_max):
    """Computes task processing time based on system model."""
    return (S_task / C_i) + np.log2(1 + (S_task / B_max))

def offloading_probability(tau_proc, tau_trans):
    """Computes probability of offloading a task."""
    return 1 / (1 + np.exp(-((tau_proc - tau_trans) / (tau_proc + tau_trans))))

def transmission_time(S_task, B_ij, theta_ij, T):
    """Computes transmission time between nodes."""
    return (S_task / B_ij) * np.mean(1 / (1 + theta_ij))

def total_task_completion_time(tau_proc, tau_trans, T_peak, S_task, B_ij):
    """Computes total task completion time including peak congestion effects."""
    return tau_proc + tau_trans + np.sin((np.pi * T_peak) / T_peak) * np.log(1 + (S_task / B_ij))

def bandwidth_allocation(B_max, d_ij, D_max, theta_ij, T_cycle, t):
    """Computes available bandwidth based on distance, interference, and congestion."""
    return B_max * np.exp(-(d_ij / D_max)**2) / (1 + np.sin((np.pi * t) / T_cycle)) / (1 + theta_ij)

def network_latency(d_ij, c, S_task, B_ij, theta_ij, T):
    """Computes total network latency."""
    L_prop = d_ij / c
    L_trans = S_task / B_ij
    L_interf = np.mean(theta_ij / B_ij)
    return L_prop + L_trans + L_interf

def routing_weight(L_i, L_max):
    """Computes the weight assigned to a node in a load-balanced routing scheme."""
    return 1 / (1 + L_i / L_max)

# Example Usage
if __name__ == "__main__":
    # Example node properties
    C_max = 40  # GHz
    L_max = 100  # Max load
    L_i = 50  # Current load
    theta_i = 0.3  # Interference level
    theta_max = 1.0  # Max interference
    
    C_i = compute_capacity(C_max, L_max, L_i, theta_i, theta_max)
    print(f"Computed Capacity: {C_i:.2f} GHz")

