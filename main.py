from fastapi import FastAPI
import psutil

# This initializes your API
app = FastAPI(title="Homelab Resource Monitor")

# A basic health check endpoint
@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API is running!"}

# The endpoint that actually does the work
@app.get("/metrics")
def get_metrics():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "ram_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent
    }