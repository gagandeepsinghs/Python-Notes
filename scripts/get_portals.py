import re
content = open('index.html', encoding='utf-8').read()
links = re.findall(r'href=["\']([^"\']+)["\']', content)
portals = [link for link in links if 'master' in link.lower() or 'portal' in link.lower()]
print(list(set(portals)))
