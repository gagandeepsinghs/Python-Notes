import re

def combine_grids():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The CSS for the thin cards (modules-grid)
    modules_css = """
    /* --- MODULES GRID CSS --- */
    .modules-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-bottom: 3rem;
    }

    .mod-card {
        background: rgba(20, 20, 20, 0.6);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        text-decoration: none;
        color: white;
        transition: all 0.3s ease;
        position: relative;
        cursor: pointer;
    }

    body.light-theme .mod-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(0,0,0,0.1);
        color: #1a1a1a;
    }

    .mod-card:hover {
        transform: translateY(-3px);
        background: rgba(30, 30, 30, 0.8);
    }
    
    body.light-theme .mod-card:hover {
        background: #ffffff;
    }

    .mod-icon {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    body.light-theme .mod-icon {
        background: rgba(0,0,0,0.03);
        border-color: rgba(0,0,0,0.1);
    }

    .mod-info {
        flex: 1;
    }
    .mod-info h3 {
        font-size: 1.1rem;
        font-weight: 600;
    }

    .mod-open {
        font-size: 0.85rem;
        padding: 6px 14px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.2);
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 5px;
        transition: all 0.3s;
    }
    
    body.light-theme .mod-open {
        border-color: rgba(0,0,0,0.2);
    }
    
    .mod-open i {
        font-size: 0.7rem;
    }

    /* Specific Mod Card Glows */
    .mod-python { border-color: rgba(59, 130, 246, 0.3); box-shadow: inset 0 0 20px rgba(59, 130, 246, 0.05); }
    .mod-python .mod-icon { color: #3b82f6; border-color: rgba(59, 130, 246, 0.4); }
    .mod-python .mod-open { border-color: rgba(59, 130, 246, 0.5); color: #e2e8f0; }

    .mod-java { border-color: rgba(239, 68, 68, 0.3); box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.05); }
    .mod-java .mod-icon { color: #ef4444; border-color: rgba(239, 68, 68, 0.4); }
    .mod-java .mod-open { border-color: rgba(239, 68, 68, 0.5); color: #e2e8f0; }

    .mod-govt { border-color: rgba(255, 255, 255, 0.2); box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.05); }
    .mod-govt .mod-icon { color: #f8fafc; border-color: rgba(255, 255, 255, 0.3); }
    .mod-govt .mod-open { border-color: rgba(255, 255, 255, 0.3); color: #e2e8f0; }
    
    body.light-theme .mod-govt { border-color: rgba(0, 0, 0, 0.2); }
    body.light-theme .mod-govt .mod-icon { color: #333; border-color: rgba(0, 0, 0, 0.2); }
    body.light-theme .mod-govt .mod-open { border-color: rgba(0, 0, 0, 0.2); color: #333; }

    .mod-excel { border-color: rgba(34, 197, 94, 0.3); box-shadow: inset 0 0 20px rgba(34, 197, 94, 0.05); }
    .mod-excel .mod-icon { color: #22c55e; border-color: rgba(34, 197, 94, 0.4); }
    .mod-excel .mod-open { border-color: rgba(34, 197, 94, 0.5); color: #e2e8f0; }

    .mod-pbi { border-color: rgba(234, 179, 8, 0.3); box-shadow: inset 0 0 20px rgba(234, 179, 8, 0.05); }
    .mod-pbi .mod-icon { color: #eab308; border-color: rgba(234, 179, 8, 0.4); }
    .mod-pbi .mod-open { border-color: rgba(234, 179, 8, 0.5); color: #e2e8f0; }

    .mod-sql { border-color: rgba(14, 165, 233, 0.3); box-shadow: inset 0 0 20px rgba(14, 165, 233, 0.05); }
    .mod-sql .mod-icon { color: #0ea5e9; border-color: rgba(14, 165, 233, 0.4); }
    .mod-sql .mod-open { border-color: rgba(14, 165, 233, 0.5); color: #e2e8f0; }

    .mod-other { border-color: rgba(226, 232, 240, 0.2); box-shadow: inset 0 0 20px rgba(226, 232, 240, 0.05); }
    .mod-other .mod-icon { color: #e2e8f0; border-color: rgba(226, 232, 240, 0.3); }
    .mod-other .mod-open { border-color: rgba(226, 232, 240, 0.3); color: #e2e8f0; }
    
    body.light-theme .mod-other { border-color: rgba(0, 0, 0, 0.2); }
    body.light-theme .mod-other .mod-icon { color: #555; border-color: rgba(0, 0, 0, 0.2); }
    body.light-theme .mod-other .mod-open { border-color: rgba(0, 0, 0, 0.2); color: #333; }

    .mod-web { border-color: rgba(56, 189, 248, 0.3); box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.05); }
    .mod-web .mod-icon { color: #38bdf8; border-color: rgba(56, 189, 248, 0.4); }
    .mod-web .mod-open { border-color: rgba(56, 189, 248, 0.5); color: #e2e8f0; }

    .mod-data { border-color: rgba(168, 85, 247, 0.3); box-shadow: inset 0 0 20px rgba(168, 85, 247, 0.05); }
    .mod-data .mod-icon { color: #a855f7; border-color: rgba(168, 85, 247, 0.4); }
    .mod-data .mod-open { border-color: rgba(168, 85, 247, 0.5); color: #e2e8f0; }

    .mod-card:hover .mod-open {
        background: rgba(255,255,255,0.1);
    }
    
    body.light-theme .mod-card .mod-open {
        color: #1a1a1a;
    }

    /* Add hover glows to cards */
    .mod-python:hover { box-shadow: inset 0 0 20px rgba(59, 130, 246, 0.05), 0 0 20px rgba(59, 130, 246, 0.2); }
    .mod-java:hover { box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.05), 0 0 20px rgba(239, 68, 68, 0.2); }
    .mod-govt:hover { box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.05), 0 0 20px rgba(255, 255, 255, 0.1); }
    .mod-excel:hover { box-shadow: inset 0 0 20px rgba(34, 197, 94, 0.05), 0 0 20px rgba(34, 197, 94, 0.2); }
    .mod-pbi:hover { box-shadow: inset 0 0 20px rgba(234, 179, 8, 0.05), 0 0 20px rgba(234, 179, 8, 0.2); }
    .mod-sql:hover { box-shadow: inset 0 0 20px rgba(14, 165, 233, 0.05), 0 0 20px rgba(14, 165, 233, 0.2); }
    .mod-other:hover { box-shadow: inset 0 0 20px rgba(226, 232, 240, 0.05), 0 0 20px rgba(226, 232, 240, 0.1); }
    .mod-web:hover { box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.05), 0 0 20px rgba(56, 189, 248, 0.2); }
    .mod-data:hover { box-shadow: inset 0 0 20px rgba(168, 85, 247, 0.05), 0 0 20px rgba(168, 85, 247, 0.2); }
    
    body.light-theme .mod-govt:hover { box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.05), 0 0 20px rgba(0, 0, 0, 0.1); }
    body.light-theme .mod-other:hover { box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.05), 0 0 20px rgba(0, 0, 0, 0.1); }

    @media (max-width: 1000px) {
        .modules-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 650px) {
        .modules-grid { grid-template-columns: 1fr; }
    }
    
    #detailed-grid-wrapper {
        animation: fadeIn 0.5s ease;
    }
    """

    modules_html = """
        <!-- MODULES GRID -->
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 10px;">
            <i class="fa-solid fa-layer-group" style="color: var(--primary);"></i> Explore Modules
        </h2>
        
        <div class="modules-grid">
            
            <a onclick="showDetailedGrid('python'); return false;" href="#" class="mod-card mod-python">
                <div class="mod-icon"><i class="fa-brands fa-python"></i></div>
                <div class="mod-info"><h3>Python</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>
            
            <a href="java/master_notes_portal.html" class="mod-card mod-java">
                <div class="mod-icon"><i class="fa-brands fa-java"></i></div>
                <div class="mod-info"><h3>Java</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a onclick="showDetailedGrid('govt'); return false;" href="#" class="mod-card mod-govt">
                <div class="mod-icon"><i class="fa-solid fa-building-columns"></i></div>
                <div class="mod-info"><h3>Govt Exams</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

            <a onclick="showDetailedGrid('other'); return false;" href="#" class="mod-card mod-excel">
                <div class="mod-icon"><i class="fa-solid fa-file-excel"></i></div>
                <div class="mod-info"><h3>Excel</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

            <a onclick="showDetailedGrid('other'); return false;" href="#" class="mod-card mod-pbi">
                <div class="mod-icon"><i class="fa-solid fa-chart-simple"></i></div>
                <div class="mod-info"><h3>Power BI</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

            <a onclick="showDetailedGrid('sql'); return false;" href="#" class="mod-card mod-sql">
                <div class="mod-icon"><i class="fa-solid fa-database"></i></div>
                <div class="mod-info"><h3>SQL</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

            <a onclick="showDetailedGrid('other'); return false;" href="#" class="mod-card mod-other">
                <div class="mod-icon"><i class="fa-solid fa-briefcase"></i></div>
                <div class="mod-info"><h3>Other Tools</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

            <a href="full_stack/html/00_master_notes_portal.html" class="mod-card mod-web">
                <div class="mod-icon"><i class="fa-solid fa-globe"></i></div>
                <div class="mod-info"><h3>Web Development</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a onclick="showDetailedGrid('sql'); return false;" href="#" class="mod-card mod-data">
                <div class="mod-icon"><i class="fa-solid fa-chart-line"></i></div>
                <div class="mod-info"><h3>Data Analytics</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-down"></i></div>
            </a>

        </div>
    """

    js_code = """
    <script>
        function showDetailedGrid(category) {
            const wrapper = document.getElementById('detailed-grid-wrapper');
            wrapper.style.display = 'block';
            
            const titleEl = document.getElementById('detailed-grid-title');
            
            const cards = document.querySelectorAll('#detailed-grid-wrapper .card');
            
            cards.forEach(card => {
                const title = card.querySelector('h2').innerText.toLowerCase();
                
                if (category === 'python' && (title.includes('python') || title.includes('master notes') || title.includes('coming'))) {
                    card.style.display = 'flex';
                    titleEl.innerHTML = '<i class="fa-brands fa-python"></i> Python Detailed Notes';
                } else if (category === 'sql' && (title.includes('sql') || title.includes('coming'))) {
                    card.style.display = 'flex';
                    titleEl.innerHTML = '<i class="fa-solid fa-database"></i> SQL & Data Analytics Detailed Notes';
                } else if (category === 'govt' && (title.includes('govt') || title.includes('geography') || title.includes('coming'))) {
                    card.style.display = 'flex';
                    titleEl.innerHTML = '<i class="fa-solid fa-building-columns"></i> Govt Exams Detailed Notes';
                } else if (category === 'other' && (title.includes('other tools') || title.includes('coming'))) {
                    card.style.display = 'flex';
                    titleEl.innerHTML = '<i class="fa-solid fa-toolbox"></i> Other Tools Detailed Notes';
                } else {
                    card.style.display = 'none';
                }
            });

            // Smooth scroll to the wrapper
            setTimeout(() => {
                wrapper.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    </script>
    """

    # Inject CSS
    html = html.replace('</style>', modules_css + '\n</style>')

    # Wrap the original grid in a detailed-grid-wrapper and insert the modules-grid right before it
    # We find `<div class="grid">` which is inside `<div class="container">`
    
    # Let's target the exact injection point.
    # In index.html, it's:
    #     <div class="container">
    #         <div class="grid">
    
    replacement = modules_html + """
        <div id="detailed-grid-wrapper" style="display: none; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <h2 id="detailed-grid-title" style="font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center; gap: 15px; color: var(--primary);">
                <i class="fa-brands fa-python"></i> Detailed Notes
            </h2>
            <div class="grid">
    """
    
    html = html.replace('<div class="grid">', replacement, 1)

    # We need to close the `detailed-grid-wrapper`.
    # It should be closed right after the closing tag of `<div class="grid">`.
    # It's followed by `</div>\n    <footer>`
    
    html = html.replace('</div>\n\n    <footer>', '</div>\n        </div>\n\n    <footer>')
    # If the exact match fails, let's try a regex
    html = re.sub(r'(</div>\s*</div>\s*<footer>)', r'</div>\n\1', html)

    # Inject JS
    html = html.replace('</body>', js_code + '\n</body>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done combining grids!")

if __name__ == '__main__':
    combine_grids()
