with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS
cpp_css = '''
    .mod-cpp { border-color: rgba(6, 182, 212, 0.3); box-shadow: inset 0 0 20px rgba(6, 182, 212, 0.05); }
    .mod-cpp .mod-icon { color: #06b6d4; border-color: rgba(6, 182, 212, 0.4); }
    .mod-cpp .mod-open { border-color: rgba(6, 182, 212, 0.5); color: #e2e8f0; }
'''

if '.mod-cpp {' not in text:
    text = text.replace('.mod-c {', cpp_css.strip() + '\n\n    .mod-c {', 1)

cpp_hover_css = '''    .mod-cpp:hover { box-shadow: inset 0 0 20px rgba(6, 182, 212, 0.05), 0 0 20px rgba(6, 182, 212, 0.2); }'''
if '.mod-cpp:hover' not in text:
    text = text.replace('    .mod-c:hover {', cpp_hover_css + '\n    .mod-c:hover {', 1)

# 2. Add Button
cpp_card = '''
            <a href="cpp_portal.html" class="mod-card mod-cpp">
                <div class="mod-icon"><i class="fa-solid fa-code"></i></div>
                <div class="mod-info"><h3>C++ Language</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>
'''

if 'cpp_portal.html' not in text:
    target = '            <a href="c_portal.html" class="mod-card mod-c">'
    text = text.replace(target, cpp_card.strip() + '\n\n' + target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html successfully')
