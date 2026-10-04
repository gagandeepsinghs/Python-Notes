import os

source_file = r"e:\My Projects\Notes\full_stack_portal.html"
target_file = r"e:\My Projects\Notes\java\00_master_notes_portal.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace("Full Stack Development | Master Portal", "Java Programming | Master Portal")

# Replace back button link to go correctly to root index.html
content = content.replace('href="index.html"', 'href="../index.html"')

# Replace the grid content
grid_start = content.find('<div class="grid">')
footer_start = content.find('<footer>')

java_card = """
            <!-- Java Programming -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-java" style="color: #ef4444;"></i></span> Java Programming</h2>
                <ul class="links-list">
                    <li><a href="01_java_basics_environment_syntax_notes.html">01. Basics, JVM & Environment</a></li>
                    <li><a href="02_java_controlflow_loops_arrays_notes.html">02. Control Flow, Loops & Arrays</a></li>
                    <li><a href="03_java_oop_pillars_interfaces_packages_notes.html">03. OOP Pillars & Interfaces</a></li>
                    <li><a href="04_java_strings_exceptions_collections_notes.html">04. Strings, Exceptions & Collections</a></li>
                    <li><a href="05_java_generics_object_lambdas_streams_notes.html">05. Generics, Lambdas & Streams</a></li>
                    <li><a href="06_java_datetime_nio_multithreading_concurrency_notes.html">06. DateTime, NIO & Concurrency</a></li>
                    <li><a href="07_java_jvm_jdbc_maven_junit_networking_notes.html">07. JVM, JDBC, Maven & JUnit</a></li>
                    <li><a href="08_modern_java_practice_coding_interview_notes.html">08. Coding & Interview Practice</a></li>
                    <li><a href="00_java_programming_master_notes.html">Java Master Notes</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">More advanced Spring Boot & Java notes are on the way!</p>
            </div>
"""

new_content = content[:grid_start + len('<div class="grid">')] + java_card + """\n        </div>\n    </div>\n\n    """ + content[footer_start:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Java portal successfully recreated.")
