import os
import logging
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# Configure logging
logging.basicConfig(filename='netmiko_log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Define the devices
devices = [
    {
        'device_type': 'cisco_ios',
        'host': os.getenv('DEVICE1_HOST'),
        'username': os.getenv('DEVICE1_USERNAME'),
        'password': os.getenv('DEVICE1_PASSWORD'),
        'secret': os.getenv('DEVICE1_SECRET'),
    },
    {
        'device_type': 'cisco_ios',
        'host': os.getenv('DEVICE2_HOST'),
        'username': os.getenv('DEVICE2_USERNAME'),
        'password': os.getenv('DEVICE2_PASSWORD'),
        'secret': os.getenv('DEVICE2_SECRET'),
    },
    {
        'device_type': 'cisco_ios',
        'host': os.getenv('DEVICE3_HOST'),
        'username': os.getenv('DEVICE3_USERNAME'),
        'password': os.getenv('DEVICE3_PASSWORD'),
        'secret': os.getenv('DEVICE3_SECRET'),
    },
]

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
for device in devices:
    output = connect_and_execute(device, commands)
    if output:
        filename = f"{device['host']}_output.txt"
        with open(filename, 'w') as file:
            for command, result in output.items():
                file.write(f"Output of '{command}' on {device['host']}:\n{result}\n\n")
        logging.info(f"Output written to {filename}")

print("Script execution complete. Check netmiko_log.log for details.")
