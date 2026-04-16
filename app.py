from flask import Flask, render_template
from sniffer import capture_packets
from model import detect_anomalies, simulate_attack
import pandas as pd
import matplotlib
matplotlib.use('Agg')   
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def generate_graph(df):
    if not os.path.exists("static"):
        os.makedirs("static")

    plt.figure()
    df['Length'].plot(kind='line', title='Packet Length Over Time')
    plt.xlabel("Packet Index")
    plt.ylabel("Length")
    plt.savefig("static/graph.png")
    plt.close()

@app.route('/')
def dashboard():
    df = capture_packets()

    df = simulate_attack(df)

    df = detect_anomalies(df)

    anomalies = df[df['Anomaly'] == -1].shape[0]
    
    attack_types = ["DDoS", "Port Scan", "Malware"]
    simulated_attacks = df[df['Protocol'].isin(attack_types)].shape[0]

    if anomalies > 5:
        alert_msg = "HIGH RISK TRAFFIC DETECTED"
    else:
        alert_msg = "Network is Stable"

    protocol_counts = df['Protocol'].value_counts().to_dict()
    generate_graph(df)

    if os.path.exists("logs_history.csv"):
        old_df = pd.read_csv("logs_history.csv")
        combined_df = pd.concat([old_df, df])
    else:
        combined_df = df

    combined_df.to_csv("logs_history.csv", index=False)
    
    return render_template("dashboard.html",
                           tables=df.to_html(classes='data', index=False),
                           anomalies=anomalies, 
                           alert_msg=alert_msg,
                           simulated=simulated_attacks,
                           protocol_counts=protocol_counts)
    
if __name__ == '__main__':
    app.run(debug=True)