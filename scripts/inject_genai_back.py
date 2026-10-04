import os
import glob
import re

genai_dir = r"e:\My Projects\Notes\Gen AI"
html_files = glob.glob(os.path.join(genai_dir, "*.html"))

# 1. Back button for regular notes files -> 00_master_notes_portal.html
notes_back_button = '<a href="00_master_notes_portal.html" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #f97316; cursor: pointer;">← Back to Modules</a>'

# 2. Back button for the portal itself -> ../index.html
portal_back_button = '<a href="../index.html" class="brand-badge" style="display: inline-block; margin-bottom: 15px; background-color: #f97316; cursor: pointer; text-decoration: none;">← Back to Home</a><br>'

for f in html_files:
    filename = os.path.basename(f)
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original_content = content
    
    if "portal" in filename:
        pass # Already handled by the recreate_genai_portal.py because it copied from Java which has the top left back button!
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

print("Gen AI files processed successfully.")
