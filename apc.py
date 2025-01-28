#!/usr/bin/env python3

import click
import configparser
import os
from pathlib import Path

def get_aws_profiles():
    """Get list of available AWS profiles from credentials file."""
    credentials_path = os.path.expanduser("~/.aws/credentials")
    config = configparser.ConfigParser()
    
    if os.path.exists(credentials_path):
        config.read(credentials_path)
        # Remove 'default' from the list if it exists
        profiles = [p for p in config.sections() if p != 'default']
        return profiles
    return []

def set_active_profile(profile):
    """Set the active AWS profile in the AWS_PROFILE environment variable."""
    os.environ['AWS_PROFILE'] = profile
    # Also update the default profile in ~/.aws/credentials
    credentials_path = os.path.expanduser("~/.aws/credentials")
    config = configparser.ConfigParser()
    
    if os.path.exists(credentials_path):
        config.read(credentials_path)
        if profile in config.sections():
            # Get the credentials from the selected profile
            access_key = config[profile]['aws_access_key_id']
            secret_key = config[profile]['aws_secret_access_key']
            
            # Update the default profile
            if 'default' not in config.sections():
                config.add_section('default')
            config['default']['aws_access_key_id'] = access_key
            config['default']['aws_secret_access_key'] = secret_key
            
            # Write the changes back to the file
            with open(credentials_path, 'w') as configfile:
                config.write(configfile)
            return True
    return False

@click.command()
@click.argument('profile', required=False)
def cli(profile):
    """Simple CLI to switch between AWS profiles."""
    profiles = get_aws_profiles()
    
    if not profiles:
        click.echo("No AWS profiles found in ~/.aws/credentials")
        return
    
    if not profile:
        # If no profile is specified, show available profiles
        click.echo("Available AWS profiles:")
        for p in profiles:
            click.echo(f"  - {p}")
        return
    
    if profile not in profiles:
        click.echo(f"Profile '{profile}' not found. Available profiles:")
        for p in profiles:
            click.echo(f"  - {p}")
        return
    
    if set_active_profile(profile):
        click.echo(f"Switched to AWS profile: {profile}")
    else:
        click.echo(f"Failed to switch to profile: {profile}")

if __name__ == '__main__':
    cli()
