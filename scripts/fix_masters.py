import os
files = [
    'notes/git_github_master_notes.html',
    'notes/python_programming_master_notes.html',
    'notes/sql_joins_master_notes.html',
    'govt/SSC_Master_Notes_Hub.html'
]
targets = [
    '../github_portal.html',
    '../python_portal.html',
    '../sql_portal.html',
    '../govt_portal.html'
]

for f, t in zip(files, targets):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace("window.location.href='../index.html'", f"window.location.href='{t}'")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
print('Updated 4 master notes files')
