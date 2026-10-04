with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# CSS for C Programming
c_css = '''
    .mod-c { border-color: rgba(99, 102, 241, 0.3); box-shadow: inset 0 0 20px rgba(99, 102, 241, 0.05); }
    .mod-c .mod-icon { color: #6366f1; border-color: rgba(99, 102, 241, 0.4); }
    .mod-c .mod-open { border-color: rgba(99, 102, 241, 0.5); color: #e2e8f0; }
    .mod-c:hover { box-shadow: inset 0 0 20px rgba(99, 102, 241, 0.05), 0 0 20px rgba(99, 102, 241, 0.2); }
'''

if '.mod-c {' not in text:
    text = text.replace('.mod-java:hover {', c_css.strip() + '\n    .mod-java:hover {', 1)

# Card HTML
c_card = '''
            <a href="c_portal.html" class="mod-card mod-c">
                <div class="mod-icon"><i class="fa-solid fa-c"></i></div>
                <div class="mod-info"><h3>C Programming</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>
'''

if 'c_portal.html' not in text:
    target = '            <a href="java_portal.html" class="mod-card mod-java">'
    text = text.replace(target, c_card.strip() + '\n\n' + target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
