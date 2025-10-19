
```bash

docker build -t vineyveanrnd/fastapi-k8s:latest .
docker push vineyveanrnd/fastapi-k8s:latest

```

```bash

docker build -t vineyveanrnd/fastapi-k8s:v202510051 .
docker push vineyveanrnd/fastapi-k8s:v202510051

```
```bash
kubectl --context kind-dc apply -f fastapi-deploy.yaml
kubectl --context kind-dr apply -f fastapi-deploy.yaml
```
kubectl --context kind-dc get svc fastapi-service
