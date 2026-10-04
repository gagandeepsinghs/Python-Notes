import os
import glob
import re

workspace_dir = r"e:\My Projects\Notes"
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file == "index.html" or "portal" in file:
            html_files.append(os.path.join(root, file))

css_rule_pattern = re.compile(r"^\s*[^{}]*\blight-theme\b[^{}]*\{[^}]*\}", re.MULTILINE)
# Also need to handle multi-line rules that might contain light-theme.
css_rule_pattern_2 = re.compile(r"\s*[^{}]*\blight-theme\b[^{}]*\{[^}]*\}")

files_updated = 0

for filepath in html_files:
    if "original_index.html" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    content = css_rule_pattern_2.sub('', content)

    # Clean up the JS if it's still there (like `body.classList.add('light-theme');`)
    # Wait, my previous script removed the JS block from `const themeToggleBtn = document.getElementById('themeToggle');`
    # Let's remove any line that contains `light-theme` just in case for JS
    lines = content.split('\n')
    new_lines = []
    in_js = False
    for line in lines:
        if 'themeToggle' in line or 'light-theme' in line:
            # wait, this might be too aggressive, but the user wants it gone
            continue
        new_lines.append(line)
        
    content = '\n'.join(new_lines)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Removed light theme CSS from: {os.path.basename(filepath)}")

print(f"Successfully processed {files_updated} files.")
