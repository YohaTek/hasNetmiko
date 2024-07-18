import yaml
import logging
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# Configure logging
logging.basicConfig(filename='netmiko_log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Load the configuration file
with open('devices.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Commands to execute
commands = ['show ip interface brief', 'show version']

# Function to connect and execute commands
def connect_and_execute(device, commands):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        results = {}
        for command in commands:
            results[command] = connection.send_command(command)
        connection.disconnect()
        return results
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        logging.error(f"Failed to connect to {device['host']}: {str(e)}")
        return None

# Execute commands on each device and log the output
for device in config['devices']:
    output = connect_and_execute(device, commands)
    if output:
        filename = f"{device['host']}_output.txt"
        with open(filename, 'w') as file:
            for command, result in output.items():
                file.write(f"Output of '{command}' on {device['host']}:\n{result}\n\n")
        logging.info(f"Output written to {filename}")

print("Script execution complete. Check netmiko_log.log for details.")
