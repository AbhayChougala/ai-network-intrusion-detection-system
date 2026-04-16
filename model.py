from sklearn.ensemble import IsolationForest
import random
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def simulate_attack(df):
    avg_length = df['Length'].mean()

    attack_types = ["DDoS", "Port Scan", "Malware"]

    # Decide whether to inject attacks
    if avg_length > 300:   
        num_attacks = random.randint(2, 10)
    else:
        num_attacks = random.randint(1, 3)

    for i in range(num_attacks):
        attack_type = random.choice(attack_types)

        # Simulate different attack patterns
        if attack_type == "DDoS":
            length = random.randint(1200, 2000)   # large packets
        elif attack_type == "Port Scan":
            length = random.randint(40, 100)      # small packets
        else:  # Malware
            length = random.randint(500, 1500)

        df.loc[len(df)] = [
            "192.168.1.100",     
            "10.0.0.5",          
            attack_type,
            length,
            80
        ]

    return df


# def detect_anomalies(df):
#     model = IsolationForest(contamination=0.05)

#     # Only numeric feature used
#     df_numeric = df[['Length']]

#     df['Anomaly'] = model.fit_predict(df_numeric)

#     return df



def detect_anomalies(df):
    if df.empty:
        return df

    # 1. Prepare features
    # We convert 'Protocol' to numbers so the ML model can understand it
    le = LabelEncoder()
    df_encoded = df.copy()
    df_encoded['Protocol_Num'] = le.fit_transform(df['Protocol'].astype(str))

    # 2. Use multiple features for detection
    # Now the AI considers Length AND Protocol AND Port
    features = ['Length', 'Protocol_Num']
    if 'Port' in df.columns:
        features.append('Port')

    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly'] = model.fit_predict(df_encoded[features])

    return df