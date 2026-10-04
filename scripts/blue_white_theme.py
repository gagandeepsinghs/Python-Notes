import glob
import re

def apply_blue_white_theme():
    files = glob.glob('**/*.html', recursive=True)
    
    for filepath in files:
        if 'python_programming_master_notes' in filepath or filepath == 'index.html':
            pass # Maybe we should apply it to python_programming_master_notes too? User said "every module that i have given you today"
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # --- CSS Variables ---
            var_replacements = {
                '--bg-page: rgb(9, 9, 11);': '--bg-page: rgb(248, 250, 252);',
                '--bg-dark: rgb(9, 9, 11);': '--bg-dark: rgb(248, 250, 252);',
                '--card-bg: rgb(24, 24, 27);': '--card-bg: rgb(255, 255, 255);',
                '--bg-sidebar: rgb(18, 18, 20);': '--bg-sidebar: rgb(30, 58, 138);',
                '--text-primary: rgb(244, 244, 245);': '--text-primary: rgb(15, 23, 42);',
                '--text-primary: rgb(18, 18, 20);': '--text-primary: rgb(15, 23, 42);',
                '--text-main: rgb(244, 244, 245);': '--text-main: rgb(15, 23, 42);',
                '--text-secondary: rgb(161, 161, 170);': '--text-secondary: rgb(100, 116, 139);',
                '--text-muted: rgb(161, 161, 170);': '--text-muted: rgb(100, 116, 139);',
                '--border-light: rgb(39, 39, 42);': '--border-light: rgb(226, 232, 240);',
                '--border-color: rgb(39, 39, 42);': '--border-color: rgb(226, 232, 240);',
            }
            for k, v in var_replacements.items():
                new_content = new_content.replace(k, v)
                
            # --- Specific Element Fixes ---
            
            # .portal-header: has blue sidebar background, so text must be white
            new_content = new_content.replace(
                '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(244, 244, 245);',
                '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(255, 255, 255);'
            )
            # just in case it had the old dark color
            new_content = new_content.replace(
                '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(24, 24, 27);',
                '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(255, 255, 255);'
            )
            
            # .header-card
            new_content = re.sub(
                r'\.header-card\s*{[^}]+background:[^;]+;',
                '.header-card {\n            background: linear-gradient(135deg, rgb(30, 58, 138) 0%, rgb(59, 130, 246) 100%);',
                new_content
            )
            
            # .header-banner gradient (for java notes portal)
            new_content = re.sub(
                r'\.header-banner\s*{[^}]+background:[^;]+;',
                '.header-banner {\n            background: linear-gradient(135deg, rgb(30, 58, 138) 0%, rgb(59, 130, 246) 100%);',
                new_content
            )
            
            # Text inside header-banner and header-card should be white
            new_content = re.sub(r'\.header-banner h1\s*{[^}]+color:[^;]+;', '.header-banner h1 {\n            font-size: 2.2rem;\n            color: rgb(255, 255, 255);', new_content)
            new_content = re.sub(r'\.header-card h1\s*{[^}]+color:[^;]+;', '.header-card h1 {\n            font-size: 2.3rem;\n            color: rgb(255, 255, 255);', new_content)
            new_content = re.sub(r'\.header-card p\s*{[^}]+color:[^;]+;', '.header-card p {\n            color: rgb(241, 245, 249);', new_content)
            
            # .master-banner
            new_content = re.sub(
                r'\.master-banner\s*{[^}]+padding: 28px 32px;\n\s*color:[^;]+;',
                '.master-banner {\n            background: linear-gradient(135deg, rgb(30, 58, 138) 0%, rgb(59, 130, 246) 100%);\n            border-radius: 12px;\n            padding: 28px 32px;\n            color: rgb(255, 255, 255);',
                new_content
            )
            new_content = new_content.replace(
                'background: linear-gradient(135deg, rgb(18, 18, 20) 0%, rgb(59, 130, 246) 100%);',
                'background: linear-gradient(135deg, rgb(30, 58, 138) 0%, rgb(59, 130, 246) 100%);'
            )
            
            # .sidebar
            new_content = re.sub(
                r'\.sidebar\s*{[^}]+background-color:[^;]+;',
                '.sidebar {\n            background-color: rgb(30, 58, 138);',
                new_content
            )
            
            # .sidebar h2 (white text)
            new_content = re.sub(
                r'\.sidebar h2\s*{[^}]+color:[^;]+;',
                '.sidebar h2 {\n            font-size: 1.15rem;\n            margin-bottom: 5px;\n            color: rgb(255, 255, 255);',
                new_content
            )
            
            # .sidebar .author-tag (lighter blue/white text)
            new_content = re.sub(
                r'\.sidebar \.author-tag\s*{[^}]+color:[^;]+;',
                '.sidebar .author-tag {\n            font-size: 0.85rem;\n            color: rgb(191, 219, 254);',
                new_content
            )
            
            # .nav-link (normal state: light blue text)
            new_content = re.sub(
                r'\.nav-link\s*{[^}]+color:\s*rgb\(212, 212, 216\);',
                '.nav-link {\n            color: rgb(219, 234, 254);',
                new_content
            )
            # .nav-link:hover (white bg, blue text)
            new_content = re.sub(
                r'\.nav-link:hover\s*{[^}]+}',
                '.nav-link:hover {\n            background-color: rgb(255, 255, 255);\n            color: rgb(30, 58, 138);\n        }',
                new_content
            )
            
            # .btn-card
            new_content = re.sub(
                r'\.btn-card\s*{[^}]+background-color:[^;]+;\n\s*color:[^;]+;',
                '.btn-card {\n            display: block;\n            text-align: center;\n            background-color: rgb(239, 246, 255);\n            color: rgb(30, 58, 138);',
                new_content
            )
            new_content = re.sub(
                r'\.btn-card:hover\s*{[^}]+}',
                '.btn-card:hover {\n            background-color: rgb(59, 130, 246);\n            color: rgb(255, 255, 255);\n        }',
                new_content
            )
            
            # .tag-btn (which I had changed to dark text)
            new_content = re.sub(
                r'\.tag-btn\s*{[^}]+background-color:[^;]+;\n\s*color:[^;]+;',
                '.tag-btn {\n            background-color: rgb(239, 246, 255);\n            color: rgb(30, 58, 138);',
                new_content
            )
            
            # .section-title (blue text for headings on white background)
            new_content = re.sub(
                r'\.section-title\s*{[^}]+color:[^;]+;',
                '.section-title {\n            font-size: 1.45rem;\n            color: rgb(30, 58, 138);',
                new_content
            )
            # Wait, java files have .section-title with flex stuff.
            if 'java' in filepath:
                new_content = re.sub(
                    r'\.section-title\s*{[^}]+color:[^;]+;',
                    '.section-title {\n            color: rgb(30, 58, 138);',
                    new_content
                )
                
            # Code headers and back-to-top etc
            # Backgrounds
            new_content = new_content.replace('rgb(9, 9, 11)', 'rgb(248, 250, 252)')      # Main background
            new_content = new_content.replace('rgb(24, 24, 27)', 'rgb(255, 255, 255)')    # Card background
            new_content = new_content.replace('rgb(18, 18, 20)', 'rgb(30, 58, 138)')      # Remaining Dark grey -> Blue
            new_content = new_content.replace('rgb(39, 39, 42)', 'rgb(226, 232, 240)')    # Dark border -> Light border
            
            # Accents: Ensure blue is used instead of reds or greens
            new_content = new_content.replace('var(--accent-orange)', 'rgb(59, 130, 246)')
            new_content = new_content.replace('var(--accent-green)', 'rgb(59, 130, 246)')
            new_content = new_content.replace('var(--accent-purple)', 'rgb(59, 130, 246)')
            
            # .badge-gagan / .author-badge
            new_content = re.sub(
                r'\.badge-gagan\s*{[^}]+background-color:[^;]+;\n\s*color:[^;]+;',
                '.badge-gagan {\n            display: inline-block;\n            background-color: rgb(59, 130, 246);\n            color: rgb(255, 255, 255);',
                new_content
            )
            
            # Java section number
            new_content = re.sub(
                r'\.section-number\s*{[^}]+background-color:[^;]+;\n\s*color:[^;]+;',
                '.section-number {\n            background-color: rgb(59, 130, 246);\n            color: rgb(255, 255, 255);',
                new_content
            )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Applied blue/white theme to {filepath}")
                
        except Exception as e:
            pass

if __name__ == '__main__':
    apply_blue_white_theme()
