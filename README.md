# AI-Powered Health Monitoring System

## Overview
Real-time health monitoring system using AI to detect anomalies and provide personalized recommendations.

## Features
- Real-time health data simulation
- AI-powered anomaly detection
- Personalized health recommendations
- Web-based dashboard
- Automated testing

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access dashboard:**
   Open http://localhost:5000 in your browser

4. **Run tests:**
   ```bash
   python test_system.py
   ```

## Project Structure
```
health_monitoring_system/
├── app.py                 # Flask web application
├── data_generator.py      # Health data simulation
├── anomaly_detector.py    # AI anomaly detection
├── test_system.py         # Unit tests
├── templates/
│   └── index.html         # Dashboard UI
└── requirements.txt       # Dependencies
```

## Health Metrics Monitored
- Heart Rate (BPM)
- Blood Oxygen Levels (%)
- Activity Level (low/moderate/high)

## AI Model
- **Algorithm:** Isolation Forest
- **Purpose:** Detect health anomalies
- **Features:** Heart rate, blood oxygen, activity level

## Deployment Ready
- Containerizable with Docker
- Cloud deployment compatible (AWS, Azure, GCP)
- RESTful API endpoints

## SDG Alignment
Supports UN SDG 3 (Good Health and Well-being) through accessible health monitoring technology.