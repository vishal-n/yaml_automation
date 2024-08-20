import yaml
import subprocess
from datetime import datetime


def run_command(command):
    """Execute a shell command and log the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr


def log_message(message):
    """Log messages to a file."""
    with open('logs/service_logs.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def automate_services(services):
    for service in services['services']:
        log_message(f"Processing service: {service['name']}")

        if service['type'] == 'cron':
            # Handle cron jobs (scheduling not implemented in this example)
            log_message(f"Scheduled job: {service['schedule']} {service['command']}")

        elif service['type'] == 'system':
            stdout, stderr = run_command(service['command'])
            if stdout:
                log_message(f"Output: {stdout.decode()}")
            if stderr:
                log_message(f"Error: {stderr.decode()}")


# Load and automate services
with open('services.yaml', 'r') as file:
    services_config = yaml.safe_load(file)

automate_services(services_config)
