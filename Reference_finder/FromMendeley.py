from cgitb import text
import pandas as pd
import pyperclip

txt = 'Fourchet, F., Kelly, L., Horobeanu, C., Loepelt, H., Taiar, R., & Millet, G. (2015). High-intensity running and plantar-flexor fatigability and plantar-pressure  distribution in adolescent runners. Journal of Athletic Training, 50(2), 117–125. https://doi.org/10.4085/1062-6050-49.3.90'
txt = input('Paste the references copied from Mendeley (+ ENTER):') 
parts_comma = txt.split(',')
parts_bracket = txt.split('(')

year = parts_bracket[1].split(')')[0]
name = (parts_comma[0] + 'et al.')
journal = parts_bracket[1].split('.')[2].split(',')[0]

# df = pd.DataFrame(columns = ['name', 'year', 'journal'])
# pd.concat(df,{'name' : name, 'year' : year, 'journal' : journal}, ignore_index = True)
df = pd.DataFrame()
df.insert(0, "name", [name], True)
df.insert(1, "year", [year], True)
df.insert(2, "journal", [journal], True)

df.to_clipboard(excel=True, sep=None, index=False, header=None)
print(txt)