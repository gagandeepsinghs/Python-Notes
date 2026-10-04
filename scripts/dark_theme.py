import glob
import re

def apply_dark_theme():
    files = glob.glob('**/*.html', recursive=True)
    
    replacements = {
        # Backgrounds
        'rgb(248, 250, 252)': 'rgb(9, 9, 11)',      # Main background
        'rgb(255, 255, 255)': 'rgb(24, 24, 27)',      # Card background
        'rgb(17, 24, 60)': 'rgb(18, 18, 20)',         # Sidebar background (from Red/White/Blue theme)
        'rgb(15, 23, 42)': 'rgb(18, 18, 20)',         # Sometimes sidebar or dark text
        
        # Text
        'rgb(15, 23, 42)': 'rgb(244, 244, 245)',      # Dark text -> White text
        'rgb(100, 116, 139)': 'rgb(161, 161, 170)',   # Muted text
        
        # Borders
        'rgb(226, 232, 240)': 'rgb(39, 39, 42)',      # Light border -> Dark border
        
        # Accents (Red to Blue)
        'rgb(220, 38, 38)': 'rgb(59, 130, 246)',      # Red accent -> Python Blue
        'rgb(239, 68, 68)': 'rgb(59, 130, 246)',      # Red accent 2
        '#dc2626': '#3b82f6',                         # Red hex -> Blue hex
        
        # Headings (Dark Blue to White or Blue)
        'rgb(30, 58, 138)': 'rgb(59, 130, 246)',      # Was used for headings, now blue
        
        # Definition boxes (Pink to Dark Grey)
        'rgb(254, 242, 242)': 'rgb(39, 39, 42)',
        'rgb(254, 202, 202)': 'rgb(63, 63, 70)',
        'rgb(153, 27, 27)': 'rgb(244, 244, 245)',
        
        # Additional Java specific stuff (from previous updates)
        'rgb(248, 113, 113)': 'rgb(59, 130, 246)',    # Was Java green -> red -> now blue
        
        # Fix nav-bar and header styles that were hardcoded to white
        'background: rgb(255, 255, 255);': 'background: rgb(18, 18, 20);',
        'background-color: var(--accent-orange)': 'background-color: rgb(59, 130, 246)',
    }

    for filepath in files:
        if 'python_programming_master_notes' in filepath or filepath == 'index.html':
            continue # Don't mess with the source of truth or the main index page
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # Since some keys overlap or might conflict, we do a careful replacement
            # E.g. 'rgb(15, 23, 42)' is both text-primary and bg-sidebar in C++
            # If we change it, it will change text to white and sidebar to white!
            # Wait, if sidebar background becomes 'rgb(244, 244, 245)' that's white.
            # Let's handle the specific CSS variable definitions first.
            
            # Replace CSS variables specifically
            var_replacements = {
                '--bg-page: rgb(248, 250, 252);': '--bg-page: rgb(9, 9, 11);',
                '--bg-dark: rgb(248, 250, 252);': '--bg-dark: rgb(9, 9, 11);',
                '--card-bg: rgb(255, 255, 255);': '--card-bg: rgb(24, 24, 27);',
                '--bg-sidebar: rgb(17, 24, 60);': '--bg-sidebar: rgb(18, 18, 20);',
                '--text-primary: rgb(15, 23, 42);': '--text-primary: rgb(244, 244, 245);',
                '--text-main: rgb(15, 23, 42);': '--text-main: rgb(244, 244, 245);',
                '--text-secondary: rgb(100, 116, 139);': '--text-secondary: rgb(161, 161, 170);',
                '--text-muted: rgb(100, 116, 139);': '--text-muted: rgb(161, 161, 170);',
                '--border-light: rgb(226, 232, 240);': '--border-light: rgb(39, 39, 42);',
                '--border-color: rgb(226, 232, 240);': '--border-color: rgb(39, 39, 42);',
                '--accent-orange: rgb(220, 38, 38);': '--accent-orange: rgb(59, 130, 246);',
                '--accent-blue: rgb(30, 58, 138);': '--accent-blue: rgb(59, 130, 246);',
            }
            
            for k, v in var_replacements.items():
                new_content = new_content.replace(k, v)
                
            # Then run the general replacements
            for k, v in replacements.items():
                new_content = new_content.replace(k, v)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Applied dark theme to {filepath}")
                
        except Exception as e:
            pass

if __name__ == '__main__':
    apply_dark_theme()
