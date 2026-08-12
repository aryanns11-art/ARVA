import subprocess
import time

process = subprocess.Popen(["notepad.exe"])

print("PID:", process.pid)
print("Initial status:", process.poll())

time.sleep(10)

print("Status after 10 seconds:", process.poll())

process.wait()

print("Notepad has closed.")

