from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

class HealthAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.label_encoder = LabelEncoder()
        self.is_trained = False
    
    def preprocess_data(self, df):
        """Preprocess data for anomaly detection"""
        df_processed = df.copy()
        df_processed['activity_encoded'] = self.label_encoder.fit_transform(df['activity_level'])
        return df_processed[['heart_rate', 'blood_oxygen', 'activity_encoded']]
    
    def train(self, df):
        """Train the anomaly detection model"""
        X = self.preprocess_data(df)
        self.model.fit(X)
        self.is_trained = True
    
    def predict(self, df):
        """Predict anomalies in health data"""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        
        X = self.preprocess_data(df)
        predictions = self.model.predict(X)
        return ['Anomaly' if pred == -1 else 'Normal' for pred in predictions]
    
    def get_recommendations(self, anomaly_type, heart_rate, blood_oxygen):
        """Generate health recommendations based on anomalies"""
        recommendations = []
        
        if heart_rate > 100:
            recommendations.append("High heart rate detected. Consider rest and hydration.")
        elif heart_rate < 60:
            recommendations.append("Low heart rate detected. Monitor closely.")
        
        if blood_oxygen < 95:
            recommendations.append("Low blood oxygen. Seek medical attention if persistent.")
        
        if not recommendations:
            recommendations.append("All metrics appear normal. Keep up the good work!")
        
        return recommendations