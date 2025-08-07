import unittest
import pandas as pd
from data_generator import generate_health_data
from anomaly_detector import HealthAnomalyDetector

class TestHealthMonitoringSystem(unittest.TestCase):
    
    def setUp(self):
        self.detector = HealthAnomalyDetector()
        self.sample_data = generate_health_data(days=1)
        self.detector.train(self.sample_data)
    
    def test_data_generation(self):
        """Test health data generation"""
        data = generate_health_data(days=1)
        self.assertGreater(len(data), 0)
        self.assertIn('heart_rate', data.columns)
        self.assertIn('blood_oxygen', data.columns)
        self.assertIn('activity_level', data.columns)
    
    def test_anomaly_detection(self):
        """Test anomaly detection functionality"""
        predictions = self.detector.predict(self.sample_data)
        self.assertEqual(len(predictions), len(self.sample_data))
        self.assertTrue(all(pred in ['Normal', 'Anomaly'] for pred in predictions))
    
    def test_recommendations(self):
        """Test recommendation generation"""
        recommendations = self.detector.get_recommendations('Normal', 75, 98)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()