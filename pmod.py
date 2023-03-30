null = (" ")
error = ("Shape does not exist or has not been added yet. Apologies")

def squarep(squarep):
    side = float(input("Enter the side length"))
    perimeter = str(4 * side)
    print("Perimeter = " + perimeter)

def rectanglep(rectanglep):
    length = float(input("Enter the length"))
    breadth = float(input("Enter the breadth"))
    perimeter = str(2 * length + 2 * breadth)
    print("Perimeter = " + perimeter)

def trianglep(trianglep):
   sideo = float(input("Enter length of the first side"))
   sidet = float(input("Enter length of the second side"))
   sideth = int(input("Enter length of the third side"))
   perimeter = str(sideo + sidet + sideth)
   print("Perimeter = " + perimeter)

def paralellogramap(paralellogramp):
    base = float(input("Enter the base or the line parallel to it"))
    diagonal = float(input("Enter the length of any one of the vertical diagonals"))
    perone = int(2 * base)
    pertwo = int(2 * diagonal)
    perimeter = str(perone + pertwo)
    print("Perimeter = " + perimeter)

def rhombusp(rhombusp):
    side = float(input("Enter the length of a side"))
    perimeter = str(4 * side)
    print("Perimeter = " + perimeter)
