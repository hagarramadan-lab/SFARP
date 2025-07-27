🛡️ SFARP: A Multi-Layered SDN Framework for Real-Time Defense Against ARP Spoofing and DDoS Attacks in IoT

SFARP is a secure, scalable, and P4-integrated framework for Software-Defined IoT (SD-IoT) networks, designed to defend against **coordinated ARP spoofing and DDoS attacks**. It fuses programmable data planes, ensemble machine learning, and distributed SDN controllers to ensure real-time detection, adaptive mitigation, and multi-layered resilience.

---

🧠 Key Features

**DFAM** – *Dynamic Flow Analysis Module*  
➡️ P4-based data plane monitors ARP traffic and extracts behavioral features (PPS, API, ETP) at line rate.

**ADFDS** – *Adaptive Dynamic Flow Detection System*  
➡️ Ensemble ML model detects ARP/DDoS/Combined attacks using hybrid traffic/ARP indicators with high accuracy.

**DAMS** – *Distributed Adaptive Mitigation System*  
➡️ Multi-controller SDN setup applies real-time, context-aware mitigation using domain-specific policies.

**Multi-Domain Resilience**  
➡️ Supports primary/backup controllers and fault-tolerant recovery in four distributed IoT domains.

📁 Project Structure
```bash

SFARP/

├── DFAM/

│ ├── p4src/

│ │ └── dfam.p4 # P4 code for line-rate ARP analysis
│ └── lcst_config.json # Table/window size, ARP thresholds
│
├── ADFDS/
│ ├── models/
│ │ └── ensemble_model.pkl # Pretrained ensemble ML model
│ ├── scripts/
│ │ ├── train_model.py # ML training pipeline
│ │ └── detect.py # Inference runtime script
│ └── features_config.json # Feature selection file
│
├── DAMS/
│ ├── controller/
│ │ └── mitigation.py # Policy enforcement (Ryu/ONOS)
│ ├── policies/
│ │ └── mitigation_rules.json # Policy configs per attack type
│
├── topology/
│ ├── sfarp_topology.py # Mininet-WiFi 4-domain topology
│ └── config.yaml # Domain-controller-device mapping
│
├── dataset/
│ ├── preprocessing.py
│ ├── balanced_stats.csv # Resampled dataset for ML
│ └── raw/ # CICIoT2023, CICIoMT2024 inputs
│
├── utils/
│ ├── arp_analysis.py # API, DMP, AMC feature extractor
│ └── traffic_features.py # Flow entropy, PPS, etc.
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

🏗️ Requirements

- Python ≥ 3.8  
- Mininet-WiFi ≥ 2.3.0  
- BMv2 with P4Runtime support  
- ONOS / Ryu for multi-controller environment  
- `xgboost`, `scikit-learn`, `pandas`, `joblib`, `grpcio`, `pyyaml`

---

🚀 Quick Start

### 1. Set up the environment

```bash
sudo apt install bmv2 p4c mininet-wifi hping3
pip install -r requirements.txt

2. Deploy the testbed
bash
Copy
Edit
sudo python3 topology/sfarp_topology.py

3. Train or load ML detection model
bash
Copy
Edit
python3 ADFDS/scripts/train_model.py
# or use pretrained ADFDS/models/ensemble_model.pkl

4. Start the SDN controller (Ryu or ONOS)
bash
Copy
Edit
python3 DAMS/controller/mitigation.py

5. Launch detection or attack simulation
bash
Copy
Edit
python3 ADFDS/scripts/detect.py

🧬 ADFDS Ensemble Model

Model architecture:

Base Classifiers: RF, XGBoost, SVM, KNN, GNB

Meta Classifier: ANN

Features: API, PPS, FlowRate, ETP, DMP, AMC, Entropy, etc.

from joblib import load
model = load('ADFDS/models/ensemble_model.pkl')
prediction = model.predict(features)
