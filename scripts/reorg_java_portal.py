import os

file_path = r"e:\My Projects\Notes\java\00_master_notes_portal.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything between <div class="grid"> and </div>\n    </div>
start_str = '<div class="grid">'
end_str = '        </div>\n    </div>'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_grid_content = """<div class="grid">
            
            <!-- Java Basics -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-java" style="color: #ef4444;"></i></span> Java Basics</h2>
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

"""
    new_content = content[:start_idx] + new_grid_content + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Java portal successfully reorganized into multi-column cards.")
else:
    print("Could not find grid bounds.")
