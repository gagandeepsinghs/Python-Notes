import glob

def fix_code_font():
    files = glob.glob('**/*.html', recursive=True)
    count = 0
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # We want to replace "color: rgb(39, 39, 42);" with "color: rgb(244, 244, 245);"
            # This fixes the dark text that was erroneously changed by dark_theme.py
            if 'color: rgb(39, 39, 42);' in content:
                content = content.replace('color: rgb(39, 39, 42);', 'color: rgb(244, 244, 245);')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed font color in {filepath}")
        except Exception as e:
            pass
            
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    fix_code_font()
