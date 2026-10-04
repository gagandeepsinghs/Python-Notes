import glob
import os

all_html = glob.glob('**/*.html', recursive=True)

def get_back_link(filepath):
    path = filepath.replace('\\', '/')
    filename = os.path.basename(path).lower()
    
    if path.startswith('C/'):
        return '../c_portal.html'
    elif path.startswith('govt/'):
        return '../govt_portal.html'
    elif path.startswith('java/'):
        return 'master_notes_portal.html'
    elif path.startswith('sql/'):
        return '../sql_portal.html'
    elif path.startswith('notes/'):
        if 'flask' in filename or 'excel' in filename or 'powerbi' in filename:
            return '../other_portal.html'
        elif 'git' in filename:
            return '../github_portal.html'
        elif 'sql' in filename:
            return '../sql_portal.html'
        else:
            return '../python_portal.html'
    elif path.startswith('C++/'):
        # Fallback if no specific portal is known
        return '../index.html'
    elif path.startswith('PHP/'):
        return '../index.html'
    elif path.startswith('React/'):
        return '../index.html'
    
    # Generic fallback
    depth = len(path.split('/')) - 1
    if depth > 0:
        return '../' * depth + 'index.html'
    return 'index.html'

count = 0
for f in all_html:
    # Skip portals
    filename = os.path.basename(f).lower()
    if 'portal' in filename or 'index' in filename or 'hub' in filename or 'master' in filename:
        continue
        
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    if 'Back to Portal' in content or 'Back to Module' in content:
        continue
        
    back_link = get_back_link(f)
    back_button_html = f'''<a href="{back_link}" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #3b82f6; cursor: pointer;">← Back to Portal</a>'''
    
    if '<div class="sidebar-header">' in content:
        new_content = content.replace(
            '<div class="sidebar-header">',
            f'<div class="sidebar-header">\n            {back_button_html}'
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f} -> {back_link}")
    elif '<div class="sidebar-logo">' in content:
        new_content = content.replace(
            '<div class="sidebar-logo">',
            f'<div class="sidebar-logo">\n            {back_button_html}'
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f} -> {back_link}")

print(f"Injected back buttons into {count} missed note files.")
