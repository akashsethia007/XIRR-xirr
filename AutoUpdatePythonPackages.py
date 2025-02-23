import subprocess
import sys

def get_outdated_packages():
    result = subprocess.check_output([sys.executable, '-m', 'pip', 'list', '--outdated'])
    lines = result.decode().split('\n')[2:]  # Skip the header lines
    outdated_packages = [line.split()[0] for line in lines if line ]
    return outdated_packages

def update_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

if __name__ == "__main__":
    outdated_packages = get_outdated_packages()
    if outdated_packages:
        update_packages(outdated_packages)
        print("Updated the following packages:", outdated_packages)
    else:
        print("All packages are up-to-date.")
