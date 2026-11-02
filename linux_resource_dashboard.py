#!/usr/bin/env python3
"""
Linux System Resource Monitoring Dashboard
Monitors CPU, RAM, disk usage, disk I/O and high-resource processes.
Run: python3 linux_resource_dashboard.py
Exit: Ctrl+C
"""
import os
import time
import shutil
import platform
from datetime import datetime

try:
    import psutil
except ImportError:
    print("Missing dependency. Install it with: python3 -m pip install psutil")
    raise SystemExit(1)

REFRESH_SECONDS = 2
HIGH_CPU_PERCENT = 70.0
HIGH_MEMORY_PERCENT = 70.0
TOP_PROCESSES = 8

def bytes_to_gb(value):
    return value / (1024 ** 3)

def bar(percent, width=24):
    percent = max(0.0, min(100.0, float(percent)))
    filled = int(width * percent / 100)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {percent:5.1f}%"

def safe_process_info(proc):
    try:
        with proc.oneshot():
            name = proc.info.get("name") or "Unknown"
            pid = proc.info.get("pid")
            cpu = proc.cpu_percent(interval=None)
            mem = proc.memory_percent()
            status = proc.status()
        return {"pid": pid, "name": name[:22], "cpu": cpu,
                "mem": mem, "status": status}
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None

def get_processes():
    items = []
    for proc in psutil.process_iter(["pid", "name"]):
        info = safe_process_info(proc)
        if info:
            items.append(info)
    return sorted(items, key=lambda p: p["cpu"], reverse=True)

def disk_io_rate(previous, current, elapsed):
    if not previous or not current or elapsed <= 0:
        return 0.0, 0.0
    read_rate = max(0, current.read_bytes - previous.read_bytes) / elapsed
    write_rate = max(0, current.write_bytes - previous.write_bytes) / elapsed
    return read_rate, write_rate

def main():
    psutil.cpu_percent(interval=None)  # prime CPU measurement
    previous_io = psutil.disk_io_counters()
    previous_time = time.time()

    try:
        while True:
            now = time.time()
            elapsed = max(0.1, now - previous_time)
            cpu = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            root_disk = psutil.disk_usage("/")
            current_io = psutil.disk_io_counters()
            read_rate, write_rate = disk_io_rate(previous_io, current_io, elapsed)

            processes = get_processes()
            high_cpu = [p for p in processes if p["cpu"] >= HIGH_CPU_PERCENT]
            high_mem = [p for p in processes if p["mem"] >= HIGH_MEMORY_PERCENT]

            os.system("clear")
            print("=" * 78)
            print("                 LINUX SYSTEM RESOURCE MONITORING DASHBOARD")
            print("=" * 78)
            print(f"Host: {platform.node()} | OS: {platform.system()} {platform.release()}")
            print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Refresh: {REFRESH_SECONDS}s")
            print("-" * 78)

            print("CPU")
            print(bar(cpu))
            print("\nMEMORY (RAM)")
            print(bar(memory.percent))
            print(f"Used: {bytes_to_gb(memory.used):.2f} GB / "
                  f"{bytes_to_gb(memory.total):.2f} GB | Available: "
                  f"{bytes_to_gb(memory.available):.2f} GB")
            print("\nSWAP")
            print(bar(swap.percent))
            print(f"Used: {bytes_to_gb(swap.used):.2f} GB / "
                  f"{bytes_to_gb(swap.total):.2f} GB")
            print("\nROOT DISK (/)")
            print(bar(root_disk.percent))
            print(f"Used: {bytes_to_gb(root_disk.used):.2f} GB / "
                  f"{bytes_to_gb(root_disk.total):.2f} GB | "
                  f"Free: {bytes_to_gb(root_disk.free):.2f} GB")
            print("\nDISK I/O")
            print(f"Read: {bytes_to_gb(read_rate * 3600):.3f} GB/hour "
                  f"({read_rate / (1024**2):.2f} MB/s) | "
                  f"Write: {write_rate / (1024**2):.2f} MB/s")
            print("\nTOP PROCESSES (sorted by CPU usage)")
            print(f"{'PID':>7}  {'PROCESS':<23} {'CPU %':>8} {'MEM %':>8}  STATUS")
            print("-" * 65)
            for p in processes[:TOP_PROCESSES]:
                print(f"{p['pid']:>7}  {p['name']:<23} "
                      f"{p['cpu']:>7.1f}% {p['mem']:>7.1f}%  {p['status']}")
            if not processes:
                print("No process information available.")

            print("\nALERTS")
            alerts = []
            if cpu >= HIGH_CPU_PERCENT:
                alerts.append(f"High total CPU usage: {cpu:.1f}%")
            if memory.percent >= HIGH_MEMORY_PERCENT:
                alerts.append(f"High RAM usage: {memory.percent:.1f}%")
            if high_cpu:
                alerts.append("High-CPU process(es): " +
                              ", ".join(f"{p['name']} (PID {p['pid']})" for p in high_cpu[:4]))
            if high_mem:
                alerts.append("High-memory process(es): " +
                              ", ".join(f"{p['name']} (PID {p['pid']})" for p in high_mem[:4]))
            if alerts:
                for alert in alerts:
                    print("WARNING: " + alert)
            else:
                print("No high-utilization warning at the configured thresholds.")

            print("\nPress Ctrl+C to stop.")
            previous_io = current_io
            previous_time = now
            time.sleep(REFRESH_SECONDS)

    except KeyboardInterrupt:
        print("\nMonitoring stopped. Thank you.")

if __name__ == "__main__":
    main()
