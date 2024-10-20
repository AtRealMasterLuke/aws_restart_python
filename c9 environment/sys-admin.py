# Import the os module:
import os
os.system("ls")
print("\n")# os.system() takes a string argument

'''Though os.system() is simple to use because it takes a string argument, it is recommended that you use the more powerful subprocess.run() function.
You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes.'''

# import the subprocess module:
import subprocess
print("SUBPROCESS MODULE")
subprocess.run(["ls","-l","README.md"]) # The third argument is the a directory name.

# Retrieving system information
command="uname" # uname command to get system information.
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
