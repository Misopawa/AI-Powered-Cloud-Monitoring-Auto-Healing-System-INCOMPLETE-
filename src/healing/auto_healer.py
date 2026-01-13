import subprocess
import logging

def restart_service(service_name):
    """
    Restart a Linux systemd service via systemctl.
    No service names are hard-coded; caller must supply a valid name.

    Safety note: automatic restarts can mask underlying issues and
    should be rate-limited and combined with proper alerting.
    """
    try:
        subprocess.run(
            ["systemctl", "restart", service_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return True
    except subprocess.CalledProcessError as exc:
        # Log failure details for later investigation
        logging.error("Failed to restart %s: %s", service_name, exc.stderr.strip())
        return False


def log_healing_action(action, logger=None):
    """
    Record an automatic healing action.

    Parameters
    ----------
    action : str
        Human-readable description of the healing step taken.
    logger : logging.Logger, optional
        Logger instance to use.  If omitted, the root logger is used.
    """
    if logger is None:
        logger = logging.getLogger()
    logger.warning("AUTO-HEAL: %s", action)
