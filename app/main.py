import subprocess
import os

# Bandit will flag this — shell injection risk (B602)
def run_command(user_input):
    subprocess.call(user_input, shell=True)

# Bandit will flag this — hardcoded password (B105)
PASSWORD = "supersecret123"

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
