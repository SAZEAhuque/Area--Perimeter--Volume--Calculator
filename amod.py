null = (" ")
error = ("Shape does not exist or has not been added yet. Apologies")

def squarea(squarea):
    side = float(input("Enter the side length"))
    area = str(side * side)
    print("Area = " + area)

def rectanglea(rectanglea):
    length = float(input("Enter the length"))
    breadth = float(input("Enter the breadth"))
    area = str(length * breadth)
    print("Area = " + area)

def trianglea(trianglea):
    base = float(input("Enter the base"))
    height = float(input('Enter the height'))
    areao = int(base * height)
    area = str(areao / 2)
    print("Area = " + area)

def paralellograma(paralellograma):
    base = float(input("Enter the base or the line parallel to it"))
    height = float(input("Enter the height"))
    diagonal = float(input("Enter the length of any one of the vertical diagonals"))
    area = str(base * height)
    perone = int(2 * base)
    pertwo = int(2 * diagonal)
    perimeter = str(perone + pertwo)
    print(("Area = " + area))

def rhombusa(rhombusa):
    diagonalone = int(input("Enter the length of one inner diagonal"))
    diagonaltwo = int(input("Enter the length of the other inner diagonal"))
    diags = int(diagonalone * diagonaltwo)
    area = str(diags / 2)
    print("Area = " + area)