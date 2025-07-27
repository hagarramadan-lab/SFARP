# SFARP: A Multi-Layered SDN Framework for Real-Time Defense

SFARP is a secure, scalable framework for defending SD-IoT networks from ARP spoofing and DDoS attacks using:
- **DFAM**: P4-based dynamic traffic analysis
- **ADFDS**: Ensemble machine learning for hybrid detection
- **DAMS**: Multi-controller distributed mitigation

## 🔧 Repository Structure
SFARP/
├── DFAM/ # P4 traffic analyzer
├── ADFDS/ # ML-based attack detector
├── DAMS/ # Distributed mitigation
├── topology/ # Mininet-WiFi topologies
├── dataset/ # Preprocessed attack data
├── utils/ # Feature + ARP analyzers
├── requirements.txt
└── README.md

## 📦 Setup

```bash
pip install -r requirements.txt
sudo mn --custom topology/sfarp_topology.py --topo sfarp

📁 Datasets
CICIoT2023

CICIoMT2024
Place CSVs under dataset/raw/

🧠 Detection
Ensemble: RF + XGB + SVM + GNB + kNN

Features: Entropy, FlowRate, DMP, API, PPS

📡 Topology
Multi-domain

4 switches, 4 APs, 20 hosts

Central + backup + 2 domain controllers

🛡️ MITIGATION
SDN (Ryu/ONOS)

Policy-based + dynamic

Real-time ARP + Flood defense
