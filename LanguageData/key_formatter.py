# arguments: [old file to format] [new file name]
import sys

f = open(sys.argv[1],'r')
n = open(sys.argv[2],'w')

line = f.readline()

already_seen = set()

while line != '':

    # check that we don't have duplicate lines
    if line in already_seen:
        print('Error: duplicate line:',line)
    else:
        already_seen.add(line)
        
    new_line = ''
    # replace any spaces with '_'
    for i in line:
        if i == ' ':
            new_line += '_'
        else:
            new_line += i
    # now write to the new file
    n.write(new_line)
    
    line = f.readline()

f.close()
n.close()
