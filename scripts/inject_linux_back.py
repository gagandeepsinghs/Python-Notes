import os
import glob

linux_dir = r"e:\My Projects\Notes\Linux Administration"
# All html files except the portal itself
html_files = [f for f in glob.glob(os.path.join(linux_dir, "*.html")) if "portal" not in os.path.basename(f)]

back_button_html = '<a href="00_master_notes_portal.html" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #facc15; color: #000; cursor: pointer; font-weight: bold;">← Back to Modules</a>'

count = 0
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'Back to Modules' in content:
        continue
        
    if '<div class="sidebar-header">' in content:
        new_content = content.replace(
            '<div class="sidebar-header">',
            f'<div class="sidebar-header">\n            {back_button_html}'
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {os.path.basename(f)}")

print(f"Injected back buttons into {count} Linux notes files.")
