## Creating a sorted list with unique words

# Open and read the file
fname = input("Enter file name: ")
fh = open(fname)

# Create a list of all the words (including repeated)
lst = list()
for line in fh :
    line = line.rstrip()
    line = line.split()
    lst = line + lst

# Create a list with unique words

newlst = list()
newword = None
for word in lst:
    if newword is None :
        newword = word
    if word in newlst : continue
    newlst.append(word)

# Sort
newlst.sort()
print(newlst)


## Counting with a dictionary - Histogram problem (long way)
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

## Counting with a dictionary (short way)
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print counts

## Counting pattern for a list
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

## Counting pattern for a text
counts = dict()
fname = input("Enter file name: ")
fh = open(fname)

words = list()
for line in fh :
    line = line.rstrip()
    line = line.split()
    words = line + words

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

## Two iteration variables
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for k,v in counts.items () :
    print(k, v)

## Most frequent words counting application
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

## What the most common email address is

name = input('Enter file: ')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From:' : continue
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


## Sorted dictionary

# Sorted by key
print('Sorted by key:')
d = {'a':10, 'c':22, 'b':1}
print(d)
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)

# Sorted by value
print('Sorted by value')
c = {'a':10, 'b':1, 'c':22}
print(c)
tmp = list()
for k,v in c.items() :
    tmp.append( (v,k) )
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

## The top 10 most common words
name = input('Enter file: ')
if len(name) < 1 : name = 'romeo.txt'
fhand = open(name)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

## The top 10 most common words (less code)
name = input('Enter file: ')
if len(name) < 1 : name = 'romeo.txt'
fhand = open(name)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = sorted( [ (val,key) for key,val in counts.items() ], reverse=True )

for val, key in lst[:10] :
    print(key, val)


## count letters in a word
fhand = 'aaa bba'

counts = dict()
for letter in fhand:
    # ab is list of letters
    ab = letter.split()
    for item in ab:
        counts[item] = counts.get(item, 0) + 1
print(counts)

## Read a file, extract hour, make a histogram, sort and print
name = input('Enter file: ')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From' : continue
    time = words[5]
    hms = time.split(':')
    hour = hms[0]
    counts[hour] = counts.get(hour, 0) + 1

for k,v in sorted(counts.items()):
    print(k,v)