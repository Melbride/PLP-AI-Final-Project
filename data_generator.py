import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_health_data(days=7):
    """Generate simulated health data for testing"""
    timestamps = pd.date_range(
        start=datetime.now() - timedelta(days=days),
        end=datetime.now(),
        freq='5T'  # Every 5 minutes
    )
    
    data = {
        'timestamp': timestamps,
        'heart_rate': np.random.normal(75, 10, len(timestamps)).astype(int),
        'blood_oxygen': np.random.normal(98, 2, len(timestamps)).astype(int),
        'activity_level': np.random.choice(['low', 'moderate', 'high'], len(timestamps))
    }
    
    # Add some anomalies
    anomaly_indices = np.random.choice(len(timestamps), size=int(len(timestamps) * 0.05), replace=False)
    for idx in anomaly_indices:
        data['heart_rate'][idx] = np.random.choice([45, 120])  # Very low or high
        data['blood_oxygen'][idx] = np.random.choice([85, 88])  # Low oxygen
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_health_data()
    df.to_csv('health_data.csv', index=False)
    print(f"Generated {len(df)} health records")