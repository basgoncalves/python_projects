import re

string = 'M\t__pycache__/bops.cpython-38.pyc\nA\tbland_altman.py\nM\tbops_test.py\nA\tjump_height.py\nM\tmain_gait_retraining.py\nM\ttest.py\n'

# Split the string based on the delimiters using regular expression
parts = re.split(r'nM\t|nA\t|nD\t', string)

# Remove empty strings from the list
parts = [part for part in parts if part]

# Join the parts with newlines
result = '\n'.join(parts)

print(result)