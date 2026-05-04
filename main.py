from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import psutil

app = FastAPI(title="Homelab Resource Monitor")


@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running!"}


@app.get("/metrics", response_class=PlainTextResponse)
def get_system_metrics():
    # Using interval=None returns the average usage since the last call (non-blocking)
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent

    disk_info = psutil.disk_usage('/')
    disk_free_gb = round(disk_info.free / (1024 ** 3), 2)
    disk_total_gb = round(disk_info.total / (1024 ** 3), 2)

    return (
        f"# HELP homelab_cpu_usage_percent CPU usage percent\n"
        f"# TYPE homelab_cpu_usage_percent gauge\n"
        f"homelab_cpu_usage_percent {cpu}\n"
        f"# HELP homelab_ram_usage_percent RAM usage percent\n"
        f"# TYPE homelab_ram_usage_percent gauge\n"
        f"homelab_ram_usage_percent {ram}\n"
        f"# HELP homelab_disk_free_gb Free disk space in GB\n"
        f"# TYPE homelab_disk_free_gb gauge\n"
        f"homelab_disk_free_gb {disk_free_gb}\n"
        f"# HELP homelab_disk_total_gb Total disk space in GB\n"
        f"# TYPE homelab_disk_total_gb gauge\n"
        f"homelab_disk_total_gb {disk_total_gb}\n"
    )