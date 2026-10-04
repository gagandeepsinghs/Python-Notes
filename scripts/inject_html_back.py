import os
import glob
import re

html_dir = r"e:\My Projects\Notes\full_stack\html"
html_files = glob.glob(os.path.join(html_dir, "*.html"))

# 1. Back button for regular notes files -> 00_master_notes_portal.html
notes_back_button = '<a href="00_master_notes_portal.html" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #f97316; cursor: pointer;">← Back to Modules</a>'

# 2. Back button for the portal itself -> ../../full_stack_portal.html
portal_back_button = '<a href="../../full_stack_portal.html" class="brand-badge" style="display: inline-block; margin-bottom: 15px; background-color: #f97316; cursor: pointer; text-decoration: none;">← Back to Full Stack Portal</a><br>'

for f in html_files:
    filename = os.path.basename(f)
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original_content = content
    
    if "portal" in filename:
        if "Back to Full Stack Portal" not in content and '<header class="portal-header">' in content:
            content = content.replace('<header class="portal-header">\n        <span class="brand-badge">', '<header class="portal-header">\n        ' + portal_back_button + '\n        <span class="brand-badge">')
    else:
        if "Back to Modules" not in content and '<div class="sidebar-header">' in content:
            content = content.replace('<div class="sidebar-header">', '<div class="sidebar-header">\n            ' + notes_back_button)
        
        # Fix sidebar href scroll if it has the old onclick issue
        content = re.sub(
            r'onclick="scrollToSection\((\d+)\)"',
            r'href="#sec_\1" onclick="if(window.innerWidth <= 900) toggleSidebar();"',
            content
        )
            
    if content != original_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated: {filename}")

print("HTML files processed successfully.")
