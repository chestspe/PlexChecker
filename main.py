import subprocess

# Define the path to the Plex Media Server executable
plex_path = "C:\\Program Files (x86)\\Plex\\Plex Media Server\\Plex Media Server.exe"

# Define the command to check the status of Plex Media Server
status_cmd = "tasklist /FI \"IMAGENAME eq Plex Media Server.exe\""

# Define the command to start Plex Media Server
start_cmd = "start \"\" \"" + plex_path + "\""

# Run the status command and capture the output
status_output = subprocess.check_output(status_cmd, shell=True)

# Check if the output contains the name of Plex Media Server
if b"Plex Media Server.exe" in status_output:
    # Plex Media Server is running, print a message
    print("Plex Media Server is running.")
else:
    # Plex Media Server is not running, print a message and try to start it
    print("Plex Media Server is not running.")
    print("Trying to start Plex Media Server...")
    # Run the start command and ignore the output
    subprocess.call(start_cmd, shell=True)
    # Print a message
    print("Plex Media Server should be starting now.")
