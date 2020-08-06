from pydilation import Schwarzschild, time_Space, Shift

try:
    mass = int(input("Solar masse : "))
except ValueError:
    print("You must enter an integer.")

print(Shift(time_Space(Schwarzschild(mass, 0), 0), 1))

### Details : 

"""RS = Schwarzschild(mass, 0)
print(Schwarzschild(mass, 1))
timeSpace = time_Space(RS, 0)
print(time_Space(RS, 1))
print(Shift(time_Space(RS, 0), 1))"""
