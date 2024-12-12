# Docker Setup
Create two Docker containers for the isolated codes:

## Dockerfile for Container 1

```
FROM python:3.8-slim
WORKDIR /app
COPY code1.py .
CMD ["python", "code1.py"]
```

## Dockerfile for Container 2

```
FROM python:3.8-slim
WORKDIR /app
COPY code2.py .
CMD ["python", "code2.py"]
```


## Build and Run Containers

```
    docker build -t container1_image -f Dockerfile1 .
    docker build -t container2_image -f Dockerfile2 .

    docker run -d --name container1 container1_image
    docker run -d --name container2 container2_image
```

## Resource Management

### For GPU management:

```
    Install NVIDIA Docker to enable GPU sharing.
    Start the containers with GPU access:

    docker run -d --name container1 --gpus all container1_image
    docker run -d --name container2 --gpus all container2_image
```
