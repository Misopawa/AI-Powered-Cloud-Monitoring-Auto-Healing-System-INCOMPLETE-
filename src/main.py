import time
import logging
from config_loader import load_config
from metrics_collector import collect_metrics
from csv_writer import save_metrics_to_csv
from threshold_monitor import check_thresholds
from anomaly_detector import detect_anomaly
from auto_healer import trigger_auto_heal
from logger import log_action

def main():
    # Load configuration from config.yaml
    config = load_config("config.yaml")
    interval = config.get("interval", 60)  # Default to 60 seconds if not specified

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    log_action("System started")

    while True:
        try:
            # Step 1: Collect system metrics
            metrics = collect_metrics()
            log_action("Metrics collected")

            # Step 2: Save metrics to CSV
            save_metrics_to_csv(metrics)
            log_action("Metrics saved to CSV")

            # Step 3: Perform threshold-based monitoring
            threshold_breach = check_thresholds(metrics, config)
            if threshold_breach:
                log_action(f"Threshold breach detected: {threshold_breach}")

            # Step 4: Perform AI-based anomaly detection
            anomaly = detect_anomaly(metrics)
            if anomaly:
                log_action(f"Anomaly detected: {anomaly}")

                # Step 5: Trigger auto-healing if anomaly is detected
                trigger_auto_heal(anomaly)
                log_action("Auto-healing triggered")

            # Sleep for the configured interval before next iteration
            time.sleep(interval)

        except Exception as e:
            log_action(f"Error in main loop: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    main()
