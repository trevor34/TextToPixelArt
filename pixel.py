import turtle
import tkinter as tk
import argparse
import re

parser = argparse.ArgumentParser(description='Make pixel art from a file')
parser.add_argument('file', help='File to make pixel art from')
parser.add_argument('--colors', '-c', help='Show colors', action='store_true')


args = parser.parse_args()


colorfile = open(args.file, 'r').read().split('\n')

if colorfile[-1] == '':
    del colorfile[-1]

for i in range(len(colorfile)):
    colorfile[i] = colorfile[i].split(' ')

colordata = {}
# Defaults
size = 20
x = -300
y = 300
mirror = False
auto = False
turtBG = '#fff'
for i in range(len(colorfile[0])):
    colorfile[0][i] = colorfile[0][i].split(':')
    if colorfile[0][i][0] == 'size': size = int(colorfile[0][i][1])
    elif colorfile[0][i][0] == 'x': x = int(colorfile[0][i][1])
    elif colorfile[0][i][0] == 'y': y = int(colorfile[0][i][1])
    elif colorfile[0][i][0] == 'bg': turtBG = colorfile[0][i][1]
    elif colorfile[0][i][0] == 'mirror': mirror = True
    elif colorfile[0][i][0] == 'auto': auto = True
    else:
        colordata[colorfile[0][i][0]] = colorfile[0][i][1] # for color variable assignments

del colorfile[0]

# Turtle settings
tk.ROUND = tk.BUTT # Sets brush end shape to square
turt = turtle.Turtle()
turt._tracer(0, 0) # Sets so it does not take time to trace. Puts picture imediately

turtle.Screen().bgcolor(turtBG)

turt.speed(0)
turt.pensize(size)

turt.ht()
turt.penup()

if args.colors:
    turt.goto(x, y)
    turt.pendown()
    for i in colordata:
        turt.color(i)
        turt.forward(size)
    turt.penup()

if mirror:
    for i in range(len(colorfile)):
        for p in range(len(colorfile[i]), 0, -1):
            if not re.match(r"r[0-9]+", colorfile[i][p - 1]) and colorfile[i] != ['']:
                colorfile[i].append(colorfile[i][p - 1])


clist = [] # colorlist
iterative = 0 # Iterative allows the clist to desync with `i` when a Repeater is put in
for i in range(len(colorfile)):
    clist.append([])

    for p in range(len(colorfile[i])):
        
        if re.match(r"r[0-9]+", colorfile[i][p]): # Repeat for iteration
                colorfile[i][p] = colorfile[i][p].replace('r', '')
                clist.pop() # Removes last appended clist object so that there is not a blank space
                for q in range(int(colorfile[i][p])):
                    clist.append(clist[i - 1 + iterative])

                iterative += int(colorfile[i][p]) - 1

        elif re.match(r"[0-9]+,TP", colorfile[i][p]): # Transparent Pixel handling.
            colorfile[i][p] = colorfile[i][p].split(',')
            length = int(colorfile[i][p][0])

            for q in range(length):
                clist[i + iterative].append('TP')

        else:
            colorfile[i][p] = colorfile[i][p].split(',')
            
            try:
                color = colordata[colorfile[i][p][1]]
            except KeyError:
                print("[!] Error : Key '" + colorfile[i][p][1] + "' is an invalid color value.")
                exit()
            
            length = int(colorfile[i][p][0])

            for q in range(length):
                clist[i + iterative].append(color)

if auto:
    x = 0
    y = len(clist) / 2 * size
    
    # This section determines the size of the longest clist string
    for i in range(len(clist)): 
        colorCompare = -1 * len(clist[i]) / 2 * size
        if colorCompare < x:
            x = colorCompare

# Drawing part
for i in range(len(clist)):

    turt.goto(x, y)
    y -= size
    turt.pendown()
    for e in clist[i]:
        if e == 'TP': # For transparent inputs
            turt.penup()
        else:
            turt.color(e)
        
        turt.forward(size)
        turt.pendown()
    turt.penup()


turtle.done()
