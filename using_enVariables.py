import os
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

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
    for device in devices:
        output = connect_and_execute(device, command)
        file.write(f"Output from {device['host']}:\n{output}\n\n")

print("Output written to output.txt")
