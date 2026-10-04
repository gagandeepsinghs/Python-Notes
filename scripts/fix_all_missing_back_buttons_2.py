import glob
import os
import re

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
        return '../index.html'
    elif path.startswith('PHP/'):
        return '../index.html'
    elif path.startswith('React/'):
        return '../index.html'
    
    depth = len(path.split('/')) - 1
    if depth > 0:
        return '../' * depth + 'index.html'
    return 'index.html'

count = 0
for f in all_html:
    filename = os.path.basename(f).lower()
    if 'portal' in filename or 'index' in filename or 'hub' in filename or 'master' in filename:
        continue
        
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    back_link = get_back_link(f)
    new_content = content
    
    # 1. Replace the existing <a onclick="... history.back() ... window.location.href='../index.html' ...">
    # We will just replace window.location.href='../index.html' with window.location.href='back_link'
    
    if "window.location.href='../index.html'" in new_content:
        new_content = new_content.replace(
            "window.location.href='../index.html'",
            f"window.location.href='{back_link}'"
        )
        
    if "window.location.href='../../index.html'" in new_content:
        new_content = new_content.replace(
            "window.location.href='../../index.html'",
            f"window.location.href='{back_link}'"
        )
        
    # Replace plain href="../index.html" that might be a back button
    # but be careful not to replace home links if they aren't back buttons.
    # We look for "Back to Home" or "Back to Main Portal" and change the href before it
    
    # We can use regex to replace href inside an anchor tag that contains "Back"
    # Actually, simpler: replace <a href="../index.html" ...>&larr; Back to Home</a>
    
    new_content = re.sub(
        r'href=["\']\.\./index\.html["\']([^>]*>.*?Back)',
        f'href="{back_link}"\\1',
        new_content,
        flags=re.IGNORECASE
    )
    new_content = re.sub(
        r'href=["\']\.\./\.\./index\.html["\']([^>]*>.*?Back)',
        f'href="{back_link}"\\1',
        new_content,
        flags=re.IGNORECASE
    )

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f} -> {back_link}")

print(f"Fixed {count} files.")
