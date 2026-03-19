# Homelab Resource Monitor

A containerized Python microservice built with FastAPI that exposes real-time Linux hardware metrics (CPU, RAM, Disk). Deployed via Ansible to a Proxmox hypervisor.

## Architecture
* **Language:** Python 3 (FastAPI, uvicorn, psutil)
* **Containerization:** Podman / Docker
* **Automation:** Ansible (Infrastructure as Code)
* **Hosting:** Proxmox VE (Privileged LXC)

## Deployment Instructions

1. Clone this repository:
   `git clone https://github.com/YOUR_USERNAME/homelab-resource-monitor.git`
2. Update the `hosts.ini` file with your target server IP.
3. Run the Ansible playbook:
   `ansible-playbook -i hosts.ini deploy.yml -u root -k`
4. Access the API documentation at `http://<SERVER_IP>:8000/docs`.

## Available Endpoints
* `/` - Health check status.
* `/metrics` - Returns real-time CPU, RAM, and Disk usage in JSON format.

## Lessons Learned & Troubleshooting
During the deployment of this architecture, I encountered and resolved several deep-level Linux networking and hypervisor constraints:
* **Nested Virtualization:** Bypassed Proxmox kernel restrictions by converting the target LXC from Unprivileged to Privileged, allowing Podman to properly map user-space network namespaces (`netns`) without throwing IO errors.
* **Firewall Routing:** Diagnosed dropped TCP packets by verifying Layer 3 routing via ICMP/Ping, eliminating Tailscale exit nodes as the culprit, and ensuring the Linux kernel had IP Forwarding (`net.ipv4.ip_forward=1`) enabled to route external requests into the container's virtual network.
