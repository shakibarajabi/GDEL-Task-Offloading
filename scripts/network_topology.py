#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class NetworkTopology:
    def __init__(self, num_nodes, max_bandwidth, max_distance, cycle_time):
        self.num_nodes = num_nodes
        self.max_bandwidth = max_bandwidth  
        self.max_distance = max_distance  
        self.cycle_time = cycle_time  

        
        self.bandwidth_matrix = np.zeros((num_nodes, num_nodes))
        self.distance_matrix = np.random.uniform(100, max_distance, (num_nodes, num_nodes))
        self.interference_matrix = np.random.uniform(0.01, 0.2, (num_nodes, num_nodes)) 

    def compute_bandwidth(self, t):
        """ Compute available bandwidth between nodes based on distance, interference, and network congestion. """
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i != j:
                    distance_factor = np.exp(-(self.distance_matrix[i, j] / self.max_distance) ** 2)
                    congestion_factor = 1 / (1 + np.sin(np.pi * t / self.cycle_time))
                    interference_factor = 1 / (1 + self.interference_matrix[i, j])

                    self.bandwidth_matrix[i, j] = self.max_bandwidth * distance_factor * congestion_factor * interference_factor
        return self.bandwidth_matrix

    def compute_latency(self, task_size, t):
        """ Compute network latency including propagation, transmission, and queuing delays. """
        propagation_delay = self.distance_matrix / 3e8  
        transmission_delay = task_size / self.compute_bandwidth(t)  
        interference_penalty = np.log(1 + self.interference_matrix)

        return propagation_delay + transmission_delay + interference_penalty

    def compute_interference(self):
        """ Compute interference based on node density and power levels. """
        interference_levels = np.sum(self.interference_matrix, axis=1) / self.num_nodes
        return interference_levels


if __name__ == "__main__":
    network = NetworkTopology(num_nodes=50, max_bandwidth=100, max_distance=5000, cycle_time=120)
    t = 30  # Simulated time step
    bandwidth = network.compute_bandwidth(t)
    latency = network.compute_latency(task_size=2, t=t)  
    interference = network.compute_interference()

    print("Bandwidth Matrix:\n", bandwidth)
    print("Latency Matrix:\n", latency)
    print("Interference Levels:\n", interference)

