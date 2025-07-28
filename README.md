
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

**High Detection Accuracy, Fast Reaction**  
➡️ Achieves strong classification performance with low-latency mitigation in real-time IoT attack scenarios.

---

📁 Project Structure

```bash
SFARP/
├── DFAM/
│   ├── p4src/
│   │   └── dfam.p4
│   └── lcst_config.json
├── ADFDS/
│   ├── models/
│   │   └── ensemble_model.pkl
│   ├── scripts/
│   │   ├── train_model.py
│   │   └── detect.py
│   └── features_config.json
├── DAMS/
│   ├── controller/
│   │   └── mitigation.py
│   ├── policies/
│   │   └── mitigation_rules.json
├── topology/
│   ├── sfarp_topology.py
│   └── config.yaml
├── dataset/
│   ├── preprocessing.py
│   ├── balanced_stats.csv
│   └── raw/
├── utils/
│   ├── arp_analysis.py
│   └── traffic_features.py
├── requirements.txt
└── README.md

```
---

🏗️ Requirements

- Python ≥ 3.8  
- Mininet-WiFi ≥ 2.3.0  
- BMv2 with P4Runtime support  
- ONOS / Ryu for multi-controller environment  
- xgboost, scikit-learn, pandas, joblib, grpcio, pyyaml

---

🚀 Quick Start

1. Set up the environment
    sudo apt install bmv2 p4c mininet-wifi hping3
    pip install -r requirements.txt

2. Deploy the testbed
    sudo python3 topology/sfarp_topology.py

3. Train or load ML detection model
    python3 ADFDS/scripts/train_model.py

4. Start the SDN controller
    python3 DAMS/controller/mitigation.py

5. Run detection or simulate attack
    python3 ADFDS/scripts/detect.py

---

📊 Evaluation Datasets

Tested on:
- CICIoT2023
- CICIoMT2024
- IoTID20
- TON_IoT


---

🧬 ADFDS Ensemble Model

- Base: RF, XGB, SVM, KNN, GNB  
- Meta: ANN  
- Features: API, PPS, ETP, FlowRate, AMC, etc.

```python
from joblib import load
model = load('ADFDS/models/ensemble_model.pkl')
prediction = model.predict(features)
```

---

🧪 Detected Attack Types

| Attack         | Layer | Description                          |
|----------------|-------|--------------------------------------|
| ARP Spoofing   | L2    | Fake MAC-IP via forged ARP replies   |
| DDoS (SYN/UDP) | L3/L4 | Flooding from distributed botnets    |
| Combined       | L2+3  | ARP spoof + DDoS combo attacks       |

---

