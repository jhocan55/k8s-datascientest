# k8s-datascientest

This project demonstrates how to deploy a FastAPI application and a PostgreSQL database on Kubernetes using YAML configurations.

---

## Deployment Overview

### Components:
1. **FastAPI Application**:
   - A Python-based web application built with FastAPI.
   - Exposed via an Ingress for external access.
   - Configured with 3 replicas for high availability.

2. **PostgreSQL Database**:
   - A stateful database deployed using a StatefulSet.
   - Stores persistent data using a PersistentVolumeClaim (PVC).

3. **Kubernetes Objects**:
   - **Deployment**: For the FastAPI application.
   - **StatefulSet**: For the PostgreSQL database.
   - **Services**: To expose the FastAPI app and PostgreSQL internally.
   - **Ingress**: To expose the FastAPI app externally.
   - **ConfigMap**: For non-sensitive PostgreSQL configurations.
   - **Secret**: For sensitive PostgreSQL credentials.

---

## Deployment Steps

### 1. **Build and Push the FastAPI Docker Image**
- Navigate to the directory containing the `Dockerfile`:
  ```bash
  cd /home/alex/Documents/kubernetes/YAML-STANDARD/k8s-datascientest/
  ```
- Build the Docker image:
  ```bash
  docker build -t <your-dockerhub-repo>/fastapi:latest .
  ```
- Push the image to DockerHub:
  ```bash
  docker push <your-dockerhub-repo>/fastapi:latest
  ```

### 2. **Apply Kubernetes Configurations**
- Apply all YAML files in the `k8s-datascientest` directory:
  ```bash
  kubectl apply -f /home/alex/Documents/kubernetes/YAML-STANDARD/k8s-datascientest/
  ```

### 3. **Verify the Deployment**
- Check the status of pods:
  ```bash
  kubectl get pods
  ```
- Check the services:
  ```bash
  kubectl get services
  ```
- Check the ingress:
  ```bash
  kubectl get ingress
  ```

### 4. **Access the Application**
- Use the Ingress URL to access the FastAPI application:
  ```
  http://<your-subdomain>.cloudns.net
  ```
- Use the following routes:
  - `/`: Welcome message.
  - `/users`: List of users.
  - `/users/count`: Count of users.

---

## Notes
- Ensure you have a Kubernetes cluster running with an NGINX ingress controller installed.
- Replace `<your-dockerhub-repo>` and `<your-subdomain>` with your actual DockerHub repository and subdomain.
