import os, glob

fixes = {
    'C++': 'cpp_programming_master_notes.html',
    'PHP': 'php_programming_master_notes.html',
    'React': 'react_master_notes.html',
    'full_stack/react': 'react_master_notes.html'
}

for folder, portal in fixes.items():
    for filepath in glob.glob(f'{folder}/**/*.html', recursive=True):
        if 'master_notes_portal' in filepath or portal in filepath:
            # Maybe the portal itself should go to ../index.html? 
            # Or leave it if we only replace the ones we injected or the ones that had ../index.html
            pass
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            # Replace the back button href we injected or that existed
            if 'href="../index.html"' in new_content:
                new_content = new_content.replace('href="../index.html"', f'href="{portal}"')
            
            # For the ones we injected, we might want to change the text from "Back to Home" to "Back to Modules"
            if '&larr; Back to Home' in new_content:
                new_content = new_content.replace('&larr; Back to Home', '&larr; Back to Modules')
            if 'Back to Home' in new_content: # For PHP files
                new_content = new_content.replace('Back to Home', 'Back to Modules')
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Fixed links in {filepath}')
        except Exception as e:
            print(f'Error reading {filepath}: {e}')
