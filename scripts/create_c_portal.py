with open('python_portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('<div class="grid">')
head_and_top = parts[0] + '<div class="grid">'
footer = text[text.rfind('</div>\n    </div>\n\n    <footer>'):]

c_cards = '''
            <!-- C Basics -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-c"></i></span> C Basics</h2>
                <ul class="links-list">
                    <li><a href="C/01_c_intro_syntax_variables_datatypes_notes.html">Intro, Syntax & Variables</a></li>
                    <li><a href="C/02_c_operators_controlflow_loops_notes.html">Operators & Control Flow</a></li>
                </ul>
            </div>
            
            <!-- Intermediate C -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-layer-group"></i></span> Intermediate C</h2>
                <ul class="links-list">
                    <li><a href="C/03_c_functions_recursion_scope_notes.html">Functions & Recursion</a></li>
                    <li><a href="C/04_c_arrays_strings_pointers_notes.html">Arrays, Strings & Pointers</a></li>
                    <li><a href="C/05_c_structures_unions_enums_notes.html">Structures & Unions</a></li>
                </ul>
            </div>
            
            <!-- Advanced C & DSA -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-brain"></i></span> Advanced C & DSA</h2>
                <ul class="links-list">
                    <li><a href="C/06_c_dynamic_memory_file_io_notes.html">Dynamic Memory & File I/O</a></li>
                    <li><a href="C/07_c_dsa_linkedlists_stacks_queues_notes.html">Linked Lists, Stacks & Queues</a></li>
                    <li><a href="C/08_c_dsa_trees_searching_sorting_notes.html">Trees, Searching & Sorting</a></li>
                </ul>
            </div>
            
            <!-- Master Notes -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-crown"></i></span> Master Notes</h2>
                <ul class="links-list">
                    <li><a href="C/00_c_programming_master_notes.html">C Programming Master Notes</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">More content is on the way!</p>
            </div>
'''

new_text = head_and_top + '\n' + c_cards + '\n' + footer
new_text = new_text.replace('<title>Python Programming | Master Portal</title>', '<title>C Programming | Master Portal</title>')

with open('c_portal.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('c_portal.html created successfully!')
