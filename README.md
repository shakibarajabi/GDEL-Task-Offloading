GDEL: GEO-DISTRIBUTED EDGE LAYERING FOR TASK OFFLOADING

A Mobility-Aware MEC Simulation with DDQN-Based Task Offloading

This repository contains the GDEL (Geo-Distributed Edge Layering) framework, a reinforcement learning-driven task offloading model designed for Mobile Edge Computing (MEC) environments. The system optimizes task offloading, resource allocation, and network efficiency while considering user mobility, interference, and network conditions.

📌 FEATURES
•	Task Offloading Model: Uses MDP and DDQN for intelligent decision-making
Geo-Distributed Edge Layering (GDEL): GAONs (Geo-Aware Offloading Nodes) and ROHs (Regional Offloading Hubs) dynamically allocate computing resources

•	Network-Aware Optimization: Factors in bandwidth, interference, latency, and power constraints

•	Mobility Prediction: Uses nonlinear motion models for user position tracking
Resource Allocation: Dynamically distributes computational load based on network congestion

•	Performance Evaluation: Includes real-world metrics like task completion time, offloading latency, and energy consumption

   


🔧 INSTALLATION GUIDE
1️ CLONE REPOSITORY

2️ INSTALL DEPENDENCIES
pip install -r requirements.txt

3️ RUN THE MEC SIMULATION
To execute the task offloading model:
python src/train.py
To analyze performance metrics:
jupyter notebook notebooks/performance_analysis.ipynb


📊 PERFORMANCE METRICS
This repository includes detailed performance evaluation CSV files, stored in the data/ folder:
1️ TASK COMPLETION TIME
📄 task_completion_time.csv
•	Measures the time required to complete tasks of varying sizes across different offloading strategies.
2️ OFFLOADING DECISION LATENCY
📄 offloading_latency.csv
•	Evaluates how quickly the system decides between local processing vs. offloading.
3️ ENERGY CONSUMPTION PER TASK
📄 energy_consumption.csv
•	Tracks power consumption for both local computation and offloading.
4️ SUCCESSFUL OFFLOADING RATIO
📄 successful_offloading_ratio.csv
•	Measures how many tasks were successfully offloaded vs. failed due to congestion or interference.
5️ NETWORK EFFICIENCY
📄 network_efficiency.csv
•	Assesses the data throughput, latency, and bandwidth utilization.

 
📌 HOW TO CONTRIBUTE
✅Fork the repository.
✅ Create a new branch:
git checkout -b feature-new-feature
✅ Commit and push your changes.
✅ Open a Pull Request with a description of your improvements.

📌 Contact: For any questions or collaborations, feel free to reach out at mehdi.hosseinzadeh@mq.edu.au.

![image](https://github.com/user-attachments/assets/97640508-6c3a-49e7-857d-9e0d9e608a90)
