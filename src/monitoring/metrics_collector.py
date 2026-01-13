import psutil

def collect_metrics():
    """
    Collect system metrics using psutil.
    Returns a dictionary with CPU, memory, and disk usage percentages.
    """
    # CPU usage percentage over an interval of 1 second
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Memory usage percentage (used memory / total memory * 100)
    memory_usage = psutil.virtual_memory().percent
    
    # Disk usage percentage for the root partition
    disk_usage = psutil.disk_usage('/').percent
    
    return {
        'cpu_usage_percent': cpu_usage,
        'memory_usage_percent': memory_usage,
        'disk_usage_percent': disk_usage
    }
