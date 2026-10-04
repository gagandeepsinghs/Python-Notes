import os
import glob

def apply_theme():
    # We will search for all html files
    files = glob.glob('**/*.html', recursive=True)
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # --- General Color Replacements for Red, Blue, White Theme ---
            
            # 1. Replace the bright orange accent in C++/React/PHP
            new_content = new_content.replace('rgb(249, 115, 22)', 'rgb(220, 38, 38)') # Red-600
            
            # 2. Replace the orange hex in the injected buttons
            new_content = new_content.replace('#f97316', '#dc2626')
            
            # 3. Replace the java orange accent
            new_content = new_content.replace('rgb(251, 146, 60)', 'rgb(239, 68, 68)') # Red-500
            
            # 4. Replace the yellow accent boxes (often used for code or notes) with light red/pink ones
            # Yellow bg -> Red-50 bg
            new_content = new_content.replace('rgb(254, 243, 199)', 'rgb(254, 242, 242)')
            # Yellow border -> Red-200 border
            new_content = new_content.replace('rgb(253, 230, 138)', 'rgb(254, 202, 202)')
            # Yellow text -> Red-800 text
            new_content = new_content.replace('rgb(146, 64, 14)', 'rgb(153, 27, 27)')
            
            # 5. In PHP files, the orange is sometimes different
            new_content = new_content.replace('rgb(217, 119, 6)', 'rgb(220, 38, 38)')
            
            # Make the sidebar a stronger/truer blue if it's currently slate? 
            # The current slate is rgb(15, 23, 42). A truer navy blue might be rgb(10, 25, 65) or rgb(30, 58, 138).
            # The prompt says "red blue and white", the slate is already a dark blueish grey, 
            # but let's make it a deeper, more pronounced navy blue to fit "blue" better.
            new_content = new_content.replace('rgb(15, 23, 42)', 'rgb(17, 24, 60)') # Deep Navy Blue
            
            # Java files use a different dark theme base: rgb(30, 41, 59)
            new_content = new_content.replace('rgb(30, 41, 59)', 'rgb(30, 58, 138)') # Brighter Navy Blue for cards
            
            # Change java accent green/purple to white/red to stick strictly to red/blue/white?
            # Java green: rgb(74, 222, 128) -> we can make it White or Red
            # Let's make green -> Red-400: rgb(248, 113, 113)
            new_content = new_content.replace('rgb(74, 222, 128)', 'rgb(248, 113, 113)')
            # Java purple: rgb(192, 132, 252) -> White/Silver: rgb(226, 232, 240)
            new_content = new_content.replace('rgb(192, 132, 252)', 'rgb(226, 232, 240)')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated theme for {filepath}")
                
        except Exception as e:
            pass

if __name__ == '__main__':
    apply_theme()
