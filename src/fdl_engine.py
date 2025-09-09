# Placeholder FDL Engine entrypoint (skeleton).
from fastapi import FastAPI

app = FastAPI(title="Protonoveya Node", version="0.1")

@app.get("/health")
def health():
    return {"status": "ok"}
