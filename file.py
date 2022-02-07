#counting line in a file
'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('line count:', count)
'''
#reading the *whole* file
'''
fhand = open ('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
'''
#searching through a file
'''
fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From :'):
        print(line)

#skipping with continue
fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From :'):
        continue
        print(line)
        '''
#Prompt for file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
