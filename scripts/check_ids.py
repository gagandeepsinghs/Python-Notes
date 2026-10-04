import os
import glob
import re

css_dir = r"e:\My Projects\Notes\full_stack\css"
html_files = glob.glob(os.path.join(css_dir, "*.html"))

for file in html_files:
    if "00_master_notes_portal.html" in file:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all scrollToSection calls
    scroll_calls = re.findall(r'scrollToSection\((\d+)\)', content)
    
    # Find all sec_ IDs
    sec_ids = re.findall(r'id="sec_(\d+)"', content)
    
    missing = [s for s in scroll_calls if s not in sec_ids]
    if missing:
        print(f"{os.path.basename(file)} is missing IDs: {missing}")

print("Check completed.")
