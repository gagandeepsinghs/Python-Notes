import os

# 1. Create cpp_portal.html based on c_portal.html
with open('c_portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('<div class="grid">')
head_and_top = parts[0] + '<div class="grid">'
footer = text[text.rfind('</div>\n    </div>\n\n    <footer>'):]

cpp_cards = '''
            <!-- C++ Basics -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-code"></i></span> C++ Basics</h2>
                <ul class="links-list">
                    <li><a href="C++/01_cpp_intro_syntax_variables_datatypes_notes.html">Intro, Syntax & Variables</a></li>
                    <li><a href="C++/02_cpp_operators_controlflow_loops_notes.html">Operators & Control Flow</a></li>
                </ul>
            </div>
            
            <!-- OOP in C++ -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-cubes"></i></span> Object-Oriented</h2>
                <ul class="links-list">
                    <li><a href="C++/03_cpp_functions_defaultargs_overloading_recursion_notes.html">Functions & Recursion</a></li>
                    <li><a href="C++/04_cpp_oop_classes_objects_constructors_destructors_notes.html">Classes & Objects</a></li>
                    <li><a href="C++/05_cpp_oop_inheritance_polymorphism_virtual_notes.html">Inheritance & Polymorphism</a></li>
                </ul>
            </div>
            
            <!-- C++ STL & DSA -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-brain"></i></span> STL & Advanced</h2>
                <ul class="links-list">
                    <li><a href="C++/06_cpp_stl_vectors_strings_maps_sets_notes.html">STL Vectors, Maps & Sets</a></li>
                    <li><a href="C++/07_cpp_stl_stacks_queues_algorithms_notes.html">STL Stacks, Queues & Algorithms</a></li>
                    <li><a href="C++/08_cpp_dsa_linkedlists_trees_graphs_notes.html">DSA: Linked Lists, Trees & Graphs</a></li>
                </ul>
            </div>
            
            <!-- Master Notes -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-crown"></i></span> Master Notes</h2>
                <ul class="links-list">
                    <li><a href="C++/cpp_programming_master_notes.html">C++ Programming Master Notes</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">More content is on the way!</p>
            </div>
'''

new_text = head_and_top + '\n' + cpp_cards + '\n' + footer
new_text = new_text.replace('<title>C Language | Master Portal</title>', '<title>C++ Language | Master Portal</title>')

with open('cpp_portal.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('cpp_portal.html created successfully!')
