import subprocess
import time

def write_file(folder_path, comment_time, str_define, output):
        # Store the Prefixes in the file
        f = open(f"{folder_path}prefixes_v6.conf", "w")
        f.write(comment_time + str_define + " " + output.rstrip().decode("utf-8"))
        f.close()

def main():
	# Maintain separate lists for IPv4's and IPv6's
	# AS-SETs & ASNs List
	as_set = ['AS-VineethP','AS-213326-PEERS','AS-TaKeN']

	# bgpq4 flags
	flags = ['-6','-A','-b', '-R 48', '-l']

	# List name IPv6
	# Bird doesn't like '-' in names
	# v6_string = "_v6"
	# list_name = [as_set_name.replace('-','_') + v6_string for as_set_name in as_set]

	# We can combine multiple AS-SET's and ASN's in one command and bgpq4 gives us the combined list. So, let's choose a generic list name.
	list_name = 'Peers_v6'

	# 'define' keyword
	str_define = 'define'

	# 'folder' path
	folder_path = '/etc/bird/filtering/prefixes/'

	output = subprocess.check_output(['sudo', '/usr/local/bin/bgpq4', *flags, f'{list_name}', *as_set])

	# convert bytes to string
	# Strip the last carriage return using rstrip()
	# concatenate "define" word

	# print(str_define + " " + output.rstrip().decode("utf-8"))

	# Time
	seconds = time.time()
	str_time = time.ctime(seconds)
	comment_time = "# Updated: " + str_time + "\n\n";

	print(comment_time)

	write_file(folder_path, comment_time, str_define, output)

# Execution starts here
main()
