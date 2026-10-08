import os

PROJECT_ROOT = r"e:\My Projects\Notes"

SEARCH_STR = """                box-shadow: 4px 0 20px rgba(0,0,0,0.3);
            }
            .sidebar.active {"""

REPLACE_STR = """                box-shadow: 4px 0 20px rgba(0,0,0,0.3);
                padding-top: 70px !important;
            }
            .sidebar.active {"""

def main():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
        # Skip .git and scripts directories
        dirnames[:] = [d for d in dirnames if d not in ['.git', 'node_modules', 'backups']]
        for fname in filenames:
            if fname.endswith('.html'):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if SEARCH_STR in content:
                        new_content = content.replace(SEARCH_STR, REPLACE_STR)
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        fixed += 1
                        print(f"Fixed padding in {fpath}")
                except Exception as e:
                    print(f"Error reading {fpath}: {e}")

    print(f"Total files updated: {fixed}")

if __name__ == '__main__':
    main()
