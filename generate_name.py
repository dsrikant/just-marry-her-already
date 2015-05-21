from sys import argv

print 'Naive linear conversion: ' + ''.join([chr(int(elm)+97) if elm.isdigit() else elm for elm in argv[1]])


# encode
new_name = ''
bounds = 103 + 20
cycle_counter = 103
for elm in argv[1]:
    if elm.isdigit():
        cycle_counter = ((cycle_counter + int(elm)) % bounds) 
        if cycle_counter < 103: cycle_counter += 103
        new_name += chr(int(cycle_counter))
    else:
        new_name += elm

print 'Full range conversion: ' + new_name

# reverse attempt here.
old_cipher = ''
cycle_counter = 103
for elm in new_name:
    if ord(elm) >= 103:
        pass

print 'Full range converstion reversal: ' + old_cipher


