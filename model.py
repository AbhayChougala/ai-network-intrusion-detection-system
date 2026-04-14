from sklearn.ensemble import IsolationForest
import random

def simulate_attack(df):
    # ✅ Condition-based attack trigger
    avg_length = df['Length'].mean()

    attack_types = ["DDoS", "Port Scan", "Malware"]

    # Decide whether to inject attacks
    if avg_length > 300:   # threshold (you can tweak)
        num_attacks = random.randint(2, 10)
    else:
        num_attacks = random.randint(0, 3)

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
            "192.168.1.100",     # fake attacker IP
            "10.0.0.5",          # victim IP
            attack_type,
            length
        ]

    return df


def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)

    # Only numeric feature used
    df_numeric = df[['Length']]

    df['Anomaly'] = model.fit_predict(df_numeric)

    return df