import os
import re

def create_portals():
    # Read original index.html which is UTF-16
    with open('original_index.html', 'r', encoding='utf-16') as f:
        original_html = f.read()
    
    python_titles = ["Python Basics", "Control Flow", "Data Structures", "Functions & Errors", "Advanced Modules", "Master Notes", "Coming Soon"]
    sql_titles = ["SQL & Data", "Data Analytics", "Coming Soon"]
    govt_titles = ["Govt Master Notes", "Govt Polity", "Geography & GK", "Coming Soon"]
    other_titles = ["Other Tools", "Coming Soon"]
    
    def extract_cards(titles):
        cards_html = ""
        card_matches = re.finditer(r'(<!--.*?-->\s*)?<div class="card".*?>.*?</div>', original_html, re.DOTALL)
        for match in card_matches:
            card_html = match.group(0)
            title_match = re.search(r'<h2>.*?</h2>', card_html, re.DOTALL)
            if title_match:
                title_text = re.sub(r'<[^>]+>', '', title_match.group(0)).strip()
                if any(t in title_text for t in titles):
                    cards_html += card_html + "\n            "
        return cards_html

    def generate_portal_html(portal_name, page_title, cards_html):
        new_html = re.sub(r'<div class="grid">.*?</div>\n    </div>', f'<div class="grid">\n            {cards_html}\n        </div>\n    </div>', original_html, flags=re.DOTALL)
        new_html = new_html.replace('<title>Python with Gagan Sir | Master Portal</title>', f'<title>{page_title} | Master Portal</title>')
        back_btn = f"""
        <div style="position: absolute; top: 20px; left: 20px; z-index: 100;">
            <a href="index.html" style="background: var(--primary); color: #000; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; font-family: 'Outfit', sans-serif;"><i class="fa-solid fa-arrow-left"></i> Back to Home</a>
        </div>
        """
        new_html = new_html.replace('<header>', f'<header>{back_btn}')
        new_html = re.sub(r'<h1 class="hero-title">.*?</h1>', f'<h1 class="hero-title">{page_title}</h1>', new_html)
        with open(portal_name, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
    generate_portal_html('python_portal.html', 'Python Programming', extract_cards(python_titles))
    generate_portal_html('sql_portal.html', 'SQL & Data Analytics', extract_cards(sql_titles))
    generate_portal_html('govt_portal.html', 'Govt Exams Notes', extract_cards(govt_titles))
    generate_portal_html('other_portal.html', 'Other Tools & Notes', extract_cards(other_titles))
    
    print("Portals created!")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_html = f.read()
        
    idx_html = re.sub(r'<div id="detailed-grid-wrapper".*?<!-- Chatbot Floating Button -->', '<!-- Chatbot Floating Button -->', idx_html, flags=re.DOTALL)
    idx_html = re.sub(r'<script>\s*function showDetailedGrid.*?</script>', '', idx_html, flags=re.DOTALL)
    
    idx_html = idx_html.replace("onclick=\"showDetailedGrid('python'); return false;\" href=\"#\"", 'href="python_portal.html"')
    idx_html = idx_html.replace("onclick=\"showDetailedGrid('sql'); return false;\" href=\"#\"", 'href="sql_portal.html"')
    idx_html = idx_html.replace("onclick=\"showDetailedGrid('govt'); return false;\" href=\"#\"", 'href="govt_portal.html"')
    idx_html = idx_html.replace("onclick=\"showDetailedGrid('other'); return false;\" href=\"#\"", 'href="other_portal.html"')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_html)
        
    print("index.html updated to use separate pages!")

if __name__ == '__main__':
    create_portals()
