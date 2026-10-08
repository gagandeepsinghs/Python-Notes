import os
import glob

def read_file(path):
    for enc in ["utf-8", "utf-16", "latin-1"]:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read(), enc
        except UnicodeDecodeError:
            continue
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(), "utf-8"

def fix_docker_grammar_back():
    root_dir = r"e:\My Projects\Notes"
    files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
    
    for fpath in files:
        rel = os.path.relpath(fpath, root_dir).replace("\\", "/")
        if "Docker" in rel or "120 rules of grammer" in rel:
            content, enc = read_file(fpath)
            if "Back to Home" not in content and "history.back()" not in content:
                dir_name = os.path.dirname(fpath)
                rel_to_root = os.path.relpath(root_dir, dir_name).replace("\\", "/")
                home_link = f"{rel_to_root}/index.html"
                
                back_button_html = f'''
    <div style="position: fixed; top: 15px; left: 15px; z-index: 9999;">
        <a href="{home_link}" style="display: inline-flex; align-items: center; gap: 6px; background: rgba(30, 41, 59, 0.9); color: #ffffff; padding: 8px 14px; border-radius: 8px; text-decoration: none; font-size: 0.85rem; font-weight: 600; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 12px rgba(0,0,0,0.3); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); transition: all 0.2s ease;">
            &larr; Back to Home
        </a>
    </div>
'''
                if "<body" in content:
                    body_idx = content.find(">", content.find("<body")) + 1
                    content = content[:body_idx] + "\n" + back_button_html + content[body_idx:]
                    with open(fpath, "w", encoding=enc) as f:
                        f.write(content)
                    print(f"Added back button to {rel}")

if __name__ == "__main__":
    fix_docker_grammar_back()
