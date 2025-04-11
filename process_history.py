import time
from datetime import datetime

# Store process history data
_process_history = []

def add_process_snapshot(processes):
    """
    Add a snapshot of current processes to history
    
    Args:
        processes: List of process tuples (pid, name, cpu%, memory%)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    snapshot = {
        'timestamp': timestamp,
        'processes': processes
    }
    _process_history.append(snapshot)
    
    # Keep only last 24 hours of data (assuming 2-second intervals)
    max_snapshots = 43200  # 24 hours * 60 minutes * 60 seconds / 2 seconds
    if len(_process_history) > max_snapshots:
        _process_history.pop(0)

def get_process_history():
    """Get the complete process history"""
    return _process_history