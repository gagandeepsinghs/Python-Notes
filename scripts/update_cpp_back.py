import glob
import os

cpp_html = glob.glob('C++/*.html')

count = 0
for f in cpp_html:
    if 'portal' in os.path.basename(f).lower() or 'master' in os.path.basename(f).lower():
        continue
        
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    # Replace back button link
    new_content = content.replace("href=\"../index.html\"", "href=\"../cpp_portal.html\"")
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f} -> ../cpp_portal.html")

print(f"Fixed {count} C++ note files.")
