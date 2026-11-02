# Linux System Resource Monitoring Dashboard
#Abstract
The Linux System Resource Monitoring Dashboard is a Python-based application that monitors and displays the current resource utilization of a Linux computer. It collects information about CPU usage, memory consumption, disk usage, disk I/O, and running processes.
The dashboard identifies processes that consume high amounts of CPU or memory. It helps users understand system performance, detect resource-intensive applications, and analyze resource utilization. The project demonstrates important Operating System concepts, including process management, memory management, file systems, process monitoring, and system resource allocation.


## Aim
To build a Python-based Linux dashboard that monitors CPU, memory, disk usage,
disk I/O and processes, and highlights processes using unusually high resources.

## Requirements
- Linux operating system (Ubuntu, Debian, Fedora, etc.)
- Python 3
- psutil Python library
- Terminal

## Installation
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 -m pip install --user psutil
```

If pip reports an externally-managed-environment error, use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install psutil
```

## Run
```bash
python3 linux_resource_dashboard.py
```
Stop with `Ctrl+C`.

## Monitored parameters
- CPU utilization percentage
- RAM and swap usage
- Root filesystem usage
- Disk read/write throughput
- Top processes by CPU usage
- High CPU/RAM usage warnings

Thresholds and refresh interval can be changed at the top of the Python file.
The program only monitors system information; it does not kill or modify processes.
