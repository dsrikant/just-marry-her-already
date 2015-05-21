from sys import argv
print ''.join([chr(int(elm)+97) if elm.isdigit() else elm for elm in argv[1]])

