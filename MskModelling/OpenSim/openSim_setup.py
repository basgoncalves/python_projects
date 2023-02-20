
import os
import struct
import sys
os.add_dll_directory("C:/OpenSim 4.3/bin")
os.add_dll_directory(r'C:\Users\Biomech\AppData\Local\Programs\Python\Python38\Lib\site-packages\btk')

print('python installed with ' + str(struct.calcsize("P") * 8) + ' bits')

