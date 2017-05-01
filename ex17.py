from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "Ready to copy, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(indata)