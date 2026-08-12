import subprocess
import os
import time

print("Python PID:", os.getpid())

process = subprocess.Popen(["notepad.exe"])

print("Notepad PID:", process.pid)

time.sleep(2)

result = subprocess.run(
    ["tasklist", "/FI", f"PID eq {process.pid}"],
    capture_output=True,
    text=True
)

print("\nWindows says:")
print(result.stdout)

time.sleep(60)