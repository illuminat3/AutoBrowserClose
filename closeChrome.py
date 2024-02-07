import psutil
import time

def close_chrome(timeS):
    time.sleep(timeS)
    for process in psutil.process_iter(['pid', 'name']):
        # Check if the process name is Google Chrome
        if 'chrome' in process.info['name'].lower():
            pid = process.info['pid']
            try:
                # Terminate the process
                psutil.Process(pid).terminate()
                print(f"Closed Chrome process with PID: {pid}")
            except psutil.NoSuchProcess:
                print(f"No process found with PID: {pid}")
            except Exception as e:
                print(f"Error closing process {pid}: {e}")
