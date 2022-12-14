# Exercises 13.3, 13.5, 13.11
# Chapter 13
# Carlos Rodriguez Escamilla
# 11/21/2022

# 13.3 Process scores in a text file

def main():
    userFile = input("Enter a filename: ")
    infile = open(userFile, "r")
    s = infile.read()
    scoresArr = [eval(num) for num in s.split()]
    total = 0

    for num in scoresArr:
        total+=num
    
    average = round((total / len(scoresArr)), 2)
    
    infile.close()
    
    print(f"There are {len(scoresArr)} scores")
    print(f"The total is {total}")
    print(f"The average is {average}")

# main()

# Exercise 13.5

def main2():
    userFile = input("Enter a filename: ")
    oldStr = input("Enter the old string to be replaced: ")
    newStr = input("Enter the new string to replace the old string: ")
    infile = open(userFile, "r")
    fileData = infile.read()
    fileData = fileData.replace(oldStr, newStr)
    infile.close()

    infile = open(userFile, "w")
    infile.write(fileData)
    infile.close()

    print("Done")

# main2()

import math


class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return bool(self.__filled)

    def setFilled(self, filled):
        if filled == 0 or filled == 1:
            self.__filled = filled
        else:
            print("Oops, enter 1 for filled, or 0 for a blank triangle.")
    
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)


class Triangle(GeometricObject):
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        self.setSide1(side1)
        self.setSide2(side2)
        self.setSide3(side3)

    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3
    
    def setSide1(self, side1):
        if self.__side2 + self.__side3 > side1:
            self.__side1 = side1
        else:
            raise RuntimeError("Invalid Triangle")

    def setSide2(self, side2):
        if self.__side1 + self.__side3 > side2:
            self.__side2 = side2
        else:
            raise RuntimeError("Invalid Triangle")
    
    def setSide3(self, side3):
        if self.__side1 + self.__side2 > side3:
            self.__side3 = side3
        else:
            raise RuntimeError("Invalid Triangle")

    def getArea(self):
        semiPerimeter = ((self.__side1 + self.__side2 + self.__side3) / 2)
        area = round(math.sqrt((semiPerimeter * (semiPerimeter - self.__side1) * (semiPerimeter - self.__side2) * (semiPerimeter - self.__side3))), 3)
        return area
    
    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3)


def main():
    try:
        side1, side2, side3 = eval(input("Enter three triangle sides (comma separated): "))
        triangleColor = input("Enter triangle color: ")
        isTriangleFilled = eval(input("Enter 1 to fill triangle with color. 0 for unfilled: "))

        triangle = Triangle(triangleColor, isTriangleFilled, side1, side2, side3)

        area = triangle.getArea()
        perimeter = triangle.getPerimeter()
        color = triangle.getColor()
        isFilled = triangle.isFilled()

        print(f"\n{triangle}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
        print(f"Color: {color}")
        print(f"Is Filled: {isFilled}")

    except RuntimeError:
        print("Cannot form a triangle if the sum of any two sides is less than the third")



main()
