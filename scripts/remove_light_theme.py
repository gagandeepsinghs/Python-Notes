import os
import glob
import re

workspace_dir = r"e:\My Projects\Notes"
# Find all portal files, and index.html
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file == "index.html" or "portal" in file:
            html_files.append(os.path.join(root, file))

# Regex patterns
css_pattern = re.compile(r"\s*body\.light-theme\s*\{[^}]+\}")
btn_pattern = re.compile(r"(?:<!-- Theme Toggle Button -->\s*)?<button class=\"theme-toggle\" id=\"themeToggle\"[^>]*>[\s\S]*?</button>\s*")
js_pattern = re.compile(r"\s*const themeToggleBtn = document\.getElementById\('themeToggle'\);[\s\S]*?\}\);\s*")

files_updated = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    content = css_pattern.sub('', content)
    content = btn_pattern.sub('', content)
    content = js_pattern.sub('\n', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Removed light theme from: {os.path.basename(filepath)}")

print(f"Successfully processed {files_updated} files.")
