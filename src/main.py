from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Purge Orchestrator is Live"}

@app.get("/health")
def health_check():
    # DigitalOcean uses this to verify your container started correctly
    return {"status": "healthy"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("src.main:app", host="127.0.0.1", port=8080, reload=True)