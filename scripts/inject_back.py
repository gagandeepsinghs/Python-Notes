import glob
import re
import os

# 1. Map each notes file to its portal
file_to_portal = {}

portals = glob.glob('*_portal.html')
portals.append('index.html') # Some might link back to index
# But wait, java is java/master_notes_portal.html
portals.append('java/master_notes_portal.html')
portals.append('full_stack/html/00_master_notes_portal.html')

for portal in portals:
    if not os.path.exists(portal): continue
    
    with open(portal, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Simple regex to find href="path/to/file.html"
    links = re.findall(r'href=[\'"]([^\'"]+\.html)[\'"]', content)
    
    portal_basename = os.path.basename(portal)
    # If portal is in a subfolder, links inside it are relative to that subfolder,
    # but for root portals, links are relative to root.
    
    for link in set(links):
        if link == 'index.html' or 'portal' in link:
            continue
            
        # The link is relative to the portal's directory
        portal_dir = os.path.dirname(portal)
        full_path = os.path.normpath(os.path.join(portal_dir, link)).replace('\\', '/')
        
        # Calculate the relative path FROM the note file TO the portal file
        # e.g., if note is C/01_notes.html and portal is c_portal.html
        # portal_rel_path = '../c_portal.html'
        
        note_dir = os.path.dirname(full_path)
        if note_dir == '':
            portal_rel_path = portal_basename
        else:
            # simple calculation: how many directories deep?
            depth = len(note_dir.split('/'))
            if portal_dir == '':
                portal_rel_path = '../' * depth + portal_basename
            else:
                # Both in subdirectories? Not fully generic but works for our case
                if note_dir == portal_dir:
                    portal_rel_path = portal_basename
                else:
                    portal_rel_path = '../' * depth + portal

        file_to_portal[full_path] = portal_rel_path

# 2. Inject the back button into every mapped note file
count = 0
for note_path, back_link in file_to_portal.items():
    if not os.path.exists(note_path):
        continue
        
    with open(note_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Check if a back button already exists
    if 'Back to Portal' in content or 'Back to Module' in content:
        # maybe we replace the old one?
        pass

    # The sidebar header looks like:
    # <div class="sidebar-header">
    #     <span class="brand-badge">Created by Gagan Sir</span>
    
    back_button_html = f'''<a href="{back_link}" class="brand-badge" style="display: block; text-align: center; text-decoration: none; margin-bottom: 10px; background-color: #3b82f6; cursor: pointer;">← Back to Portal</a>'''
    
    if back_button_html in content:
        continue
        
    if '<div class="sidebar-header">' in content:
        # Insert right after
        new_content = content.replace(
            '<div class="sidebar-header">',
            f'<div class="sidebar-header">\n            {back_button_html}'
        )
        
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
    elif '<div class="sidebar-logo">' in content:
        new_content = content.replace(
            '<div class="sidebar-logo">',
            f'<div class="sidebar-logo">\n            {back_button_html}'
        )
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Injected back buttons into {count} note files.")
