from flask import Flask, render_template, jsonify
import pandas as pd
from data_generator import generate_health_data
from anomaly_detector import HealthAnomalyDetector
import json

app = Flask(__name__)
detector = HealthAnomalyDetector()

# Initialize with sample data
sample_data = generate_health_data(days=1)
detector.train(sample_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health-data')
def get_health_data():
    """Get current health metrics"""
    current_data = generate_health_data(days=1).tail(1)
    anomalies = detector.predict(current_data)
    
    data = {
        'heart_rate': int(current_data['heart_rate'].iloc[0]),
        'blood_oxygen': int(current_data['blood_oxygen'].iloc[0]),
        'activity_level': current_data['activity_level'].iloc[0],
        'status': anomalies[0],
        'timestamp': current_data['timestamp'].iloc[0].strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Get recommendations
    recommendations = detector.get_recommendations(
        anomalies[0], 
        data['heart_rate'], 
        data['blood_oxygen']
    )
    data['recommendations'] = recommendations
    
    return jsonify(data)

@app.route('/api/history')
def get_history():
    """Get historical health data"""
    history_data = generate_health_data(days=7)
    anomalies = detector.predict(history_data)
    
    history = []
    for i, row in history_data.iterrows():
        history.append({
            'timestamp': row['timestamp'].strftime('%Y-%m-%d %H:%M'),
            'heart_rate': int(row['heart_rate']),
            'blood_oxygen': int(row['blood_oxygen']),
            'status': anomalies[i]
        })
    
    return jsonify(history[-50:])  # Last 50 records

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)