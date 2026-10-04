import os
import glob

css_dir = r"e:\My Projects\Notes\full_stack\css"
html_files = glob.glob(os.path.join(css_dir, "*.html"))

count = 0
for file in html_files:
    if os.path.basename(file) == "00_master_notes_portal.html":
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "master_notes_portal.html" in content and "00_master_notes_portal.html" not in content:
        new_content = content.replace("master_notes_portal.html", "00_master_notes_portal.html")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        
print(f"Fixed back buttons in {count} files.")
