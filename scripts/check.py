import os, glob

folders = ['C++', 'PHP', 'React', 'java', 'govt', 'notes', 'full_stack']
for folder in folders:
    for filepath in glob.glob(f'{folder}/**/*.html', recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                has_media = '@media' in content
                has_back = '../index.html' in content
                if not has_media or not has_back:
                    print(f'{filepath}: media={has_media}, back={has_back}')
        except Exception as e:
            print(f'Error reading {filepath}: {e}')
