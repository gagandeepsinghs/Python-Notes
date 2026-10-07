import glob
import os

files = glob.glob(r'e:\My Projects\Notes\govt\120 rules of grammer\*.html')

for f in files:
    if 'Grammar_Master_Notes' in f:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'Back to Master' in content:
        continue
        
    back_button = '<a href="Grammar_Master_Notes.html" style="background: var(--accent-blue); color: white; text-align: center; font-weight: bold; margin-bottom: 15px; padding: 10px; border-radius: 5px; display: block;">&larr; Back to Master</a>\n        '
    
    new_content = content.replace('<div class="sidebar">\n        <h2>', '<div class="sidebar">\n        ' + back_button + '<h2>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
    print(f'Updated {f}')
