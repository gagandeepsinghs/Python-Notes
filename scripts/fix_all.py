import os
import glob

# Map folders to their respective master portal file names
portal_map = {
    'C++': 'cpp_programming_master_notes.html',
    'PHP': 'php_programming_master_notes.html',
    'React': 'react_master_notes.html',
    'full_stack/react': 'react_master_notes.html',
    'full_stack/html': 'html_programming_master_notes.html',
    'full_stack/css': 'css_programming_master_notes.html',
    'full_stack/js': 'javascript_programming_master_notes.html',
    'full_stack/node_js': 'index.html', # Might be different, let's just use index.html or check later
    'full_stack/mongo_db': 'index.html',
    'java': 'java_programming_master_notes.html',
    'govt': 'SSC_Master_Notes_Hub.html',
    'notes': 'python_programming_master_notes.html' # Defaulting python notes to python portal
}

# If a file is in this set, it's considered a portal and should link back to main website
known_portals = set()
for folder, p in portal_map.items():
    known_portals.add(p)
    # Some folders have multiple portal files
    known_portals.add('00_master_notes_portal.html')
    known_portals.add('master_notes_portal.html')
    known_portals.add('00_react_master_notes.html')
    known_portals.add('00_php_programming_master_notes.html')
    known_portals.add('00_cpp_programming_master_notes.html')
    known_portals.add('00_html_programming_master_notes.html')
    known_portals.add('00_css_programming_master_notes.html')
    known_portals.add('00_javascript_programming_master_notes.html')

def get_depth(filepath):
    # e.g. "java/file.html" -> 1
    # "full_stack/react/file.html" -> 2
    return len(filepath.replace('\\', '/').split('/')) - 1

def main():
    for folder, portal in portal_map.items():
        if not os.path.isdir(folder):
            continue
        
        # Get all html files
        for filepath in glob.glob(f'{folder}/**/*.html', recursive=True):
            filename = os.path.basename(filepath)
            depth = get_depth(filepath)
            up_path = '../' * depth + 'index.html'
            
            is_portal = filename in known_portals
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Check for standard back button structures
                # E.g. href="../index.html" or href="../../index.html" or href="master_notes_portal.html" etc
                # We'll just do simple string replacements for common href targets.
                
                targets_to_replace = [
                    'href="../index.html"', 
                    'href="../../index.html"',
                    'href="master_notes_portal.html"',
                    'href="00_master_notes_portal.html"'
                ]
                
                # For some java files it's window.location.href='master_notes_portal.html'
                js_targets = [
                    "window.location.href='master_notes_portal.html'",
                    "window.location.href='../index.html'"
                ]
                
                if is_portal:
                    # Point back to main website
                    for t in targets_to_replace:
                        new_content = new_content.replace(t, f'href="{up_path}"')
                    for jt in js_targets:
                        new_content = new_content.replace(jt, f"window.location.href='{up_path}'")
                        
                    new_content = new_content.replace('Back to Modules', 'Back to Main Portal')
                    new_content = new_content.replace('Back to Master Portal', 'Back to Main Portal')
                else:
                    # Point to portal
                    for t in targets_to_replace:
                        if f'href="{portal}"' not in t:
                            new_content = new_content.replace(t, f'href="{portal}"')
                    for jt in js_targets:
                        if f"window.location.href='{portal}'" not in jt:
                            new_content = new_content.replace(jt, f"window.location.href='{portal}'")
                            
                    new_content = new_content.replace('Back to Main Portal', 'Back to Modules')
                    new_content = new_content.replace('Back to Home', 'Back to Modules')
                    
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Fixed hierarchy for: {filepath} (Is Portal: {is_portal})')
                    
            except Exception as e:
                print(f'Error on {filepath}: {e}')

if __name__ == '__main__':
    main()
