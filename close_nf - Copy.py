import psutil
import time

def close_process(process_name):
    found = False
    for process in psutil.process_iter(['pid', 'name', 'username']):
        if process.info['name'] == process_name:
            try:
                print(f"Terminating {process_name} (PID: {process.info['pid']}, User: {process.info['username']})")
                process.terminate()  # Sends termination signal
                found = True
            except psutil.AccessDenied:
                print(f"Access denied for {process_name} (PID: {process.info['pid']}). Run the script as an administrator.")
            except psutil.NoSuchProcess:
                print(f"{process_name} (PID: {process.info['pid']}) no longer exists.")
    return found

if __name__ == "__main__":
    process_to_close = "NF.exe"
    print("Monitoring for processes...")
    try:
        while True:
            if close_process(process_to_close):
                print(f"{process_to_close} was found and terminated.")
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
