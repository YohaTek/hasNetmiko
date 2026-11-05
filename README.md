# hasNetmiko

Educational examples of network automation with
[Netmiko](https://github.com/ktbyers/netmiko), a Python library that simplifies
SSH management of network devices.

The repository walks from a single-device connection to multi-device runs that
read credentials from a YAML file or from environment variables, with optional
logging. All examples target Cisco IOS devices and can be adapted to any
platform Netmiko supports by changing `device_type`.

## Scripts

| Script | Credentials from | What it does |
| --- | --- | --- |
| `connect_single_device.py` | `config.yaml` | Connects to one device, runs `show ip interface brief`, and prints the result. |
| `multi_device_from_yaml.py` | `devices.yaml` | Connects to every device in the file and writes all output to `output.txt`. |
| `multi_device_from_yaml_with_logging.py` | `devices.yaml` | Runs two commands per device, writes one `<host>_output.txt` file per device, and logs to `netmiko_log.log`. |
| `multi_device_from_env_vars.py` | `DEVICEn_*` environment variables | Same as `multi_device_from_yaml.py`, with three devices defined from environment variables. |
| `multi_device_from_env_vars_with_logging.py` | `DEVICEn_*` environment variables | Same as `multi_device_from_yaml_with_logging.py`, with devices defined from environment variables. |

## Requirements

- Python 3.9 or newer
- Network access and SSH credentials for the devices you want to manage
- [Netmiko](https://pypi.org/project/netmiko/) and [PyYAML](https://pypi.org/project/PyYAML/), installed with:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Never commit real credentials. `config.yaml`, `devices.yaml`, `devices_2.yaml`,
and `.env` are git-ignored for that reason. Start from the example templates:

```sh
cp config.example.yaml config.yaml
cp devices.example.yaml devices.yaml
```

Then edit the copies and replace the placeholder credentials. `config.yaml`
describes a single device; `devices.yaml` holds a `devices` list.

The environment-variable examples expect three devices named `DEVICE1` to
`DEVICE3`:

```sh
export DEVICE1_HOST='192.0.2.11'
export DEVICE1_USERNAME='admin'
export DEVICE1_PASSWORD='change-me'
export DEVICE1_SECRET='change-me'

# ... repeat for DEVICE2_* and DEVICE3_*
```

## Running

```sh
python connect_single_device.py
python multi_device_from_yaml.py
python multi_device_from_yaml_with_logging.py
python multi_device_from_env_vars.py
python multi_device_from_env_vars_with_logging.py
```

The scripts must be run from the repository root (or wherever the YAML files
live), because they open `config.yaml` and `devices.yaml` by relative path.

## Generated files

Command output and logs are written next to the scripts and are ignored by Git:

- `output.txt` (all devices, from the non-logging examples)
- `<host>_output.txt` (one file per device, from the logging examples)
- `netmiko_log.log`

## Security notes

- Use dedicated, least-privilege accounts rather than shared admin credentials.
- The examples call `connection.enable()`, so the account needs an enable
  secret; set `secret` in the YAML file or `DEVICEn_SECRET` accordingly.
- The IP addresses in the templates come from the documentation range
  (`192.0.2.0/24`); replace them with your own lab or device addresses.
- Treat a leaked credential as compromised: rotate it and remove it from the
  working tree before committing.

## Limitations

These scripts connect to real or lab devices, so there is no test harness and
nothing is executed in CI. The environment-variable examples hardcode three
devices; extend the list if you need more.
