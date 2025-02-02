#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class MobilityModel:
    def __init__(self, num_users, area_size, max_speed, time_step):
        self.num_users = num_users
        self.area_size = area_size
        self.max_speed = max_speed  
        self.time_step = time_step  

        
        self.positions = np.random.uniform(0, area_size, (num_users, 2))
        self.velocities = np.random.uniform(-max_speed, max_speed, (num_users, 2))
        self.accelerations = np.random.uniform(-0.1, 0.1, (num_users, 2))  

    def update_positions(self):
        """ Update user positions based on velocity and acceleration. """
        self.velocities += self.accelerations * self.time_step
        self.positions += self.velocities * self.time_step

        # Keep users within boundaries
        self.positions = np.clip(self.positions, 0, self.area_size)

    def predict_next_position(self):
        """ Predict next position using a motion model. """
        predicted_positions = self.positions + self.velocities * np.cos(np.pi / 4) + np.tanh(self.accelerations)
        return predicted_positions

    def compute_mobility_error(self, actual_positions):
        """ Compute mobility prediction error. """
        prediction_error = np.mean(np.linalg.norm(self.positions - actual_positions, axis=1))
        return prediction_error


if __name__ == "__main__":
    mobility = MobilityModel(num_users=100, area_size=10000, max_speed=3, time_step=1)
    mobility.update_positions()
    predicted_positions = mobility.predict_next_position()
    mobility_error = mobility.compute_mobility_error(predicted_positions)

    print("Updated User Positions:\n", mobility.positions)
    print("Predicted Positions:\n", predicted_positions)
    print("Mobility Prediction Error:\n", mobility_error)

