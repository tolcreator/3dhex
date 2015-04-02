import dice

oneJumpMatrixOddZOddX = [
    # Z - 1: Plane above
    [-1, 0, -1],
    [0,-1, -1],
    [0, 0, -1],
    # Z + 0: Same plane
    [-1, -1, 0],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [1, -1, 0],
    [1, 0, 0],
    # Z + 1: Plane below
    [-1, 0, 1],
    [0, -1, 1],
    [0, 0, 1]
]

oneJumpMatrixOddZEvenX = [
    # Z - 1: Plane above
    [-1, 0, -1],
    [0, 0, -1],
    [0, 1, -1],
    # Z + 0: Same plane
    [-1, 0, 0],
    [-1, 1, 0],
    [0, -1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    # Z + 1: Plane below
    [-1, 0, 1],
    [0, 0, 1],
    [0, 1, 1]
]

oneJumpMatrixEvenZOddX = [
    # Z - 1: Plane above
    [0, 0, -1],
    [0, 1, -1],
    [1, 0, -1],
    # Z + 0: Same plane
    [-1, 0, 0],
    [-1, 1, 0],
    [0, -1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    # Z + 1: Plane below
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1]
]

oneJumpMatrixEvenZEvenX = [
    # Z - 1: Plane above
    [0, -1, -1],
    [0, 0, -1],
    [1, 0, -1],
    # Z + 0: Same plane
    [-1, -1, 0],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [1, -1, 0],
    [1, 0, 0],
    # Z + 1: Plane below
    [0, -1, 1],
    [0, 0, 1],
    [1, 0, 1]
]

twoJumpMatrixOddZOddX = [
    # Z - 2: 2 Planes above
    [-1, -1, -2],
    [-1, 0, -2],
    [0, -1, -2],
    [0, 0, -2],
    [0, 1, -2],
    [1, -1, -2],
    [1, 0, -2],
    # Z - 1: 1 Plane above
    [-2, -1, -1],
    [-2, 0, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [0, -2, -1],
    [0, 1, -1],
    [1, -1, -1],
    [1, 0, -1],
    [1, 1, -1],
    # Z + 0: Same plane
    [-2, -1, 0],
    [-2, 0, 0],
    [-2, 1, 0],
    [-1, -2, 0],
    [-1, 1, 0],
    [0, -2, 0],
    [0, 2, 0],
    [1, -2, 0],
    [1, 1, 0],
    [2, -1, 0],
    [2, 0, 0],
    [2, 1, 0],
    # Z + 1: 1 Plane below
    [-2, -1, 1],
    [-2, 0, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [0, -2, 1],
    [0, 1, 1],
    [1, -1, 1],
    [1, 0, 1],
    [1, 1, 1],
    # Z + 2: 2 Planes below
    [-1, -1, 2],
    [-1, 0, 2],
    [0, -1, 2],
    [0, 0, 2],
    [0, 1, 2],
    [1, -1, 2],
    [1, 0, 2],
]

twoJumpMatrixOddZEvenX = [
    # Z - 2: 2 Planes above
    [-1, 0, -2],
    [-1, 1, -2],
    [0, -1, -2],
    [0, 0, -2],
    [0, 1, -2],
    [1, 0, -2],
    [1, 1, -2],
    # Z - 1: 1 Plane above
    [-2, -1, -1],
    [-2, 0, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [0, -2, -1],
    [0, 1, -1],
    [1, -1, -1],
    [1, 0, -1],
    [1, 1, -1],
    # Z + 0: Same plane
    [-2, -1, 0],
    [-2, 0, 0],
    [-2, 1, 0],
    [-1, -1, 0],
    [-1, 2, 0],
    [0, -2, 0],
    [0, 2, 0],
    [1, -1, 0],
    [1, 2, 0],
    [2, -1, 0],
    [2, 0, 0],
    [2, 1, 0],
    # Z + 1: 1 Plane above
    [-2, -1, 1],
    [-2, 0, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [0, -2, 1],
    [0, 1, 1],
    [1, -1, 1],
    [1, 0, 1],
    [1, 1, 1],
    # Z + 2: 2 Planes above
    [-1, 0, 2],
    [-1, 1, 2],
    [0, -1, 2],
    [0, 0, 2],
    [0, 1, 2],
    [1, 0, 2],
    [1, 1, 2],
]

twoJumpMatrixEvenZOddX = [
    # Z - 2: 2 Planes above
    [-1, 0, -2],
    [-1, 1, -2],
    [0, -1, -2],
    [0, 0, -2],
    [0, 1, -2],
    [1, 0, -2],
    [1, 1, -2],
    # Z - 1: 1 Plane above
    [-1, -1, -1],
    [-1, 0, -1],
    [-1, 1, -1],
    [0, -1, -1],
    [0, 2, -1],
    [1, -1, -1],
    [1, 1, -1],
    [2, 0, -1],
    [2, 1, -1],
    # Z + 0: Same plane
    [-2, -1, 0],
    [-2, 0, 0],
    [-2, 1, 0],
    [-1, -1, 0],
    [-1, 2, 0],
    [0, -2, 0],
    [0, 2, 0],
    [1, -1, 0],
    [1, 2, 0],
    [2, -1, 0],
    [2, 0, 0],
    [2, 1, 0],
    # Z + 1: 1 Plane above
    [-1, -1, 1],
    [-1, 0, 1],
    [-1, 1, 1],
    [0, -1, 1],
    [0, 2, 1],
    [1, -1, 1],
    [1, 1, 1],
    [2, 0, 1],
    [2, 1, 1],
    # Z + 2: 2 Planes above
    [-1, 0, 2],
    [-1, 1, 2],
    [0, -1, 2],
    [0, 0, 2],
    [0, 1, 2],
    [1, 0, 2],
    [1, 1, 2],
]

twoJumpMatrixEvenZEvenX = [
    # Z - 2: 2 Planes above
    [-1, -1, -2],
    [-1, 0, -2],
    [0, -1, -2],
    [0, 0, -2],
    [0, 1, -2],
    [1, -1, -2],
    [1, 0, -2],
    # Z - 1: 1 Plane above
    [-1, -1, -1],
    [-1, 0, -1],
    [-1, 1, -1],
    [0, -2, -1],
    [0, 1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [2, -1, -1],
    [2, 0, -1],
    # Z + 0: Same plane
    [-2, -1, 0],
    [-2, 0, 0],
    [-2, 1, 0],
    [-1, -2, 0],
    [-1, 1, 0],
    [0, -2, 0],
    [0, 2, 0],
    [1, -2, 0],
    [1, 1, 0],
    [2, -1, 0],
    [2, 0, 0],
    [2, 1, 0],
    # Z + 1: 1 Plane above
    [-1, -1, 1],
    [-1, 0, 1],
    [-1, 1, 1],
    [0, -2, 1],
    [0, 1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [2, -1, 1],
    [2, 0, 1],
    # Z + 2: 2 Planes above
    [-1, -1, 2],
    [-1, 0, 2],
    [0, -1, 2],
    [0, 0, 2],
    [0, 1, 2],
    [1, -1, 2],
    [1, 0, 2],
]

def odd(i):
    if i % 2 == 0:
        return False
    else:
        return True

def even(i):
    if i % 2 == 0:
        return True
    else:
        return False

def duplicateCoordinate(source):
    ret = []
    ret.append(source[0])
    ret.append(source[1])
    ret.append(source[2])
    return ret

def getIsJumpOne(source, destination):
    if odd(source[2]):
        if odd(source[0]):
            matrix = oneJumpMatrixOddZOddX
        else:
            matrix = oneJumpMatrixOddZEvenX
    else:
        if odd(source[0]):
            matrix = oneJumpMatrixEvenZOddX
        else:
            matrix = oneJumpMatrixEvenZEvenX
    for rule in matrix:
        candidate = transform(source, rule)
        if candidate == destination:
            return True
    return False

def getIsJumpTwo(source, destination):
    if odd(source[2]):
        if odd(source[0]):
            matrix = twoJumpMatrixOddZOddX
        else:
            matrix = twoJumpMatrixOddZEvenX
    else:
        if odd(source[0]):
            matrix = twoJumpMatrixEvenZOddX
        else:
            matrix = twoJumpMatrixEvenZEvenX
    for rule in matrix:
        candidate = transform(source, rule)
        if candidate == destination:
            return True
    return False

def transform(source, rule):
    ret = duplicateCoordinate(source)
    ret[0] += rule[0]
    ret[1] += rule[1]
    ret[2] += rule[2]
    return ret

class System:
    def __init__(self, name = "Default", coordinates = [1,1,1]):
        self.name = name
        self.coordinates = duplicateCoordinate(coordinates)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCoordinates(self, coordinates):
        self.coordinates = duplicateCoordinate(coordinates)

    def getCoordinates(self):
        return self.coordinates

    def getString(self):
        return "%-32s [%02d %02d %02d]" % (self.name, self.coordinates[0], self.coordinates[1], self.coordinates[2])

def parseSystemLine(line):
    elements = line.split()
    name = elements[0]
    x = elements[1].strip("[,")
    y = elements[2].strip(",")
    z = elements[3].strip("],")
    return System(name = name, coordinates = [int(x), int(y), int(z)])
  
class Quick3d:
    """
    Density is system presence, in percent
    Size is size of the cube of space, in hexes
    """
    def __init__(self, density = 12, size = 8, name = "Default"):
        self.density = density
        self.size = size
        self.name = name
        self.systems = []

    def generate(self):
        num = 0
        self.systems = []
        mydice = dice.Dice()
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if mydice.roll(1, 100) <= self.density:
                        num += 1
                        name = str(num);
                        system = System(name, [x + 1, y + 1, z + 1])
                        self.systems.append(system)

    def getSystems(self):
        return self.systems

    def show(self):
        print "%d systems:" % (len(self.systems))
        for system in self.systems:
            print system.getString()

    def showJump(self, jump = 2):
        for i in range(1, jump + 1):
            print "Showing all jumps of range %d" % (i)
            self.showOnlyJump(i)

    def showOnlyJump(self, jump):
        if jump > 2:
            print "Sorry we only support jump 1 and 2"
            return
        for source in self.systems:
            for destination in self.systems:
                if jump == 1:
                    if getIsJumpOne(source.getCoordinates(), destination.getCoordinates()):
                        print source.getString() + " -> " + destination.getString()
                if jump == 2:
                    if getIsJumpTwo(source.getCoordinates(), destination.getCoordinates()):
                        print source.getString() + " -> " + destination.getString()

    def showJumpFor(self, source, jump):
        for i in range(1, jump + 1):
            print "Showing all jumps of range %d" % (i)
            self.showOnlyJumpFor(source, i)

    def showOnlyJumpFor(self, source, jump):
        num = 0
        for destination in self.systems:
            if jump == 1:
                if getIsJumpOne(source.getCoordinates(), destination.getCoordinates()):
                    print source.getString() + " -> " + destination.getString()
                    num += 1
            if jump == 2:
                if getIsJumpTwo(source.getCoordinates(), destination.getCoordinates()):
                    print source.getString() + " -> " + destination.getString()
                    num += 1
        print "%d systems" % (num)

    def getOnlyJump(self, jump):
        ret = []
        if jump > 2:
            print "sorry we only support jump 1 and 2"
            return
        for source in self.systems:
            for destination in self.systems:
                if jump == 1:
                    if getIsJumpOne(source.getCoordinates(), destination.getCoordinates()):
                        route = {"Source": source, "Destination": destination}
                        ret.append(route)
                if jump == 2:
                    if getIsJumpTwo(source.getCoordinates(), destination.getCoordinates()):
                        route = {"Source": source, "Destination": destination}
                        ret.append(route)
        return ret


    def save(self, filename):
        f = open(filename, 'w')
        f.write("%-32s size:%d parsecs cube\n" % (self.name, self.size))
        for system in self.systems:
            f.write("%s\n" % (system.getString()))
        f.close()

    def open(self, filename):
        firstline = True
        num = 0
        self.systems = []
        f = open(filename, 'r')
        for line in f:
            if firstline:
                firstline = False
                elements = line.split()
                self.name = elements[0]
                sizeStr = elements[1].strip("size:")
                self.size = int(sizeStr)
            else:
                system = parseSystemLine(line)
                self.systems.append(system)
        f.close()
                


    
       

