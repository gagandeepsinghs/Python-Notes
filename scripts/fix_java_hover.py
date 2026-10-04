import os
import re

file_path = r"e:\My Projects\Notes\java\00_master_notes_portal.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's completely replace the body content starting from the floating icons to the footer.
# But actually, the issue is from the first Back to Home button.
start_cut = content.find('<div style="position: absolute; top: 20px; left: 20px; z-index: 100;">')
footer_start = content.find('<footer>')

if start_cut != -1 and footer_start != -1:
    clean_html = """    <div style="position: absolute; top: 20px; left: 20px; z-index: 100;">
        <a href="../index.html" style="background: var(--primary); color: #000; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; font-family: 'Outfit', sans-serif;"><i class="fa-solid fa-arrow-left"></i> Back to Home</a>
    </div>

    <div class="container" style="max-width: 95%; padding-top: 100px;">
        <div class="grid">
            
            <!-- Java Basics -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-java"></i></span> Java Basics</h2>
                <ul class="links-list">
                    <li><a href="01_java_basics_environment_syntax_notes.html">01. Basics, JVM & Environment</a></li>
                    <li><a href="02_java_controlflow_loops_arrays_notes.html">02. Control Flow, Loops & Arrays</a></li>
                </ul>
            </div>

            <!-- OOP & Data Structures -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-cubes"></i></span> OOP & Collections</h2>
                <ul class="links-list">
                    <li><a href="03_java_oop_pillars_interfaces_packages_notes.html">03. OOP Pillars & Interfaces</a></li>
                    <li><a href="04_java_strings_exceptions_collections_notes.html">04. Strings, Exceptions & Collections</a></li>
                    <li><a href="05_java_generics_object_lambdas_streams_notes.html">05. Generics, Lambdas & Streams</a></li>
                </ul>
            </div>

            <!-- Advanced Java -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-server"></i></span> Advanced Java</h2>
                <ul class="links-list">
                    <li><a href="06_java_datetime_nio_multithreading_concurrency_notes.html">06. DateTime, NIO & Concurrency</a></li>
                    <li><a href="07_java_jvm_jdbc_maven_junit_networking_notes.html">07. JVM, JDBC, Maven & JUnit</a></li>
                </ul>
            </div>

            <!-- Practice & Master Manual -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-code"></i></span> Practice & Manual</h2>
                <ul class="links-list">
                    <li><a href="08_modern_java_practice_coding_interview_notes.html">08. Coding & Interview Practice</a></li>
                    <li><a href="00_java_programming_master_notes.html">Java Master Notes</a></li>
                </ul>
            </div>

        </div>
    </div>

    """
    
    new_content = content[:start_cut] + clean_html + content[footer_start:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Java portal layout fixed and hover effects restored.")
else:
    print("Could not find start_cut or footer_start")
