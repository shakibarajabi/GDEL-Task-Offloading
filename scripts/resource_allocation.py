#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class ResourceAllocation:
    def __init__(self, num_nodes, max_capacity, max_load):
        self.num_nodes = num_nodes
        self.max_capacity = max_capacity  
        self.max_load = max_load  

        
        self.node_loads = np.random.uniform(0, max_load, num_nodes)
        self.node_capacities = np.random.uniform(max_capacity * 0.5, max_capacity, num_nodes)
        self.interference_levels = np.random.uniform(0.01, 0.2, num_nodes)  

    def allocate_resources(self):
        """ Allocate computational resources dynamically based on load and interference. """
        allocation = (self.node_capacities / np.sum(self.node_capacities)) * \
                     (1 / (1 + self.interference_levels)) * \
                     np.cos(np.pi * self.node_loads / (2 * self.max_load))

        return allocation

    def adjust_for_priority(self, task_priority):
        """ Adjust resource allocation based on task priority (higher priority gets more resources). """
        base_allocation = self.allocate_resources()
        priority_factor = 1 + np.log2(1 + task_priority)
        return base_allocation * priority_factor

    def energy_aware_allocation(self, power_consumption, max_power):
        """ Allocate resources while considering power consumption constraints. """
        base_allocation = self.allocate_resources()
        energy_factor = np.exp(-power_consumption / max_power)
        return base_allocation * energy_factor

# Example Usage
if __name__ == "__main__":
    resource_alloc = ResourceAllocation(num_nodes=50, max_capacity=10, max_load=100)
    
    allocation = resource_alloc.allocate_resources()
    priority_allocation = resource_alloc.adjust_for_priority(task_priority=3)
    energy_allocation = resource_alloc.energy_aware_allocation(power_consumption=np.random.uniform(1, 5, 50), max_power=10)

    print("Resource Allocation:\n", allocation)
    print("Priority-Based Allocation:\n", priority_allocation)
    print("Energy-Aware Allocation:\n", energy_allocation)

