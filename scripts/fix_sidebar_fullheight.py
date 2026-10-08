import os
import glob
import re

def read_file(path):
    for enc in ["utf-8", "utf-16", "latin-1"]:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read(), enc
        except UnicodeDecodeError:
            continue
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(), "utf-8"

def fix_sidebar_fullheight():
    root_dir = r"e:\My Projects\Notes"
    html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
    
    updated_count = 0
    
    for file_path in html_files:
        content, enc = read_file(file_path)
            
        if ".sidebar" not in content:
            continue
            
        modified = False
        
        # Replace max-height: 40vh in old media queries if present
        if "max-height: 40vh" in content:
            content = content.replace("max-height: 40vh;", "/* max-height: 40vh; */")
            modified = True
            
        # Also let's update the injected mobile CSS for .sidebar to ensure max-height: none !important; and overflow-y: auto !important;
        old_sidebar_css_pattern = r"(\.sidebar\s*\{\s*transform:\s*translateX\(-110%\);[\s\S]*?padding-top:\s*70px\s*!important;\s*\})"
        
        new_sidebar_css = """.sidebar {
                transform: translateX(-110%) !important;
                transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                z-index: 1000 !important;
                width: 280px !important;
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                height: 100vh !important;
                height: 100dvh !important;
                max-height: none !important;
                box-shadow: 4px 0 20px rgba(0,0,0,0.3) !important;
                padding-top: 70px !important;
                overflow-y: auto !important;
                display: block !important;
            }"""
            
        if re.search(old_sidebar_css_pattern, content):
            content = re.sub(old_sidebar_css_pattern, new_sidebar_css, content)
            modified = True
        else:
            if ".sidebar.active" in content and "max-height: none !important;" not in content:
                content = content.replace("height: 100dvh !important;", "height: 100dvh !important;\n                max-height: none !important;\n                overflow-y: auto !important;")
                modified = True
                
        if ".sidebar { width: 260px !important; }" in content:
            content = content.replace(
                ".sidebar { width: 260px !important; }", 
                ".sidebar { width: 260px !important; max-height: none !important; height: 100vh !important; height: 100dvh !important; }"
            )
            modified = True
            
        if modified:
            with open(file_path, "w", encoding=enc) as f:
                f.write(content)
            updated_count += 1

    print(f"Updated {updated_count} files for sidebar full height.")

if __name__ == "__main__":
    fix_sidebar_fullheight()
