import os
import glob
import re

linux_dir = r"e:\My Projects\Notes\Linux Administration"
html_files = glob.glob(os.path.join(linux_dir, "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # 1. Fix back button to 00_master_notes_portal.html
    content = content.replace("onclick=\"window.location.href='master_notes_portal.html'\"", "onclick=\"window.location.href='00_master_notes_portal.html'\"")
    
    # 2. Fix sidebar links
    content = re.sub(
        r'onclick="scrollToSection\((\d+)\)"',
        r'href="#sec_\1" onclick="if(window.innerWidth <= 900) toggleSidebar();"',
        content
    )
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Fixed back buttons and sidebar links in Linux Administration files.")
