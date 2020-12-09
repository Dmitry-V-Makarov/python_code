# Matching and extracting data
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

# Greedy matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# Non-greedy matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# Extracting an email address
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

# Matching differs from extraction
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)

# The double split pattern - extracting host
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# Extracting host with regex
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', x)
print(y)

# Spam confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1  : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# Extracting all the numbers and summing them up
import re
hand = open('regex_sum_323360.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1  : continue #skipping an empty line
    numbers = [int(i) for i in numbers] #converting to a list of integers
    numlist = numlist + numbers #concatinating lists
print(sum(numlist))

#A different way 1 for the same problem
import re
hand = open('regex_sum_323360.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    numbers = [int(i) for i in re.findall('[0-9]+', line)]
    numlist = numlist + numbers
print(sum(numlist))

# A different way 2 for the same problem
print(sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_323360.txt').read()) ] ) )

# Search for lines that start with From and have an at sign
import re
hand = open('mbox.txt')
search = input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(search, line): count = count + 1

print('mbox.txt had', count, 'lines that matched', search)

# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Search for lines that have an at sign between characters
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
# The results will be slightly more accurate than re07.py for email addresses
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that start 'X' followed by any non whitespace
# characters and ':' then output the first group of non whitespace
# characters that follows
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)

# Search for lines that contain 'Author:' followed by any characters,
# an at sign, and any non whitespace character
# Then print the character group that follows the at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)

# Search for lines that contain 'New Revision: ' followed by a number
# Then turn the number into a float and append it to nums
# Finally print the length and the average of nums
import re
fname = input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(int(sum(nums)/len(nums)))
