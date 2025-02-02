#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random
import json

class MECEnvironment:
    def __init__(self, num_nodes=50, num_users=500, max_bandwidth=100, max_computational_capacity=40):
        self.num_nodes = num_nodes  
        self.num_users = num_users  
        self.max_bandwidth = max_bandwidth  
        self.max_computational_capacity = max_computational_capacity  
        self.nodes = self.initialize_nodes()
        self.tasks = []
        self.time = 0

    def initialize_nodes(self):
        nodes = []
        for i in range(self.num_nodes):
            nodes.append({
                'id': i,
                'type': 'GAON' if i < (self.num_nodes - 10) else 'ROH',
                'computational_capacity': random.uniform(10, self.max_computational_capacity),
                'current_load': 0,
                'location': np.array([random.uniform(0, 10), random.uniform(0, 10)]),
                'bandwidth': random.uniform(10, self.max_bandwidth),
                'interference': random.uniform(0.1, 0.5),
            })
        return nodes

    def generate_task(self):
        task = {
            'size': np.random.normal(2, 1),  
            'priority': random.randint(1, 5),
            'deadline': random.uniform(5, 30),  
            'user_id': random.randint(0, self.num_users - 1),
            'arrival_time': self.time,
        }
        self.tasks.append(task)

    def update_network_conditions(self):
        for node in self.nodes:
            node['bandwidth'] *= np.exp(-random.uniform(0.01, 0.05))  
            node['interference'] *= random.uniform(0.9, 1.1)  

    def allocate_task(self, task):
        available_nodes = [n for n in self.nodes if n['current_load'] < n['computational_capacity']]
        if available_nodes:
            selected_node = min(available_nodes, key=lambda n: n['current_load'])
            selected_node['current_load'] += task['size']
            task['assigned_node'] = selected_node['id']
            task['processing_time'] = self.calculate_processing_time(selected_node, task)
        else:
            task['assigned_node'] = None  
            task['processing_time'] = float('inf')

    def calculate_processing_time(self, node, task):
        load_factor = (node['computational_capacity'] - node['current_load']) / node['computational_capacity']
        interference_factor = np.cos(np.pi / 2 * (node['interference'] / 1.0))
        return (task['size'] / node['computational_capacity']) * load_factor * interference_factor

    def step(self):
        self.generate_task()
        self.update_network_conditions()
        for task in self.tasks:
            if 'assigned_node' not in task:
                self.allocate_task(task)
        self.time += 1

    def save_results(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

# Example Usage
env = MECEnvironment()
for _ in range(100):  # Simulate 100 time steps
env.step()
env.save_results()

