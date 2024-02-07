import psutil
import time

def close_edge(time):
    time.sleep(time)
    for process in psutil.process_iter(['pid', 'name']):
        # Check if the process name is Microsoft Edge
        if 'msedge' in process.info['name'].lower():
            pid = process.info['pid']
            try:
                # Terminate the process
                psutil.Process(pid).terminate()
                print(f"Closed Edge process with PID: {pid}")
            except psutil.NoSuchProcess:
                print(f"No process found with PID: {pid}")
            except Exception as e:
                print(f"Error closing process {pid}: {e}")

if __name__ == "__main__":
    close_edge()
