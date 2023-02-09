# actiavte mskenvironment 
# cd C:\Git
# .\Python_environments\mskmodelling\Scripts\activate

# adding msk_modelling_pkg_install to the system path
import sys
sys.path.append(r'..\Utils')
import msk_modelling_pkg_install

import os
from bs4 import BeautifulSoup
import pandas as pd
from distutils.dir_util import copy_tree
import shutil
import osimPaths as op

current_script_path = os.path.dirname(__file__) # 'os.path.dirname(__file__)' if.py  'os.getcwd() ' if  .ipynb)
datafolder = r'Z:\EMG_realtime_biofeedback'

Dir = op.getosimPath(datafolder)

print(type(Dir))

# second_list = list(Dir.values())[0]
# print(type(second_list))

# print(list(second_list.values())['current'])

# new_folder = r'C:\Users\Biomech\Documents\DataFolder\Running_FAI'

# subject_folders = os.listdir(datafolder)

# folders_to_copy = ['ceinms', 'dynamicElaborations', 'inverseDynamics',
#                    'inverseKinematics','JointReactionAnalysis']

# for subject in subject_folders[21:]:
#     for fname in folders_to_copy:
#         src = os.path.join(datafolder, subject,'pre',fname)
#         dst = os.path.join(new_folder, subject,'pre',fname)
#         if not os.path.isdir(dst):
#             os.makedirs(dst)
#         print(str('copying ' + subject + ' ' + fname))
#         shutil.copytree(src, dst,dirs_exist_ok=True)
        
        
        
