import psutil
import time


def get_system_stats():
    cpu_usage = round(psutil.cpu_percent(), 2)
    memory_usage = round(psutil.virtual_memory().percent, 2)
    disk_usage = round(psutil.disk_usage('/').percent, 2)
    return cpu_usage, memory_usage, disk_usage


# Cache for process data
_process_cache = []
_process_name_index = {}
_last_update = 0
CACHE_TIMEOUT = 1  # Update cache every 1 second

def get_process_list(search_text=""):
    global _process_cache, _process_name_index, _last_update
    current_time = time.time()
    
    # Return early for empty search
    search_text = search_text.lower().strip()
    if not search_text and _process_cache and current_time - _last_update <= CACHE_TIMEOUT:
        return _process_cache
    
    # Update cache if timeout exceeded
    if current_time - _last_update > CACHE_TIMEOUT:
        try:
            processes = [
                (p.info["pid"], p.info["name"], round(p.info["cpu_percent"] or 0.0, 2),
                 round(p.info["memory_percent"] or 0.0, 2))
                for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"])
            ]
            _process_cache = sorted(processes, key=lambda x: x[2], reverse=True)
            # Update name index for faster searching
            _process_name_index = {p[1].lower(): i for i, p in enumerate(_process_cache)}
            _last_update = current_time
        except Exception as e:
            print(f"Error updating process cache: {e}")
            if not _process_cache:  # If cache is empty, return empty list
                return []
    
    # Use indexed search for better performance
    if search_text:
        return [p for p in _process_cache if search_text in p[1].lower()]
    
    return _process_cache


def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        return True, f"Process {pid} terminated successfully."
    except psutil.NoSuchProcess:
        return False, f"Process {pid} does not exist."
    except psutil.AccessDenied:
        return False, f"Permission denied to terminate process {pid}."
    except Exception as e:
        return False, f"Failed to terminate process {pid}: {str(e)}"
