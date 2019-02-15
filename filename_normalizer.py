import re 
import subprocess

suffix = ""
import sys
fileencoding = sys.getfilesystemencoding()
# print out all folders/files
folders = subprocess.check_output(["ls", "*/", "-d"], shell=True)
# decode into string format
folders = folders.decode(fileencoding)
# separate string into folder/file names
folders = folders.split("\n")[:-1]

# do not want anything with a "." in the name; will not work with 
# folders with a period in the name
folders = [folder for folder in folders if "." not in folder]


# matches contiguous integer sets
integer_matcher = re.compile(r'[0-9]+')
# finds the first contiguous integer grouping; None if none found
find_integer = lambda folder_name : integer_matcher.search(folder_name).group(0)

# assuming all "found" integers are between 0 and 100 (exclusive)
def find_integer_with_pad(folder_name):
	found_integer = find_integer(folder_name)
	if len(found_integer) > 1:
		return found_integer 
	return "0" + found_integer

folder_tuples = [(folder, find_integer_with_pad(folder)) for folder in folders]


for folder_name, folder_number in folder_tuples:
	# no reason to move folder to the same location/name or if no numbers
	if folder_name == folder_number + suffix or not folder_number:
		continue
	subprocess.call(["mv", folder_name, folder_number + suffix])



