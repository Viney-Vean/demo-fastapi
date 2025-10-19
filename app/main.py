from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in Kubernetes DC/DR!"}

@app.get("/health")
def health_check():
    return {"message": "Ok"}

