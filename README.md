🖥️ Linux System Resource Monitoring Dashboard

A Python-based Linux System Resource Monitoring Dashboard that monitors and displays real-time system performance information, including CPU usage, RAM utilization, disk storage, disk I/O, and running processes.

📌 Project Overview

The Linux System Resource Monitoring Dashboard is a mini project developed to understand and demonstrate important Operating System concepts using Python.

It collects system information from the Linux "/proc" filesystem and displays resource utilization through a terminal-based dashboard that refreshes every 3 seconds.

The project helps users identify resource-intensive processes and understand system performance.

🎯 Objectives

- Monitor real-time CPU utilization.
- Display total, used, and available RAM.
- Monitor disk capacity and storage utilization.
- Display disk read/write activity.
- List running processes and their resource consumption.
- Identify high-CPU and high-memory processes.
- Refresh monitoring information periodically.
- Display system statistics in a simple dashboard.

✨ Features

- Real-time CPU usage monitoring.
- RAM usage and availability monitoring.
- Disk space monitoring.
- Running process information.
- Top 5 memory-consuming processes.
- Automatic dashboard refresh every 3 seconds.
- Simple terminal-based interface.
- Safe program termination using "Ctrl + C".

🛠️ Technologies Used

Technology| Purpose
Python 3| Programming language
Linux| Operating system
"/proc" filesystem| System resource information
OS Module| Operating system interaction
Time Module| Refresh interval
Platform Module| System information

🧠 Operating System Concepts Used

- Process Management: Listing and monitoring running processes.
- CPU Management: Measuring CPU utilization.
- Memory Management: Monitoring RAM usage.
- File Systems: Checking disk capacity and free space.
- Disk I/O: Monitoring disk read/write activity.
- System Monitoring: Collecting and displaying system statistics.

⚙️ Requirements

- Linux operating system
- Python 3 installed
- Terminal or command-line interface

🚀 Installation & Execution

Step 1: Clone the repository

git clone https://github.com/YOUR-USERNAME/linux-system-resource-monitoring-dashboard.git

Step 2: Open the project folder

cd linux-system-resource-monitoring-dashboard

Step 3: Run the Python program

python3 main.py

Step 4: Stop the dashboard

Press:

Ctrl + C

📊 Sample Output

 LINUX SYSTEM RESOURCE MONITORING DASHBOARD


Operating System: Linux
Computer Name: Your-Computer

CPU Usage: 7.25%

Total RAM: 7938.40 MB
Used RAM: 3064.74 MB
Available RAM: 4873.66 MB
Memory Usage: 38.61%

Top 5 Processes by Memory Usage

PID       Memory (MB)       P

Refreshing every 3 seconds...
Press Ctrl+C to stop.

Note: Actual values depend on the computer and running applications.

🧪 Testing

The project includes the following test cases:

1. Run the program – Dashboard displays system statistics.
2. Open a CPU-intensive application – CPU usage may increase.
3. Run several applications – Memory usage updates.
4. Reach CPU usage of 80% or above – High CPU warning is expected.
5. Reach memory usage of 80% or above – High memory warning is expected.
6. Copy a large file – Disk I/O counters may increase.
7. Press "Ctrl + C" – Monitoring terminates safely.

🔮 Future Enhancements

- Graphical user interface (GUI).
- Real-time performance charts.
- High CPU and memory usage alerts.
- Disk I/O monitoring improvements.
- Multi-computer monitoring.
- Historical resource usage reports.

👨‍💻 Team Members

This mini project was developed by the following students:

Name| Student ID
Simi Mallick| 27631725022
Kunal Das| 27631725018
Chandan Pal| 27631725023
Gourab Pan| 27631725020
Raunak Kumar Singh| 27631725019

👨‍🏫 Project Guide

Dr. Munshi Yusuf Alam

Department of Computer Science & Engineering (Cyber Security)
Budge Budge Institute of Technology (BBIT)

Semester: Fifth
Academic Year: 2026–2027

📚 References

1. Operating System Concepts – Silberschatz, Galvin and Gagne.
2. Modern Operating Systems – Andrew S. Tanenbaum.
3. The Linux Programming Interface – Michael Kerrisk.
4. "Linux "/proc" Documentation" (https://man7.org/linux/man-pages/man5/proc.5.html)
5. "Python Documentation" (https://docs.python.org/3/)
6. "psutil Documentation" (https://psutil.readthedocs.io/)
