import subprocess
import time

while True:
    # define the path to the Python script you want to run
    script_path = 'shell.py'

    # start a new Python process and execute the script
    subprocess.run(['python3', script_path, 'RUN("example.txt")'])

    time.sleep(60)