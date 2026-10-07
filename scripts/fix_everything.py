import os
import re

def fix_everything(directory):
    back_btn = '\n        <a href="javascript:void(0)" onclick="if(window.history.length > 1) { history.back(); } else { window.location.href=\'../index.html\'; }" style="display:inline-block; margin-bottom: 15px; padding: 6px 12px; background-color: var(--bg-tertiary, #2c2c2c); color: var(--text-primary, #fff); text-decoration: none; font-size: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #444);">&larr; Back</a>'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    encoding_used = 'utf-8'
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='utf-16') as f:
                            content = f.read()
                        encoding_used = 'utf-16'
                    except:
                        continue
                
                original_content = content
                
                # 1. Add back button if sidebar exists but back button doesn't
                if '<div class="sidebar"' in content and 'history.back()' not in content:
                    # Find the first sidebar div and insert the button right after it
                    content = re.sub(
                        r'(<div\s+class="sidebar"[^>]*>)',
                        r'\1' + back_btn,
                        content,
                        count=1
                    )
                
                # 2. Remove / Replace Gagan Sir
                content = content.replace('by Gagan Sir ✌️✌️', 'Keep Learning ✌️✌️')
                content = content.replace('Python with Gagan Sir.', 'Python Learning.')
                content = content.replace('Created by Gagan Sir', '')
                content = content.replace('Gagan Sir', 'Instructor')
                
                if content != original_content:
                    with open(file_path, 'w', encoding=encoding_used) as f:
                        f.write(content)
                    print(f"Updated: {file_path}")

if __name__ == '__main__':
    fix_everything(r'e:\My Projects\Notes')
