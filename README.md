# DevOps ML Pipeline Assignment

Student: Manas Ramesh More
Subject: Agile and DevOps

## How to Run

1. Build & Run Application:
   `docker compose up -d`

2. Run Monitoring Stack:
   `docker compose -f docker-compose-monitoring.yml up -d`

3. Access Endpoints:
   - App: http://localhost:5000/health
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3001
