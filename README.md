# DevOps Learning Project

A hands-on project for learning DevOps, step by step.
A small Tasks API that goes through the full DevOps lifecycle.

## Tech Stack
- Python + FastAPI
- PostgreSQL
- Docker + Docker Compose
- Git + GitHub

## Run
```
docker compose up -d --build
```

Then open: http://127.0.0.1:8000/docs

Stop:
```
docker compose down
```

## Roadmap
- [x] Environment, Git and GitHub
- [x] Tasks API (FastAPI)
- [x] Docker
- [x] Docker Compose + PostgreSQL
- [ ] CI with GitHub Actions
- [ ] Kubernetes
- [ ] Terraform
- [ ] Monitoring (Prometheus + Grafana)
- [ ] GitOps (Argo CD)
