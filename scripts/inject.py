import os, glob

folders = ['C++', 'PHP', 'React', 'full_stack/react', 'java', 'govt', 'notes']
for folder in folders:
    for filepath in glob.glob(f'{folder}/**/*.html', recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if back button already exists
            if '../index.html' not in content and 'master_notes_portal.html' not in content:
                # Find where to inject
                if '<div class="sidebar-header">' in content:
                    btn = '<a href="../index.html" style="display:block; padding:10px; margin-bottom:15px; background:var(--accent-orange, #f97316); color:white; text-decoration:none; text-align:center; border-radius:6px; font-weight:bold;">&larr; Back to Home</a>\n            '
                    content = content.replace('<div class="sidebar-header">', '<div class="sidebar-header">\n            ' + btn)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Fixed sidebar-header {filepath}')
                elif '<div class="sidebar">' in content:
                    btn = '<a href="../index.html" style="display:block; padding:10px; margin-bottom:15px; background:var(--accent-orange, #f97316); color:white; text-decoration:none; text-align:center; border-radius:6px; font-weight:bold;">&larr; Back to Home</a>\n        '
                    content = content.replace('<div class="sidebar">', '<div class="sidebar">\n        ' + btn)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Fixed sidebar {filepath}')
        except Exception as e:
            pass
