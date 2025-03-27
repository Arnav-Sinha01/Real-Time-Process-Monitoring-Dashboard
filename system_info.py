import psutil


def get_system_stats():
    cpu_usage = round(psutil.cpu_percent(), 2)
    memory_usage = round(psutil.virtual_memory().percent, 2)
    disk_usage = round(psutil.disk_usage('/').percent, 2)
    return cpu_usage, memory_usage, disk_usage


def get_process_list(search_text=""):
    processes = [(p.info["pid"], p.info["name"], round(p.info["cpu_percent"], 2), round(p.info["memory_percent"], 2))
                 for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"])]
    processes.sort(key=lambda x: x[2], reverse=True)
    if search_text:
        processes = [p for p in processes if search_text in p[1].lower()]
    return processes


def terminate_process(pid):
    
        process = psutil.Process(pid)
        process.terminate()
        return True, f"Process {pid} terminated successfully."
    
        return False, f"Failed to terminate process {pid}: {str(e)}"
