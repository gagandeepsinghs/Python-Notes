import os
import glob
import re

css_dir = r"e:\My Projects\Notes\full_stack\css"
html_files = glob.glob(os.path.join(css_dir, "*.html"))

count = 0
for file in html_files:
    if "00_master_notes_portal.html" in file:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "scrollToSection(" in content:
        # We will replace `onclick="scrollToSection(1)"` 
        # with `href="#sec_1" onclick="if(window.innerWidth <= 900) toggleSidebar();"`
        # But wait, there might be single quotes or no quotes if they pass variables.
        # It's usually `onclick="scrollToSection(1)"`
        
        new_content = re.sub(
            r'onclick="scrollToSection\((\d+)\)"',
            r'href="#sec_\1" onclick="if(window.innerWidth <= 900) toggleSidebar();"',
            content
        )
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            
print(f"Fixed sidebar links in {count} files.")
