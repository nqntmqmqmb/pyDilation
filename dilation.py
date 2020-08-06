import math
import sys

phrase = "If a chronometer was present on the surface of your object, there will be a shift of {0} seconds in one year between the latter and a distant observer"

def Schwarzschild(mass, details):
    RS = 2 * 6.6743 * pow(10,-11) * (mass * 1.989 * pow(10,30)) / pow(299791999.91712,2)
    if details == 0:
        return RS
    else:
        return "[-] RS = 2GM/c²\n[-] = 2 * 6.673 * 10^-11 * ({0} * 1.989 * 10^30)\n[-] = {1}\n[?] Wolfram Alpha code : 2 * 6.6743 * 10^-11 * ({0} * 1.989 * 10^30) / 300000000^2".format(mass,str(RS))


def time_Space(RS, details):
    A = math.sqrt((1 - RS / (7 * pow(10,8))) * pow(1,2) - pow(1 - RS / 7 * pow(10,8),-1)*pow(0,2) - pow(7 * pow(10,8),2) * (0 + pow(math.sin(0),2) * pow(0,2)))
    if details == 0:
        return A
    else:
        return "[-] ds² = (1 - RS / r) * dt² - (1 - RS / r)^-1 * dr² - r²(dθ² + sin² θ dφ²)\n[-] = (1 - {0} / 7 × 10^8) × 1² - (1 - {0} / 7 × 10^8)^-1× 0² - (7 × 10^8)² (0 + sin² (0) × 0²)\n[-] = {1} \n[?] Wolfram Alpha code : sqrt((1 - {0} / (7 * 10^8)) * 1^2 - (1 - {0} / 7 * 10^8)^-1*0^2 - (7 * 10^8)^2 (0 + sin^2 (0) * 0^2))\n".format(str(RS), str(A))

def Shift(time_space, details):
    shift = 365*24*3600-365*24*3600*time_space
    if details == 0:
        if shift < 3600:
            return shift

        elif shift < 86400:
            return shift/3600

        elif shift > 86400:
            return shift/3600
    else:
        if shift < 3600:
            return phrase.format(str(shift))

        elif shift < 86400:
            return phrase.format(str(shift/3600))

        elif shift > 86400:
            return phrase.format(str(shift/3600))
