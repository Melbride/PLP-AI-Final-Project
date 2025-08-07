# Deployment Guide

## Docker Containerization
```bash
# Build the container
docker build -t ai-health-monitor .

# Run locally
docker run -p 5000:5000 ai-health-monitor
```

## Azure Deployment
1. Create Azure account and resource group
2. Deploy to Azure App Service:
   ```bash
   az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name ai-health-monitor --deployment-container-image-name ai-health-monitor
   ```

## AWS Deployment
1. Push to Amazon ECR
2. Deploy using AWS App Runner or ECS

## Google Cloud Deployment
1. Push to Google Container Registry
2. Deploy using Cloud Run

## Kubernetes (Optional)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: health-monitor
spec:
  replicas: 3
  selector:
    matchLabels:
      app: health-monitor
  template:
    metadata:
      labels:
        app: health-monitor
    spec:
      containers:
      - name: health-monitor
        image: ai-health-monitor:latest
        ports:
        - containerPort: 5000
```