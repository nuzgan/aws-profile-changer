# AWS Profile Changer (apc)

A simple command-line tool to easily switch between AWS profiles.

## Description

This tool helps you manage multiple AWS profiles by:
- Listing all available AWS profiles
- Switching between profiles by updating both the environment variable and the default profile in credentials

## Prerequisites

- Python 3.x
- AWS credentials configured in `~/.aws/credentials`

## Installation

1. Install the required package:

```bash
pip install click
```

2. Save the script as `apc.py`

3. Make it executable:

```bash
chmod +x apc.py
```

4. (Optional) Create an alias in your shell configuration file (`.bashrc` or `.zshrc`):

```bash
alias apc='python /path/to/apc.py'
```

## Usage

List all available profiles:

```bash
./apc.py
```

Switch to a specific profile:

```bash
./apc.py myprofile
```

If you set up the alias, you can use:

```bash
apc # List profiles
apc myprofile # Switch to a specific profile
```

## AWS Credentials File Format

The script expects your AWS credentials to be stored in `~/.aws/credentials` with the following format:

```ini
[default]
aws_access_key_id = YOUR_DEFAULT_ACCESS_KEY
aws_secret_access_key = YOUR_DEFAULT_SECRET_KEY

[profile1]
aws_access_key_id = YOUR_PROFILE1_ACCESS_KEY
aws_secret_access_key = YOUR_PROFILE1_SECRET_KEY

[profile2]
aws_access_key_id = YOUR_PROFILE2_ACCESS_KEY
aws_secret_access_key = YOUR_PROFILE2_SECRET_KEY
```

## Note

When switching profiles, the tool will overwrite the `default` profile in your credentials file with the selected profile's credentials.