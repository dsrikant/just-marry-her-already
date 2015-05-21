from sys import argv
print ''.join([chr(int(elm)+65) if elm.isdigit() else elm for elm in argv[1]])

