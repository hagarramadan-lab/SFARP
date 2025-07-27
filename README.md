# SFARP: Secure Framework for ARP and DDoS Protection in SD-IoT

**SFARP** is a multi-layered Software Defined Networking (SDN) framework designed to detect and mitigate coordinated ARP spoofing and DDoS attacks in IoT networks using programmable data planes and machine learning.

---

## 📁 Repository Structure

SFARP/
├── DFAM/ # P4-based ARP/Flood detection
│ ├── p4src/dfam.p4
│ └── lcst_config.json
│
├── ADFDS/ # ML-based traffic classification
│ ├── models/ensemble_model.pkl
│ ├── scripts/
│ │ ├── train_model.py
│ │ └── detect.py
│ └── features_config.json
│
├── DAMS/ # Mitigation module
│ ├── controller/mitigation.py
│ └── policies/mitigation_rules.json
│
├── topology/ # Network emulation (Mininet-WiFi)
│ ├── sfarp_topology.py
│ └── config.yaml
│
├── dataset/ # Placeholder for dataset & preprocessing
├── utils/ # Helper scripts (ARP analysis, etc.)
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/hagarramadan-lab/SFARP.git
cd SFARP

2. Install dependencies

bash
Copy
Edit

3. Run the Mininet topology

bash
Copy
Edit
sudo python3 topology/sfarp_topology.py

4. Train detection model

bash
Copy
Edit
python3 ADFDS/scripts/train_model.py

5. Run inference

bash
Copy
Edit
python3 ADFDS/scripts/detect.py dataset/test_sample.csv

🛡️ Disclaimer
This repository is intended for research and academic use. Please ensure compliance with your institution’s ethical and security guidelines.

