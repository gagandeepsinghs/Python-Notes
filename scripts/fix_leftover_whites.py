import glob

def fix_whites():
    files = glob.glob('**/*.html', recursive=True)
    count = 0
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # The specific inline code and border colors that were accidentally made white
            new_content = new_content.replace('--code-text: rgb(244, 244, 245);', '--code-text: rgb(15, 23, 42);')
            new_content = new_content.replace('--accent-yellow-text: rgb(244, 244, 245);', '--accent-yellow-text: rgb(153, 27, 27);')
            new_content = new_content.replace('--border-color: rgb(244, 244, 245);', '--border-color: rgb(226, 232, 240);')
            
            # General color that was replaced in fix_font_color.py
            new_content = new_content.replace('color: rgb(244, 244, 245);', 'color: rgb(15, 23, 42);')
            # Same for background-color if any
            new_content = new_content.replace('background-color: rgb(244, 244, 245);', 'background-color: rgb(255, 255, 255);')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                
        except Exception as e:
            pass
            
    print(f"Fixed white text in {count} files.")

if __name__ == '__main__':
    fix_whites()
