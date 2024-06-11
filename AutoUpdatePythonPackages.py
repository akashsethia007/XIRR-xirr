import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]

for wrds in packages:
    print("New package being processed here ############################################ : ", wrds)
    print(wrds)
    try:
        call("pip install --upgrade " + ' ' + wrds, shell=True)
    except Exception as e:
        print("THIS IS THE ERROR HERE --------------------------------------------->" + str(e))
'''
call("pip install --upgrade " + ' '.join(packages), shell=True)
'''
print("Done")