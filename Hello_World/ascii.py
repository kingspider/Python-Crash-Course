import sys
import math
import re

line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
count = 1
Abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']
charmap = {}
line = ''


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def build_carmap(ln1, ln2, ln3, ln4, ln5, ab):
    for character in ab:
        charmap[character] = [ln1[Abc.index(character)], ln2[Abc.index(character)], ln3[Abc.index(character)],
                              ln4[Abc.index(character)], ln5[Abc.index(character)]]


''' 
    for line in range(5):
        if line == 0:
            for character in ab:
                charmap[character] = ln1[Abc.index(character)]

        if line == 1:
            for character in ab:
                charmap[character] = ln2[Abc.index(character)]

        if line == 2:
            for character in ab:
                charmap[character] = ln3[Abc.index(character)]

        if line == 3:
            for character in ab:
                charmap[character] = ln4[Abc.index(character)]

        if line == 4:
            for character in ab:
                charmap[character] = ln5[Abc.index(character)]
'''

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    row = re.findall('....', row)
    # print('Debug(line 22): Row:' + str(row), file=sys.stderr)
    if count == 1:
        line1 = row
        count = count + 1
    elif count == 2:
        line2 = row
        count = count + 1
    elif count == 3:
        line3 = row
        count = count + 1
    elif count == 4:
        line4 = row
        count = count + 1
    else:
        line5 = row
        count = 0

# print('Debug(line 60): line1' + str(line1), file=sys.stderr)
build_carmap(line1, line2, line3, line4, line5, Abc)

'''
print('Debug(line 63): charmap A:' + str(charmap['A']), file=sys.stderr)
print('Debug(line 64): Charmap build test: line1: ' + str(charmap['A'][0]), file=sys.stderr)
print('Debug(line 65): Charmap build test: line2: ' + str(charmap['A'][1]), file=sys.stderr)
print('Debug(line 66): Charmap build test: line3: ' + str(charmap['A'][2]), file=sys.stderr)
print('Debug(line 67): Charmap build test: line4: ' + str(charmap['A'][3]), file=sys.stderr)
print('Debug(line 68): Charmap build test: line5: ' + str(charmap['A'][4]), file=sys.stderr)
'''

for line in range(h):
    print('Debug(line 78): line: ' + str(line), file=sys.stderr)
    for char in t:
        print('Debug(line 80): char: ' + str(char), file=sys.stderr)
        line = line + str(charmap[char][line])
    print('Debug(line 82): line: ' + line, file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # Debug block

dic = {'A':[1,2,3]}
dic['A'].append(list)