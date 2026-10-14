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
- Argo CD (GitOps)

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

## Run on Kubernetes with Argo CD (GitOps)
Install Argo CD and register the app once:
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v3.0.6/manifests/install.yaml
kubectl apply -f argocd/app.yaml
```

From now on, every merge to `main` that changes `k8s/` is deployed automatically.

## How a change reaches production
1. Create a branch and open a Pull Request
2. GitHub Actions builds and tests the app
3. Merge to `main`
4. GitHub Actions publishes the image to `ghcr.io`
5. Argo CD syncs the cluster to match Git

## Roadmap
- [x] Environment, Git and GitHub
- [x] Tasks API (FastAPI)
- [x] Docker
- [x] Docker Compose + PostgreSQL
- [x] CI with GitHub Actions
- [x] Kubernetes
- [x] Terraform
- [x] Monitoring (Prometheus + Grafana)
- [x] GitOps (Argo CD)
