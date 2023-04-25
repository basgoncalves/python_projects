import os


text = 'Welcome to datagy.io!'
text2 = 'Bye to datagy.io!'
dir_path = os.path.dirname(os.path.realpath(__file__)) # for .py
txt_file = os.path.join(dir_path, 'changes_summary.txt')

with open(txt_file, 'a') as f:
    f.write(text)
    f.write('\n')
    
with open(txt_file, 'a') as f:
    f.write(text2)