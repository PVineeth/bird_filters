import subprocess
import time

# AS-SET List
as_set = ['AS-213326-PEERS']

# bgpq4 flags
flags = ['-6','-A','-b', '-R 48', '-l']

# List name
# Bird doesn't like '-' in names
list_name = [as_set_name.replace('-','_') for as_set_name in as_set]

# 'define' keyword
str_define = 'define'

# 'folder' path
folder_path = '/etc/bird/filtering/prefixes/'

# Using the as_set name also for the list name
output = subprocess.check_output(['sudo', '/usr/local/bin/bgpq4', f'{flags[0]}', f'{flags[1]}', f'{flags[2]}', f'{flags[3]}', f'{flags[4]}', f'{list_name[0]}', f'{as_set[0]}'])

# convert bytes to string
# Strip the last carriage return using rstrip()
# concatenate "define" word

# print(str_define + " " + output.rstrip().decode("utf-8"))

# Time
seconds = time.time()
str_time = time.ctime(seconds)
comment_time = "# Updated: " + str_time + "\n\n";

print(comment_time)

# Store the Prefixes in the file
f = open(f"{folder_path}prefixes.conf", "w")
f.write(comment_time + str_define + " " + output.rstrip().decode("utf-8"))
f.close()
