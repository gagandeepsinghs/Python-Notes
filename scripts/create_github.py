with open('python_portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('<div class="grid">')
head_and_top = parts[0] + '<div class="grid">'
footer = text[text.rfind('</div>\n    </div>\n\n    <footer>'):]

github_cards = '''
            <!-- Git & GitHub -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-github"></i></span> Git & GitHub</h2>
                <ul class="links-list">
                    <li><a href="notes/git_github_master_notes.html">Git & GitHub Master Notes</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">More content is on the way!</p>
            </div>
'''

new_text = head_and_top + '\n' + github_cards + '\n' + footer
new_text = new_text.replace('<title>Python Programming | Master Portal</title>', '<title>Git & GitHub | Master Portal</title>')

with open('github_portal.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('github_portal.html created successfully!')
