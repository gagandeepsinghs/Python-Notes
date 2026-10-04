import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The wrapper starts at <div id="detailed-grid-wrapper" and ends before <footer>
html = re.sub(r'<div id="detailed-grid-wrapper".*?(?=<footer>)', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Removed detailed grid from index.html")
