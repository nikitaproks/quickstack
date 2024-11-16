from fastapi import FastAPI

app = FastAPI()


@app.get("/api/health")
def health():
    return {"message": "Healthy"}
