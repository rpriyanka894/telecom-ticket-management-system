# Telecom Ticket & Incident Management System
## Project Overview
This project simulates a telecom incident management system where network tickets are created, tracked, and updated.

The application is developed using Python Flask and deployed using Docker and Kuberenetes.

---

## Technologies Used

- Python Flask
- Docker
- Kubernetes
- Minikube
- YAML

---

## Features

- Create telecom incident tickets
- View all tickets
- Filter high-priority incidents
- Update ticket status
- Kubernetes deployment
- Scaling and self-healing

---

## Project Structure

```text
telecom-ticket-system/
|
|--- app.py
|
|--- requirements.txt
|
|--- Dockerfile
|
|--- deployment.yaml
|
|--- service.yaml
|
|--- README.md
```

---

##APIs

### Create Ticket
POST `/create`

### View Tickets
GET `/tickets`

### High Priority Tickets
GET `/high`

### Update Ticket
PUT `/update/<ticket_id>`

---

## Run Application

Install dependencies

```bash
pip install -r requirements.txt
```

Run application:

```bash
python3 app.py
```

Open browser:

```text
http://localhost:5001
```

---

##Docker Commands
Build Docker image:

```bash
docker build -t telecom-ticket-app .
```

Run Docker conatiner:

```bash
docker run -p 5001:5001 telecom-ticket-app
```

---

## Kubernetes Deployment

start minikube:

```bash
minikube start
```

Apply deployment:

```bash
kubectl apply -f deployment.yaml
```

Apply service:

```bash
kubectl apply -f service.yaml
```

check pods:

```bash
kubectl get pods
```

Open service:

```bash
minikube service telecom-ticket-service
```

---

## Kubernetes Features Used

- Pod
- Deployment
- Service
- ReplicaSet
- Scaling
- Self-healing

---

## Sample Use Cases

-Fiber cut incident
- Network outage tracking
- Node failure management
- Telecom alarm ticket handling

---

## Project Output

- Telecom dashboard displaying incident tickets and status management
- Dockerized Python Flask application
- Kubernetes deployment with sacling and self-healing

---

## Resume Description

Developed a Telecom Ticket & Incident Management System using Python Flask, Docker, and Kubernetes for telecom-style incident tracking and deployment automation

---

## Author

Priyanka
