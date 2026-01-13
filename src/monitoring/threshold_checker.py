def check_thresholds(metrics, config):
    """
    Compare CPU, memory, and disk metrics against configured thresholds.

    Args:
        metrics (dict): Current metric values with keys 'cpu', 'memory', 'disk'.
        config (dict): Threshold configuration with keys 'cpu_threshold',
                       'memory_threshold', and 'disk_threshold'.

    Returns:
        dict: {
            'threshold_exceeded': bool,  # True if any threshold is exceeded
            'exceeded_resources': list  # List of resource names that exceeded
        }
    """
    exceeded_resources = []

    # Check CPU threshold
    if metrics.get('cpu', 0) > config.get('cpu_threshold', 100):
        exceeded_resources.append('cpu')

    # Check memory threshold
    if metrics.get('memory', 0) > config.get('memory_threshold', 100):
        exceeded_resources.append('memory')

    # Check disk threshold
    if metrics.get('disk', 0) > config.get('disk_threshold', 100):
        exceeded_resources.append('disk')

    return {
        'threshold_exceeded': bool(exceeded_resources),
        'exceeded_resources': exceeded_resources
    }
