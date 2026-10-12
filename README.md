# DevOps Learning Project

A hands-on project for learning DevOps, step by step.
A small Tasks API that goes through the full DevOps lifecycle.

## Tech Stack
- Python + FastAPI
- Docker
- Git + GitHub

## Run with Docker
docker build -t tasks-api .
docker run -d --rm --name tasks -p 8000:8000 tasks-api

Then open: http://127.0.0.1:8000/docs

## Roadmap
- [x] Environment, Git and GitHub
- [x] Tasks API (FastAPI)
- [x] Docker
- [ ] Docker Compose + PostgreSQL
- [ ] CI with GitHub Actions
- [ ] Kubernetes
- [ ] Terraform
- [ ] Monitoring (Prometheus + Grafana)
- [ ] GitOps (Argo CD)
