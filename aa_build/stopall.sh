podman stop api_backend_1
podman stop infra_api_backend
podman rm api_backend_1
podman rm infra_api_backend

podman pod stop pod_api_backend
podman pod rm pod_api_backend
