from fastapi import FastAPI
import psutil

app = FastAPI(title="Homelab Resource Monitor")


@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running!"}


@app.get("/metrics")
def get_system_metrics():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    disk_info = psutil.disk_usage('/')
    disk_free_gb = round(disk_info.free / (1024 ** 3), 2)
    disk_total_gb = round(disk_info.total / (1024 ** 3), 2)

    return {
        "cpu_usage_percent": cpu,
        "ram_usage_percent": ram,
        "disk_free_gb": disk_free_gb,
        "disk_total_gb": disk_total_gb
    }