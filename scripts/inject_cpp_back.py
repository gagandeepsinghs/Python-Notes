import glob
cpp_html = glob.glob('C++/*.html')

count = 0
for f in cpp_html:
    if 'portal' in f or 'master' in f:
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    back_button_html = '<a href="../cpp_portal.html" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #3b82f6; cursor: pointer;">← Back to Portal</a>'
    
    # Check if back button is already injected but points to index.html
    old_back_button_html = '<a href="../index.html" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #3b82f6; cursor: pointer;">← Back to Portal</a>'
    
    if old_back_button_html in content:
        new_content = content.replace(old_back_button_html, back_button_html)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        continue
        
    if back_button_html in content:
        continue

    
    if '<div class="sidebar-header">' in content:
        new_content = content.replace(
            '<div class="sidebar-header">',
            f'<div class="sidebar-header">\n            {back_button_html}'
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        
print(f'Injected back button in {count} C++ files')
