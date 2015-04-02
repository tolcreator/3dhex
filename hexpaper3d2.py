from Tkinter import *
import math
import tkFont
import quick3d

"""
Given coords (top left corner of the rectangle containing the hex)
and size (between parallel faces) return the vertices of the hex.
"""
def getHex(size, coords):
    """
    Assuming coords = 0 at center.
    coords at top left = -1/r3, -0.5
    Size = 3
     0.5 /r3,  0.5
     1.0 /r3,  0
     0.5 /r3, -0.5
    -0.5 /r3, -0.5
    -1.0 /r3,  0
    -0.5 /r3,  0.5
    """
    r3 = math.sqrt(3)
    x, y = coords
    vert1 = [(x + size * 1.5 / r3) + 2, (y + size) + 2]
    vert2 = [(x + size * 2.0 / r3) + 2, (y + size * 0.5) + 2]
    vert3 = [(x + size * 1.5 / r3) + 2, y + 2]
    vert4 = [(x + size * 0.5 / r3) + 2, y + 2]
    vert5 = [x + 2, (y + size * 0.5) + 2]
    vert6 = [(x + size * 0.5 / r3) + 2, (y + size) + 2]
    return [vert1, vert2, vert3, vert4, vert5, vert6]

def getQuaterHexWidth(size):
    r3 = math.sqrt(3)
    width = size * 2 / r3
    return width / 4

"""
Gets the system offsets within the rectangle bounding the hex
"""
def getSystemOffset(size, coords):
    r3 = math.sqrt(3)
    z = coords[2]
    x = size / r3
    print coords
    if z == 1 or z == 2:
        y = size / 6
    elif z == 3 or z == 4:
        y = size / 3
    elif z == 5 or z == 6:
        y = size * 2 / 3
    else:
        y = size * 5 / 6
    return [x, y]
        

"""
Get the canvas size required to draw the given hexmap
for a hexmap of x * y hexes of parrallel face size n, that is:
Height of (2y + 1) n /2
Width of (3x + 1) n / 2 * r3
"""
def getBoundingSize(hexsize, size):
    return [(((3 * size[0]) + 1) * hexsize / (2 * math.sqrt(3))) + 3, (((2 * size[1]) + 1) * hexsize * 0.5) + 3]

"""
Get the coordinates (of top left of bounding rectangle) of 
the given hex
for coords x, y and size n,
y = y * n (if x is even), or (2y + 1) * n/2 (if x is odd)
x = 3x * n / 2 * r3
"""
def getHexCoordinates(hexsize, coords):
    if coords[0] % 2 == 0:
        return [(coords[0] * 3 * hexsize / (2 * math.sqrt(3))) + 2, (coords[1] * hexsize) + 2]
    else:
        return [(coords[0] * 3 * hexsize /  (2 * math.sqrt(3))) + 2, (((coords[1] * 2) + 1) * hexsize * 0.5) + 2]

def getHexCoordinatesOddZ(hexsize, coords):
    if coords[0] % 2 == 0:
        return [(coords[0] * 3 * hexsize / (2 * math.sqrt(3))) + 2, (coords[1] * hexsize) + 2]
    else:
        return [(coords[0] * 3 * hexsize /  (2 * math.sqrt(3))) + 2, (((coords[1] * 2) + 1) * hexsize * 0.5) + 2]

def getHexCoordinatesEvenZ(hexsize, coords):
    if coords[0] % 2 == 0:
        return [(coords[0] * 3 * hexsize /  (2 * math.sqrt(3))) + 2 + getQuaterHexWidth(hexsize), (((coords[1] * 2) + 1) * hexsize * 0.5) + 2]
    else:
        return [(coords[0] * 3 * hexsize / (2 * math.sqrt(3))) + 2 + getQuaterHexWidth(hexsize), (coords[1] * hexsize) + 2]


def getHexnumberCoordinates(hexsize, coords):
    base = getHexCoordinates(hexsize, coords)
    base[1] += 2
    base[0] += (2 * hexsize / (2 * math.sqrt(3))) + 1
    return base

