# AI-Based Network Intrusion Detection System (IDS)

## Overview

This project implements a real-time Network Intrusion Detection System (IDS) using Python. It captures live network traffic, analyzes packet data, detects anomalies using a machine learning model, and visualizes results through an interactive web dashboard.

The system is designed to demonstrate how modern cybersecurity tools monitor, analyze, and detect suspicious network activity in real time.

---

## Features

- Real-time packet capture using Scapy
- Machine learning-based anomaly detection using Isolation Forest
- Dynamic attack simulation (DDoS, Port Scan, Malware)
- Web-based dashboard using Flask
- Traffic visualization using graphs and charts
- Auto-refresh for real-time updates
- IP tracking (source and destination)
- Log storage and history tracking
- Protocol distribution analysis
- Alert system for network status

---

## System Architecture

Network Traffic → Packet Capture → Feature Extraction → Anomaly Detection → Dashboard Visualization

---

## Technologies Used

- Python
- Scapy
- Flask
- Scikit-learn
- Matplotlib
- Pandas

---

## Machine Learning Model

The system uses the Isolation Forest algorithm for anomaly detection.

- It identifies unusual patterns in packet size
- It does not rely on predefined rules
- Output:
  - 1 indicates normal traffic
  - -1 indicates suspicious traffic

---

## Attack Simulation

The system simulates different types of cyber attacks to demonstrate detection capabilities:

- DDoS: Large packet sizes representing traffic flooding
- Port Scan: Small packet sizes representing probing behavior
- Malware: Mixed packet sizes representing irregular activity

The number and type of attacks are dynamically generated based on network conditions.

---

## Dashboard Features

- Tabular display of captured packet data
- Protocol distribution summary
- Total attack count
- Real-time traffic graph
- Protocol distribution chart
- Attack distribution chart
- Network status alerts (Stable or High Risk)

---

## Installation

Clone the repository:

git clone https://github.com/your-username/ai-network-intrusion-detection-system.git

cd ai-network-intrusion-detection-system

Install dependencies:


pip3 install -r requirements.txt


---

## Running the Project

Run the application with administrative privileges:


sudo python3 app.py


Open the browser and go to:


http://localhost:5000


---

## Project Structure


network-security-project/
│── app.py
│── sniffer.py
│── model.py
│── requirements.txt
│── logs.csv
│── logs_history.csv
│── static/
│ ├── graph.png
│ ├── protocol_chart.png
│ ├── attack_chart.png
│── templates/
│ └── dashboard.html
│── README.md


---

## Use Cases

- Network traffic monitoring
- Intrusion detection systems
- Cybersecurity learning and demonstration
- Basic research in anomaly detection

---

## Future Scope

- Integration with deep learning models
- Cloud-based deployment
- Real-time alert notifications (email or SMS)
- Integration with firewall systems
- Advanced attack classification

---

## Author

Abhay Chougala

---

## Acknowledgements

This project is inspired by widely used network security tools such as Wireshark and Snort, and demonstrates similar concepts in a simplified and programmable form.

---

## License

This project is intended for academic and educational use.
