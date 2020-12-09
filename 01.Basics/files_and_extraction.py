## Extracting an email

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh :
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement (len(words) < 3 has to come first)
    if len(words) < 3 or words[0] != 'From' : continue
    email = words[1]
    count = count + 1
    print(email)

print("There were", count, "lines in the file with From as the first word")



fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])




fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)




fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) > 0:
        if words[0] != 'From':
            continue
        print(words[2])




fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) > 0:
        if words[0] != 'From':
            continue
        print(words[2])




fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])




fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)