def getCoordsFromSystem(hexsize, system):
    x, y, z = system
    x -= 1
    y -= 1
    z -= 1
    if quick3d.odd(z):
        coords = getHexCoordinatesEvenZ(hexsize, [x, y])
    else:
        coords = getHexCoordinatesOddZ(hexsize, [x, y])
    offset = getSystemOffset(hexsize, system)
    systemCoords = [offset[0] + coords[0], offset[1] + coords[1]]
    return systemCoords


class Paper:
    def __init__(self, master, filename, hexsize = 96, size = [8, 8]):
        hexNumberFont = tkFont.Font(family="Arial", size=10)
        canvasSize = getBoundingSize(hexsize, size)
        bg = Canvas(master, bg="white", width = canvasSize[0] + getQuaterHexWidth(hexsize), height = canvasSize[1])

        evenz_hexes = []
        for x in range(size[0]):
            column = []
            for y in range(size[1]):
                coords = getHexCoordinatesEvenZ(hexsize, [x, y])
                verts = getHex(hexsize, coords)
                entry = bg.create_polygon(verts, fill="", outline="gray")
                column.append(entry)
                for z in [2, 4, 6, 8]:
                    system = [x, y, z]
                    offset = getSystemOffset(hexsize, system)
                    systemCoords = [offset[0] + coords[0], offset[1] + coords[1]]
                    dot = bg.create_oval(systemCoords[0]-1, systemCoords[1]-1, systemCoords[0]+1, systemCoords[1]+1, fill="gray", outline="gray")
                    evenz_hexes.append(column)
                    bg.pack()
        oddz_hexes = []
        for x in range(size[0]):
            column = []
            for y in range(size[1]):
                coords = getHexCoordinatesOddZ(hexsize, [x, y])
                verts = getHex(hexsize, coords)
                entry = bg.create_polygon(verts, fill="", outline="black")
                column.append(entry)
                for z in [1, 3, 5, 7]:
                    systemCoords = getCoordsFromSystem(hexsize, [x+1, y+1, z])
                    dot = bg.create_oval(systemCoords[0]-1, systemCoords[1]-1, systemCoords[0]+1, systemCoords[1]+1, fill="black", outline="black")
                    oddz_hexes.append(column)
                    bg.pack()
        subsec = quick3d.Quick3d()
        if filename:
            subsec.open(filename)
        else:
            subsec.generate()
        
        jump1 = subsec.getOnlyJump(1)
        jump2 = subsec.getOnlyJump(2)

        for jump in jump1:
            source = jump["Source"]
            destination = jump["Destination"]
            sourceCoords = getCoordsFromSystem(hexsize, source.getCoordinates())
            destCoords = getCoordsFromSystem(hexsize, destination.getCoordinates())
            line = bg.create_line(sourceCoords[0], sourceCoords[1], destCoords[0], destCoords[1], fill="dark green", width=3)

        for jump in jump2:
            source = jump["Source"]
            destination = jump["Destination"]
            sourceCoords = getCoordsFromSystem(hexsize, source.getCoordinates())
            destCoords = getCoordsFromSystem(hexsize, destination.getCoordinates())
            line = bg.create_line(sourceCoords[0], sourceCoords[1], destCoords[0], destCoords[1], fill="green", width=1)


        systems = subsec.getSystems()
        hexNumberFont = tkFont.Font(family="Arial", size=10)
        for system in systems:
            print system
            x, y, z = system.getCoordinates()
            coords = getCoordsFromSystem(hexsize, system.getCoordinates())
            circle = bg.create_oval(coords[0]-4, coords[1]-4, coords[0]+4, coords[1]+4, fill="", outline="blue")
            text = bg.create_text([coords[0], coords[1] + 4], text="%02d%02d%02d" % (x, y, z), fill="blue", anchor=N, font=hexNumberFont)
        bg.pack()
        bg.update()
        bg.postscript(file="output.ps", colormode='color')
        

        
top = Tk()
paper = Paper(top, filename="")
top.mainloop()
