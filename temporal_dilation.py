#import math
#import sys
from dilation import Schwarzschild, time_Space, Shift

mass = input("Solar masse : ")

"""print("[*] Calculation of the Schwarzschild radius for {0} solar masses using the metric of Schwarzschild : ".format(mass))

RS = 2 * 6.6743 * pow(10,-11) * (int(mass) * 1.989 * pow(10,30)) / pow(299791999.91712,2);

print("	[-] RS = 2GM/c²\n	[-] = 2 * 6.673 * 10^-11 * ({0} * 1.989 * 10^30)\n	[-] = \n	[?] Wolfram Alpha code : 2 * 6.6743 * 10^-11 * ({0} * 1.989 * 10^30) / 300000000^2\n".format(mass,str(RS)))

print("[*] Calculation of the distance of time space at the surface of the object : ")

A = math.sqrt((1 - RS / (7 * pow(10,8))) * pow(1,2) - pow(1 - RS / 7 * pow(10,8),-1)*pow(0,2) - pow(7 * pow(10,8),2) * (0 + pow(math.sin(0),2) * pow(0,2)))

print("	[-] ds² = (1 - RS / r) * dt² - (1 - RS / r)^-1 * dr² - r²(dθ² + sin² θ dφ²)\n	[-] = (1 - {0} / 7 × 10^8) × 1² - (1 - {0} / 7 × 10^8)^-1× 0² - (7 × 10^8)² (0 + sin² (0) × 0²)\n	[-] = {1} \n	[?] Wolfram Alpha code : sqrt((1 - {0} / (7 * 10^8)) * 1^2 - (1 - {0} / 7 * 10^8)^-1*0^2 - (7 * 10^8)^2 (0 + sin^2 (0) * 0^2))﻿\n".format(str(RS), str(A)))

shift = 365*24*3600-365*24*3600*A

if shift < 3600:
	print("If a chronometer was present on the surface of your object, there will be a shift of {0} seconds in one year between the latter and a distant observer".format(str(shift)))
	sys.exit()

elif shift < 86400:
	print("If a chronometer was present on the surface of your object, there will be a shift of {0} hours in one year between the latter and a distant observer".format(str(shift/3600)))
	sys.exit()

elif shift > 86400:
	print("If a chronometer was present on the surface of your object, there will be a shift of {0} days in one year between the latter and a distant observer".format(str(shift/3600)))
	sys.exit()"""


RS = Schwarzschild(mass, 0)
time_Space = time_Space(RS, 0)
print(Shift(time_Space, 1))


# 1.989*10^30
