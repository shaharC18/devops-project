terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.35"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "docker-desktop"
}

resource "kubernetes_namespace" "staging" {
  metadata {
    name = "staging"

    labels = {
      environment = "staging"
      managed-by  = "terraform"
    }
  }
}
