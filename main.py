from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Deploy su Kubernetes con ArgoCD! Al momento ho aggiunto Github Actions"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
