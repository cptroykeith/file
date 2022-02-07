#counting line in a file
'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('line count:', count)
'''
#reading the *whole* file
fhand = open ('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

