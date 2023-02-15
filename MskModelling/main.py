import os
from bs4 import BeautifulSoup
import pandas as pd
from distutils.dir_util import copy_tree
import shutil

current_script_path = os.path.dirname(__file__) # 'os.path.dirname(__file__)' if.py  'os.getcwd() ' if  .ipynb)
datafolder = r'D:\3-PhD\Data\MocapData\ElaboratedData'
new_folder = r'C:\Users\Biomech\Documents\DataFolder\Running_FAI'
subject_folders = os.listdir(datafolder)
folders_to_copy = ['ceinms', 'dynamicElaborations', 'inverseDynamics',
                   'inverseKinematics','JointReactionAnalysis']

for subject in subject_folders[21:]:
    for fname in folders_to_copy:
        src = os.path.join(datafolder, subject,'pre',fname)
        dst = os.path.join(new_folder, subject,'pre',fname)
        if not os.path.isdir(dst):
            os.makedirs(dst)
        print(str('copying ' + subject + ' ' + fname))
        shutil.copytree(src, dst,dirs_exist_ok=True)
        
        
        
