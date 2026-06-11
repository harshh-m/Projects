import psutil
import platform

print("=" * 40)
print("      PC INFORMATION TOOL")
print("=" * 40)

# System Info
print(f"System      : {platform.system()}")
print(f"Release     : {platform.release()}")
print(f"Machine     : {platform.machine()}")
print(f"Processor   : {platform.processor()}")

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"\nCPU Usage   : {cpu_usage}%")

# RAM Usage
memory = psutil.virtual_memory()
print(f"RAM Total   : {round(memory.total / (1024**3), 2)} GB")
print(f"RAM Used    : {round(memory.used / (1024**3), 2)} GB")
print(f"RAM Usage   : {memory.percent}%")

# Disk Usage
disk = psutil.disk_usage('/')
print(f"\nDisk Total  : {round(disk.total / (1024**3), 2)} GB")
print(f"Disk Used   : {round(disk.used / (1024**3), 2)} GB")
print(f"Disk Usage  : {disk.percent}%")

# Battery Info
battery = psutil.sensors_battery()

if battery:
    print(f"\nBattery     : {battery.percent}%")
    print(f"Charging    : {battery.power_plugged}")
else:
    print("\nBattery Info Not Available")

print("=" * 40)