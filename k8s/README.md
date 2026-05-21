# Kubernetes - PROYECTO_V_JABS
## Vue + Flask + MongoDB con Docker Desktop

---

## Prerequisitos
- Docker Desktop con Kubernetes habilitado (`kubectl get nodes` → docker-desktop Ready)
- Imágenes Docker construidas localmente

---

## Paso 1 — Construir las imágenes Docker localmente

```bash
# Desde la raíz del proyecto
docker build -t proyecto-v-jabs-frontend:latest ./frontend
docker build -t proyecto-v-jabs-backend:latest ./backend
```

---

## Paso 2 — Editar el Secret con tus variables de entorno

Abre `k8s/backend-secret.yml` y completa tus variables del `.env`:

```yaml
stringData:
  MONGO_URI: "mongodb://mongo-service:27017/salon_db"
  JWT_SECRET: "tu_secreto"
  # ... resto de variables
```

---

## Paso 3 — Aplicar los manifiestos en orden

```bash
# 1. Secret (primero, lo necesita el backend)
kubectl apply -f k8s/backend-secret.yml

# 2. MongoDB (con su volumen persistente)
kubectl apply -f k8s/mongo-deployment.yml

# 3. Backend Flask
kubectl apply -f k8s/backend-deployment.yml

# 4. Frontend Vue/Nginx
kubectl apply -f k8s/frontend-deployment.yml
```

---

## Paso 4 — Verificar que todo esté corriendo

```bash
kubectl get pods
kubectl get svc
```

Resultado esperado:
```
NAME                                    READY   STATUS    RESTARTS
frontend-deployment-xxx                 1/1     Running   0
backend-deployment-xxx                  1/1     Running   0
mongo-deployment-xxx                    1/1     Running   0
```

---

## Acceso a la aplicación

| Servicio  | URL                        |
|-----------|---------------------------|
| Frontend  | http://localhost:30300     |
| Backend   | http://localhost:30500     |
| MongoDB   | Solo interno (ClusterIP)   |

---

## Comandos útiles

```bash
# Ver logs de un pod
kubectl logs deployment/backend-deployment
kubectl logs deployment/frontend-deployment

# Escalar el backend a 3 réplicas
kubectl scale deployment backend-deployment --replicas=3

# Eliminar todo
kubectl delete -f k8s/
```

---

## Comunicación entre servicios

En Kubernetes los servicios se comunican por nombre. Tu backend debe
conectarse a MongoDB usando:

```
mongodb://mongo-service:27017/salon_db
```

Asegúrate que tu `MONGO_URI` en el Secret use `mongo-service` 
(no `localhost` ni `mongo` como en docker-compose).
