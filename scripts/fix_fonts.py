import glob

def fix_fonts():
    files = glob.glob('**/*.html', recursive=True)
    count = 0
    
    replacements = {
        '--text-primary: rgb(18, 18, 20);': '--text-primary: rgb(244, 244, 245);',
        '--text-primary: rgb(24, 24, 27);': '--text-primary: rgb(244, 244, 245);',
        '--text-main: rgb(18, 18, 20);': '--text-main: rgb(244, 244, 245);',
        
        # master_notes_portal.html specific
        '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(24, 24, 27);': '.portal-header {\n            background-color: var(--bg-sidebar);\n            color: rgb(244, 244, 245);',
        '.master-banner {\n            background: linear-gradient(135deg, rgb(18, 18, 20) 0%, rgb(59, 130, 246) 100%);\n            border-radius: 12px;\n            padding: 28px 32px;\n            color: rgb(24, 24, 27);': '.master-banner {\n            background: linear-gradient(135deg, rgb(18, 18, 20) 0%, rgb(59, 130, 246) 100%);\n            border-radius: 12px;\n            padding: 28px 32px;\n            color: rgb(244, 244, 245);',
        '.btn-card {\n            display: block;\n            text-align: center;\n            background-color: rgb(18, 18, 20);\n            color: rgb(24, 24, 27);': '.btn-card {\n            display: block;\n            text-align: center;\n            background-color: rgb(18, 18, 20);\n            color: rgb(244, 244, 245);',
        '.btn-card:hover {\n            background-color: rgb(255, 255, 255);\n        }': '.btn-card:hover {\n            background-color: rgb(255, 255, 255);\n            color: rgb(24, 24, 27);\n        }',
        
        # individual notes page specific
        '.sidebar h2 {\n            font-size: 1.15rem;\n            margin-bottom: 5px;\n            color: rgb(24, 24, 27);': '.sidebar h2 {\n            font-size: 1.15rem;\n            margin-bottom: 5px;\n            color: rgb(244, 244, 245);',
        '.header-card h1 {\n            font-size: 2.3rem;\n            color: rgb(24, 24, 27);': '.header-card h1 {\n            font-size: 2.3rem;\n            color: rgb(244, 244, 245);',
        '.badge-gagan {\n            display: inline-block;\n            background-color: var(--accent-color);\n            color: rgb(24, 24, 27);': '.badge-gagan {\n            display: inline-block;\n            background-color: var(--accent-color);\n            color: rgb(244, 244, 245);',
        '.section-title {\n            font-size: 1.45rem;\n            color: rgb(24, 24, 27);': '.section-title {\n            font-size: 1.45rem;\n            color: rgb(244, 244, 245);',
        
        # Fix tag-btn which relies on --text-primary but has a light background
        '.tag-btn {\n            background-color: rgb(241, 245, 249);\n            color: var(--text-primary);': '.tag-btn {\n            background-color: rgb(241, 245, 249);\n            color: rgb(24, 24, 27);',
    }
    
    # We should also handle more flexible replacements in case spacing is different
    # But since these are generated/copied, spacing is likely identical.
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # Simple direct replacements
            for k, v in replacements.items():
                new_content = new_content.replace(k, v)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed fonts in {filepath}")
        except Exception as e:
            pass
            
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    fix_fonts()
