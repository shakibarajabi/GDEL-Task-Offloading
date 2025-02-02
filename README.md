# GDEL Task Offloading with DDQN

## Overview
This repository provides the implementation of **Geo-Distributed Edge Layering (GDEL)** for **task offloading in a Mobile Edge Computing (MEC) environment**. The proposed system integrates **Double Deep Q-Networks (DDQN)** to optimize task allocation decisions based on network conditions, user mobility, and resource availability.

## Features
- **System Simulation**: Implements an MEC environment with network topology, bandwidth allocation, and interference modeling.
- **Task Offloading via DDQN**: Uses reinforcement learning to optimize task scheduling.
- **Resource Allocation**: Dynamically manages edge resources based on real-time demand.
- **Mobility Model**: Simulates user mobility patterns affecting network performance.
- **Performance Analysis**: Includes comparison metrics such as task completion time, energy consumption, and network efficiency.

## Repository Structure
```
GDEL-Task-Offloading/
│── README.md                # Instructions on using the repo
│── installation.md           # Dependencies and setup guide
│── requirements.txt          # Python dependencies
│── .gitignore                # Ignore unnecessary files
│── notebooks/                # Jupyter Notebooks
│   ├── environment.ipynb
│   ├── system_model.ipynb
│   ├── network_topology.ipynb
│   ├── mobility_model.ipynb
│   ├── resource_allocation.ipynb
│   ├── performance_analysis.ipynb
│   ├── train_ddqn.ipynb
│── data/                     # CSV datasets
│   ├── task_data.csv
│   ├── network_conditions.csv
│   ├── energy_consumption.csv
│   ├── latency_analysis.csv
│── scripts/                  # Python scripts for training & evaluation
│   ├── ddqn_agent.py
│   ├── environment.py
│   ├── system_model.py
│   ├── network_topology.py
│   ├── mobility_model.py
│   ├── resource_allocation.py
│   ├── utils.py

```

## Installation
1. Clone the repository:
   ```bash
   git clone git clone https://github.com/shakibarajabi/GDEL-Task-Offloading/
   cd GDEL-Task-Offloading
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Running the Simulation
### Step 1: Generate Tasks
```bash
python scripts/task_generator.py
```

### Step 2: Train the DDQN Model
```bash
python scripts/train_ddqn.py
```

### Step 3: Run Performance Analysis
Open `performance_analysis.ipynb` in Jupyter Notebook and execute all cells.

## Results and Performance Metrics
- **Task Completion Time**
- **Offloading Decision Latency**
- **Energy Consumption per Task**
- **Successful Offloading Ratio**
- **Network Efficiency**

## Contributions
We welcome contributions to improve this project. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

