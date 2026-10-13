# DevOps Learning Project

A hands-on project for learning DevOps, step by step.
A small Tasks API that goes through the full DevOps lifecycle.

## Tech Stack
- Python + FastAPI
- PostgreSQL
- Docker + Docker Compose
- GitHub Actions (CI + publish to GitHub Container Registry)
- Kubernetes
- Terraform
- Prometheus + Grafana

## Run with Docker Compose
```
docker compose up -d --build
```

| Service    | URL                           |
|------------|-------------------------------|
| API docs   | http://127.0.0.1:8000/docs    |
| Metrics    | http://127.0.0.1:8000/metrics |
| Prometheus | http://127.0.0.1:9090         |
| Grafana    | http://127.0.0.1:3000         |

## Run on Kubernetes
```
kubectl apply -f k8s
kubectl port-forward svc/api 8080:8000
```

Then open: http://127.0.0.1:8080/docs

## Roadmap
- [x] Environment, Git and GitHub
- [x] Tasks API (FastAPI)
- [x] Docker
- [x] Docker Compose + PostgreSQL
- [x] CI with GitHub Actions
- [x] Kubernetes
- [x] Terraform
- [x] Monitoring (Prometheus + Grafana)
- [ ] GitOps (Argo CD)
