import os

portal_file = "database_portal.html"
with open(portal_file, "r", encoding="utf-8") as f:
    content = f.read()

# Update title
content = content.replace("Other Tools | Master Portal", "Database | Master Portal")

# Replace Other Tools card with SQL and MongoDB
old_card = """            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-toolbox"></i></span> Other Tools</h2>
                <ul class="links-list">
                    <li><a href="notes/excel_complete_notes.html">Excel Complete Notes</a></li>
                    <li><a href="notes/powerbi_complete_notes.html">PowerBI Complete Notes</a></li>
                    <li><a href="notes/flask-tutorial.html">Flask Tutorial</a></li>
                </ul>
            </div>"""

new_cards = """            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-database"></i></span> SQL & Data</h2>
                <ul class="links-list">
                    <li><a href="database/SQL/sql_portal.html">SQL Master Portal</a></li>
                </ul>
            </div>
            
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-leaf"></i></span> MongoDB</h2>
                <ul class="links-list">
                    <li><a href="database/MongoDB/00_master_notes_portal.html">MongoDB Master Notes</a></li>
                </ul>
            </div>"""

content = content.replace(old_card, new_cards)

with open(portal_file, "w", encoding="utf-8") as f:
    f.write(content)


# Now update index.html to point to database_portal.html
index_file = "index.html"
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# The current SQL card in index.html is:
old_sql_card = """            <a href="database/SQL/sql_portal.html" class="mod-card mod-sql">
                <div class="mod-icon"><i class="fa-solid fa-database"></i></div>
                <div class="mod-info"><h3>SQL</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>"""

new_db_card = """            <a href="database_portal.html" class="mod-card mod-database">
                <div class="mod-icon"><i class="fa-solid fa-server"></i></div>
                <div class="mod-info"><h3>Database</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>"""

index_content = index_content.replace(old_sql_card, new_db_card)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_content)
