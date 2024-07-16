from netmiko import ConnectHandler

# Define the device to connect to
# and replace every value in the device dictionary, according to your system.

device = {
    'device_type': 'cisco_ios',  
    'host': '192.168.1.1',       
    'username': 'Yohan', 
    'password': '1234', 
    'port': 22,                  
    'secret': 'your_secret',     
    'verbose': True              
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
