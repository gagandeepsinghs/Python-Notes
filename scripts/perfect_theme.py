import os
import glob
import re

def fix_css():
    files = glob.glob('**/*.html', recursive=True)
    
    for filepath in files:
        if 'python_programming_master_notes' in filepath or 'index.html' == filepath:
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            
            # --- Fix Java Files specifically ---
            if 'java' in filepath:
                # Header Gradient
                new_content = re.sub(
                    r'background:\s*linear-gradient\([^)]+\);',
                    'background: linear-gradient(135deg, rgb(24, 24, 27) 0%, rgb(39, 39, 42) 100%);',
                    new_content
                )
                
                # Header h1 color to white
                new_content = re.sub(
                    r'\.header h1\s*{[^}]+color:\s*var\(--accent-blue\);',
                    '.header h1 {\n            color: rgb(255, 255, 255);',
                    new_content
                )
                
                # section title color to white
                new_content = re.sub(
                    r'\.section-title\s*{[^}]+color:\s*var\(--accent-blue\);',
                    '.section-title {\n            color: rgb(255, 255, 255);',
                    new_content
                )
                new_content = re.sub(
                    r'\.section-title\s*{[^}]+color:\s*var\(--text-primary\);',
                    '.section-title {\n            color: rgb(255, 255, 255);',
                    new_content
                )
                
                # nav-back button to match python theme outline button
                new_content = re.sub(
                    r'\.nav-back\s*{[^}]+}',
                    '.nav-back {\n            color: rgb(212, 212, 216);\n            text-decoration: none;\n            font-weight: 500;\n            display: flex;\n            align-items: center;\n            gap: 6px;\n            cursor: pointer;\n            font-size: 0.9rem;\n            background: transparent;\n            border: 1px solid rgb(39, 39, 42);\n            padding: 6px 12px;\n            border-radius: 4px;\n            transition: all 0.2s;\n        }\n        .nav-back:hover {\n            background: rgb(39, 39, 42);\n            color: white;\n        }',
                    new_content
                )
                
                # Replace java's hardcoded text color for 'Created by Gagan Sir'
                new_content = new_content.replace('color: var(--accent-purple)', 'color: rgb(161, 161, 170)')
                
                # Badges (like Author badge)
                new_content = re.sub(
                    r'\.author-badge\s*{[^}]+}',
                    '.author-badge {\n            display: inline-block;\n            background: rgb(59, 130, 246);\n            color: rgb(255, 255, 255);\n            padding: 5px 14px;\n            border-radius: 20px;\n            font-weight: 600;\n            margin-top: 12px;\n            font-size: 0.88rem;\n        }',
                    new_content
                )
                
                # nav-bar background
                new_content = re.sub(
                    r'\.nav-bar\s*{[^}]+background:[^;]+;',
                    '.nav-bar {\n            background: rgb(18, 18, 20);',
                    new_content
                )
                
            # --- Fix C++, React, PHP, full_stack Files ---
            else:
                # header card gradient
                new_content = re.sub(
                    r'\.header-card\s*{[^}]+background:[^;]+;',
                    '.header-card {\n            background: linear-gradient(135deg, rgb(24, 24, 27) 0%, rgb(39, 39, 42) 100%);',
                    new_content
                )
                
                # Sidebar background
                new_content = re.sub(
                    r'\.sidebar\s*{[^}]+background-color:[^;]+;',
                    '.sidebar {\n            background-color: rgb(18, 18, 20);',
                    new_content
                )
                
                # Fix sidebar header title
                new_content = re.sub(
                    r'\.sidebar-title\s*{[^}]+color:[^;]+;',
                    '.sidebar-title {\n            color: rgb(255, 255, 255);',
                    new_content
                )
                
                # Fix module cards
                new_content = re.sub(
                    r'\.module-card h2\s*{[^}]+color:[^;]+;',
                    '.module-card h2 {\n            color: rgb(255, 255, 255);',
                    new_content
                )
                
            # --- Global Fixes for injected Back buttons (inline styles) ---
            new_content = re.sub(
                r'<a href="\.\./index\.html" style="display:block; padding:10px; margin-bottom:15px; background:rgb\(59, 130, 246\); color:white; text-decoration:none; text-align:center; border-radius:6px; font-weight:bold;">',
                '<a href="../index.html" class="nav-link" style="border: 1px solid rgb(39, 39, 42); text-align: center; margin-bottom: 15px; color: rgb(212, 212, 216); display: block; padding: 8px; border-radius: 4px; text-decoration: none;">',
                new_content
            )
            # Handle variations of the back button I might have injected
            new_content = re.sub(
                r'<a href="\.\./index\.html"[^>]*background[^>]*>&larr; Back to Main Portal</a>',
                '<a href="../index.html" style="border: 1px solid rgb(39, 39, 42); text-align: center; margin-bottom: 15px; color: rgb(212, 212, 216); display: block; padding: 8px; border-radius: 4px; text-decoration: none;">&larr; Back to Main Portal</a>',
                new_content
            )

            # Enforce H1 colors
            new_content = new_content.replace('color: var(--accent-blue);', 'color: rgb(255, 255, 255);')
            new_content = new_content.replace('color: rgb(59, 130, 246);', 'color: rgb(255, 255, 255);')
            
            # EXCEPT for the author badge, which SHOULD be blue
            # We handled author badge in Java, what about C++?
            new_content = new_content.replace('class="brand-badge"', 'class="badge-gagan" style="background-color: rgb(59, 130, 246); color: rgb(255, 255, 255);"')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Perfected theme for {filepath}")
                
        except Exception as e:
            pass

if __name__ == '__main__':
    fix_css()
