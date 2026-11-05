import yaml
from netmiko import ConnectHandler

# Load the configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Define the device to connect to using the configuration file
device = {
    'device_type': 'cisco_ios',
    'host': config['device']['host'],
    'username': config['device']['username'],
    'password': config['device']['password'],
    'secret': config['device']['secret'],
}

# Establish an SSH connection to the device
connection = ConnectHandler(**device)

# Enter enable mode
connection.enable()

# Execute a command on the device
output = connection.send_command('show ip interface brief')

# Print the command output
print(output)

# Close the connection
connection.disconnect()
