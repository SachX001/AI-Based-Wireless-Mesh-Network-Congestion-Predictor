#  AI-Based Wireless Mesh Network Congestion Predictor (Python + Machine Learning)

A structured and practical **Machine Learning project** that predicts congestion levels in **wireless mesh networks** using telemetry-based parameters such as node density, packet rate, retry attempts, mobility speed, signal strength, and transmission range.

This project demonstrates how the **Random Forest Classification algorithm** can be applied to detect congestion early and support smarter routing and broadcast control strategies in mesh network environments.


##  Problem Description

Wireless mesh networks often suffer from congestion due to:

- Increasing node density
- High packet transmission rates
- Retransmission attempts
- Node mobility
- Weak signal strength

This project:

1. Uses telemetry-based network parameters as input
2. Trains a Machine Learning model using Random Forest
3. Predicts congestion levels as:

LOW  
MEDIUM  
HIGH

The system helps detect congestion **before severe packet loss or broadcast storms occur**.


##  Concepts Used

 Machine Learning Classification  
 Random Forest Algorithm  
 Data Preprocessing  
 Label Encoding  
 Dataset Simulation  
 Command-Line Prediction Interface  
 Data Visualization using Matplotlib  


##  Input Parameters

The model predicts congestion level using:

node_density  
packet_rate  
retry_count  
mobility_speed  
signal_strength  
transmission_range  

Example input:

node_density = 45  
packet_rate = 120  
retry_count = 6  
mobility_speed = 3  
signal_strength = -72  
transmission_range = 85  


##  Output

Predicted congestion level:

HIGH


##  Project Structure
```
AIML/
│
├── dataset.csv
├── preprocess.py
├── train_model.py
├── predictor.py
├── visualize.py
├── main.py
└── model.pkl
```

##  Dataset Description

The dataset simulates wireless mesh network telemetry behavior using structured parameters:

| Feature | Description |
|--------|-------------|
| node_density | Number of nodes in network area |
| packet_rate | Packets transmitted per second |
| retry_count | Number of retransmission attempts |
| mobility_speed | Node movement speed |
| signal_strength | Signal strength (dBm) |
| transmission_range | Coverage range of node |
| congestion | Target class label |

The dataset reflects realistic congestion transitions observed in mesh network environments.


##  Model Used — Random Forest Classifier

Random Forest was selected because it:

- Handles nonlinear relationships efficiently
- Works well with structured datasets
- Reduces overfitting risk
- Provides stable classification accuracy
- Performs well for congestion prediction problems


##  Program Workflow

### Step 1 — Data Loading

Reads dataset using:

dataset.csv


### Step 2 — Preprocessing

Encodes congestion labels:

LOW → 0  
MEDIUM → 1  
HIGH → 2  


### Step 3 — Model Training

Train model using:

python train_model.py

Outputs:

model.pkl


### Step 4 — Prediction Interface

Run prediction system:

python main.py

Program predicts congestion level instantly.


### Step 5 — Visualization

Generate visualization:

python visualize.py

Displays:

Node Density vs Packet Rate scatter plot


##  How To Run The Project

### Step 1 — Install Dependencies

pip install pandas scikit-learn matplotlib


### Step 2 — Train Model

python train_model.py


### Step 3 — Run Predictor

python main.py


### Step 4 — Generate Visualization

python visualize.py


##  Applications

This project can be applied in:

- Wireless mesh networks
- Smart city infrastructure
- IoT communication systems
- Disaster recovery communication networks
- Broadcast storm prediction systems
- Network simulation environments


##  Future Improvements

Possible enhancements include:

- Integration with ns-3 simulation datasets
- Real-time congestion monitoring dashboard
- Deep learning-based congestion prediction
- Adaptive rebroadcast suppression mechanisms
- Live telemetry-driven congestion prediction


##  Conclusion

This project demonstrates how Machine Learning techniques can be applied to predict congestion levels in wireless mesh networks using telemetry parameters.

Early congestion prediction enables improved routing strategies, broadcast optimization, and better performance management in dynamic wireless communication environments.
