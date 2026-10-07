import os
import re

def fix_styles(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    encoding_used = 'utf-8'
                except UnicodeDecodeError:
                    with open(file_path, 'r', encoding='utf-16') as f:
                        content = f.read()
                    encoding_used = 'utf-16'
                
                original_content = content
                
                # 1. Replace the color in hinglish-box
                content = content.replace('color: rgb(167, 243, 208)', 'color: #000000')
                
                # 2. Replace the color in mnemonic-box
                content = content.replace('color: rgb(243, 232, 255)', 'color: #000000')

                # 3. Handle strong highlights
                highlight_css = "\n        .hinglish-box strong, .mnemonic-box strong { color: #b91c1c !important; background-color: #fef08a !important; padding: 2px 4px; border-radius: 4px; }\n"
                
                # If there's already a rule for hinglish-box strong, remove it first
                content = re.sub(r'\.hinglish-box strong\s*\{[^}]*\}', '', content)
                content = re.sub(r'\.mnemonic-box strong\s*\{[^}]*\}', '', content)
                
                # Add our new rule before </style>
                if highlight_css not in content:
                    content = content.replace('</style>', highlight_css + '</style>')
                
                if content != original_content:
                    with open(file_path, 'w', encoding=encoding_used) as f:
                        f.write(content)
                    print(f"Updated: {file_path}")

if __name__ == '__main__':
    fix_styles(r'e:\My Projects\Notes\govt')
