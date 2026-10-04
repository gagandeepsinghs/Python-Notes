import os
import glob

workspace_dir = r"e:\My Projects\Notes"
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file == "index.html" or "portal" in file:
            html_files.append(os.path.join(root, file))

files_updated = 0

for filepath in html_files:
    if "original_index.html" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_lines = list(lines)

    new_lines = []
    skip = False
    brace_count = 0

    for line in lines:
        if skip:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count <= 0:
                skip = False
            continue

        if 'light-theme' in line and '{' in line:
            skip = True
            brace_count = line.count('{') - line.count('}')
            if brace_count <= 0:
                skip = False
            continue

        if 'light-theme' in line:
            # Maybe JS or HTML class list
            continue
            
        if 'themeToggle' in line:
            # We already removed the JS block and HTML button in the first script, but just in case
            continue

        new_lines.append(line)

    if lines != new_lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        files_updated += 1
        print(f"Cleaned up light theme from: {os.path.basename(filepath)}")

print(f"Successfully processed {files_updated} files.")
