import sys
from subprocess import call,run
import subprocess
def check(name):
    latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(name)], capture_output=True, text=True))
    latest_version = latest_version[latest_version.find('(from versions:')+15:]
    latest_version = latest_version[:latest_version.find(')')]
    latest_version = latest_version.replace(' ','').split(',')[-1]
    return latest_version

all_pkgs = subprocess.run(["pip", "freeze", "/dev/null"], capture_output=True).stdout.splitlines()
for pkg in all_pkgs:
    pk_name = str(pkg).replace('b\'','').replace('\'','').split("==")
    ver = check(pk_name[0])
    try:
        if ver != pk_name[1]:
            try:
                print(f"{pk_name[0]} needs to be updated as installed is {ver} and latest version is {pk_name[1]}")
                call("pip install --upgrade " + ' ' + pk_name[0], shell=True)
            except Exception as e:
                print("ERROR: While installing the upgraded package got and error as ::" + str(e))
    except Exception as e:
        print(f"ERROR: {str(e)}")
print("INFO: All packages updated")