import os
import glob

PORTALS = {
    'java': 'master_notes_portal.html',
    'C++': 'master_notes_portal.html',
    'React': 'master_notes_portal.html',
    'PHP': 'php_programming_master_notes.html',
    'notes': 'python_programming_master_notes.html',
    'full_stack/css': 'css_programming_master_notes.html',
    'full_stack/html': 'html_programming_master_notes.html',
    'full_stack/js': 'javascript_programming_master_notes.html',
    'full_stack/react': 'master_notes_portal.html',
    'govt': 'SSC_Master_Notes_Hub.html'
}

def get_portal_for_dir(filepath):
    # Normalize path
    filepath = filepath.replace('\\', '/')
    for k, v in PORTALS.items():
        if filepath.startswith(k + '/'):
            # Make sure it actually exists
            if os.path.exists(os.path.join(k, v)):
                return v
            elif os.path.exists(os.path.join(k, '00_' + v)):
                return '00_' + v
            elif os.path.exists(os.path.join(k, 'master_notes_portal.html')):
                return 'master_notes_portal.html'
            elif os.path.exists(os.path.join(k, '00_master_notes_portal.html')):
                return '00_master_notes_portal.html'
            return v
    return None

def run():
    files = glob.glob('**/*.html', recursive=True)
    count = 0
    for filepath in files:
        # Normalize
        normalized_path = filepath.replace('\\', '/')
        portal_file = get_portal_for_dir(normalized_path)
        
        if not portal_file:
            continue
            
        # We don't want to change the back button OF the portal file itself
        # Or at least, the portal file's back button should go to ../index.html or ../../index.html
        if os.path.basename(normalized_path) in [portal_file, '00_' + portal_file, 'master_notes_portal.html', '00_master_notes_portal.html'] or 'master' in os.path.basename(normalized_path):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            # Replace the onclick attribute
            if 'onclick="window.location.href=\'../index.html\'"' in new_content:
                new_content = new_content.replace(
                    'onclick="window.location.href=\'../index.html\'"',
                    f'onclick="window.location.href=\'{portal_file}\'"'
                )
            
            if 'onclick="window.location.href=\'../../index.html\'"' in new_content:
                new_content = new_content.replace(
                    'onclick="window.location.href=\'../../index.html\'"',
                    f'onclick="window.location.href=\'{portal_file}\'"'
                )

            # Replace the href attribute for sidebar
            if 'href="../index.html"' in new_content:
                new_content = new_content.replace(
                    'href="../index.html"',
                    f'href="{portal_file}"'
                )
                
            if 'href="../../index.html"' in new_content:
                new_content = new_content.replace(
                    'href="../../index.html"',
                    f'href="{portal_file}"'
                )
                
            # Replace the text to be appropriate
            new_content = new_content.replace('← Back to Main Portal', '← Back to Module Portal')
            new_content = new_content.replace('&larr; Back to Home', '&larr; Back to Module')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated back button in {filepath} to point to {portal_file}")
                count += 1
        except Exception as e:
            pass
            
    print(f"Updated back button in {count} files.")

if __name__ == '__main__':
    run()
