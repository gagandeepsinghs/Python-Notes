import re
content = open('index.html', encoding='utf-8').read()
matches = re.finditer(r'<a href="([^"]+)"[^>]*>.*?<h2[^>]*>(.*?)<\/h2>', content, re.DOTALL)
for m in matches:
    print(m.group(1), m.group(2).strip().replace('\n', ' '))
