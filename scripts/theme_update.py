import os
import glob

def update_java_css(content):
    # Make java background white
    content = content.replace('--bg-dark: rgb(17, 24, 60);', '--bg-dark: rgb(248, 250, 252);')
    content = content.replace('--bg-dark: rgb(15, 23, 42);', '--bg-dark: rgb(248, 250, 252);')
    content = content.replace('--card-bg: rgb(30, 58, 138);', '--card-bg: rgb(255, 255, 255);')
    content = content.replace('--card-bg: rgb(30, 41, 59);', '--card-bg: rgb(255, 255, 255);')
    
    # Text dark for readability on white
    content = content.replace('--text-main: rgb(241, 245, 249);', '--text-main: rgb(15, 23, 42);')
    content = content.replace('--text-muted: rgb(148, 163, 184);', '--text-muted: rgb(100, 116, 139);')
    content = content.replace('--border-color: rgb(51, 65, 85);', '--border-color: rgb(226, 232, 240);')
    
    # Headings blue
    content = content.replace('--accent-blue: rgb(56, 189, 248);', '--accent-blue: rgb(30, 58, 138);') # Darker blue
    
    # Make Java header white background or keep it blue? "little bit blue headigns" -> Make text blue, background white
    content = content.replace('background: linear-gradient(135deg, rgb(30, 58, 138), rgb(17, 24, 60));', 'background: rgb(255, 255, 255);')
    content = content.replace('background: rgb(30, 58, 138);', 'background: rgb(255, 255, 255);')
    
    # Make nav-back a red button
    if '.nav-back {' in content:
        # We replace the .nav-back block if it doesn't already have background-color
        if 'background-color: var(--accent-orange)' not in content:
            content = content.replace(
                '.nav-back {\n            color: var(--accent-blue);', 
                '.nav-back {\n            background-color: var(--accent-orange);\n            color: white;\n            padding: 8px 16px;\n            border-radius: 6px;'
            )
            
    # Fix the link to point to index.html and change text
    targets = [
        "window.location.href='master_notes_portal.html'",
        "window.location.href='java_programming_master_notes.html'"
    ]
    for t in targets:
        content = content.replace(t, "window.location.href='../index.html'")
        
    return content

def update_all_back_buttons(content, depth):
    up_path = '../' * depth + 'index.html'
    
    # For C++, React, PHP, we previously set them to cpp_programming_master_notes.html etc.
    # The user wants them ALL to go to the portal in the 3rd pic (which is index.html).
    portals = ['cpp_programming_master_notes.html', 'php_programming_master_notes.html', 'react_master_notes.html']
    for p in portals:
        content = content.replace(f'href="{p}"', f'href="{up_path}"')
        
    # Ensure they look like buttons (the injected ones already do, but we ensure text is right)
    content = content.replace('Back to Master Portal', 'Back to Main Portal')
    content = content.replace('Back to Modules', 'Back to Main Portal')
    
    return content

def main():
    files = glob.glob('**/*.html', recursive=True)
    for filepath in files:
        if 'index.html' in filepath and os.path.dirname(filepath) == '':
            continue # skip main index
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            depth = len(filepath.replace('\\', '/').split('/')) - 1
            
            if 'java' in filepath:
                new_content = update_java_css(new_content)
                
            new_content = update_all_back_buttons(new_content, depth)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
                
        except Exception as e:
            pass

if __name__ == '__main__':
    main()
