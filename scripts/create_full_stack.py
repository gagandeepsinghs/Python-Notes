import os

# Create full_stack_portal.html based on c_portal.html
with open('c_portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('<div class="grid">')
head_and_top = parts[0] + '<div class="grid">'
footer = text[text.rfind('</div>\n    </div>\n\n    <footer>'):]

fs_cards = '''
            <!-- CSS -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-css3-alt" style="color: #264de4;"></i></span> CSS</h2>
                <ul class="links-list">
                    <li><a href="full_stack/css/00_master_notes_portal.html">CSS Master Notes Portal</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">HTML, JS, React, Node.js, and MongoDB notes are on the way!</p>
            </div>
'''

new_text = head_and_top + '\n' + fs_cards + '\n' + footer
new_text = new_text.replace('<title>C Language | Master Portal</title>', '<title>Full Stack | Master Portal</title>')

# Also update the title in the header if it exists
# "<h1>C <span>Language</span></h1>" -> "<h1>Full <span>Stack</span></h1>"
new_text = new_text.replace('<h1>C <span>Language</span></h1>', '<h1>Full <span>Stack</span></h1>')
new_text = new_text.replace('<p>Your ultimate resource for mastering C programming.</p>', '<p>Your ultimate resource for mastering Full Stack Development.</p>')

with open('full_stack_portal.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('full_stack_portal.html created successfully!')
