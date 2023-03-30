import math as m
import amod as a
import pmod as p

shapes = ['SQUARE', 'RECTANGLE', 'TRIANGLE', 'RHOMBUS', 'PARALELLOGRAM']

null = ('Calculating...')

error = ("Shape does not exist or has not been added yet. Apologies")

dimen = input('Do you want to calculate a 2D or a 3D object').upper()
if dimen == ('2D'):
    aorp = input('Do you want to calculate Area or Perimeter').upper()
elif dimen == ('3D'):
    vors = input('DO you want to calculate Volume or Surface Area').upper()

if aorp == ('AREA'):
    shapea = input('Choose a shape').upper()

if shapea == ('SQUARE'):
    a.squarea(null)
elif shapea == ('RECTANGLE'):
    a.rectanglea(null)
elif shapea == ('TRIANGLE'):
    a.trianglea(null)
elif shapea == ('RHOMBUS'):
    a.rhombusa(null)
elif shapea == ('PARALELLOGRAM'):
    a.paralellograma(null)
else:
    print(error)

if aorp == ('PERIMETER'):
    shapeb = input('Choose a shape').upper()

if shapeb == ('SQUARE'):
    p.squarep(null)
elif shapeb == ('RECTANGLE'):
    p.rectanglep(null)
elif shapeb == ('TRIANGLE'):
    p.trianglep(null)
elif shapeb == ('RHOMBUS'):
    p.rhombusp(null)
elif shapeb == ('PARALELLOGRAM'):
    p.paralellogramp(null)
else:
    print(error)

if shapea not in shapes:
    print(error)
if shapeb not in shapes:
    print(error)
