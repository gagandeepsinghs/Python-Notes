import os
import glob
import re

def remove_gagan(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.py'):
                file_path = os.path.join(root, file)
                
                # skip this script itself
                if file == 'remove_gagan.py':
                    continue
                    
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    encoding_used = 'utf-8'
                except UnicodeDecodeError:
                    with open(file_path, 'r', encoding='utf-16') as f:
                        content = f.read()
                    encoding_used = 'utf-16'
                
                original_content = content
                
                # HTML replacements
                content = content.replace('<span class="brand-badge">Created by Gagan Sir</span>', '')
                content = content.replace('<span class="author-tag">Created by Gagan Sir</span>', '')
                content = content.replace(' - Created by Gagan Sir</title>', '</title>')
                
                # Python string replacements (if any are hardcoded in print/write statements)
                content = content.replace('\'<span class="brand-badge">Created by Gagan Sir</span>\'', '\'\'')
                content = content.replace('\'<span class="author-tag">Created by Gagan Sir</span>\'', '\'\'')
                
                # If there are any other specific occurrences, maybe regex:
                # e.g., whitespace variations
                content = re.sub(r'<span class="brand-badge">\s*Created by Gagan Sir\s*</span>', '', content)
                content = re.sub(r'<span class="author-tag">\s*Created by Gagan Sir\s*</span>', '', content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding=encoding_used) as f:
                        f.write(content)
                    print(f"Updated: {file_path}")

if __name__ == '__main__':
    remove_gagan(r'e:\My Projects\Notes')
