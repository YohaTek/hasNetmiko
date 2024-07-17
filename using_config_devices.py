import yaml
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# Load the configuration file
with open('devices.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Function to connect and execute commands
def connect_and_execute(device, command):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_command(command)
        connection.disconnect()
        return output
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return f"Failed to connect to {device['host']}: {str(e)}"

# Command to execute
command = 'show ip interface brief'

# Open a file to write the output
with open('output.txt', 'w') as file:
    for device in config['devices']:
        output = connect_and_execute(device, command)
        file.write(f"Output from {device['host']}:\n{output}\n\n")

print("Output written to output.txt")
