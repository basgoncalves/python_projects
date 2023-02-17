
import os
import struct
import sys
os.add_dll_directory("C:/OpenSim 4.4/bin")
os.add_dll_directory("C:/OpenSim 4.4/sdk")
os.add_dll_directory("C:/OpenSim 4.4/sdk/Simbody")

print(struct.calcsize("P") * 8)
