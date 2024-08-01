import schedule
import time
import subprocess

def run_php_script():
    # Command to run your PHP script
    command = ["php", "C:/Users/mate2/OneDrive/Escritorio/FreeLancing/EEmperor/OCI/ScriptSolutionHostCapacity/oci-arm-host-capacity/index.php"]
    subprocess.run(command)

# Schedule the task to run every 5 minutes
schedule.every(30).seconds.do(run_php_script)

while True:
    schedule.run_pending()
    time.sleep(1)      
