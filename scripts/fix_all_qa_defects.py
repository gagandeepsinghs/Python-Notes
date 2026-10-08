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

def fix_all_qa():
    root_dir = r"e:\My Projects\Notes"
    html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
    html_files = [f for f in html_files if "backups" not in f and "node_modules" not in f]
    
    # Map of filename -> list of relative paths from root
    file_map = {}
    for f in html_files:
        rel = os.path.relpath(f, root_dir).replace("\\", "/")
        fname = os.path.basename(f).lower()
        if fname not in file_map:
            file_map[fname] = []
        file_map[fname].append(rel)
        
    print(f"=== COMPREHENSIVE QA FIXER FOR {len(html_files)} FILES ===")
    
    links_fixed = 0
    back_buttons_added = 0
    touch_handlers_added = 0
    
    for file_path in html_files:
        rel_file = os.path.relpath(file_path, root_dir).replace("\\", "/")
        dir_name = os.path.dirname(file_path)
        content, enc = read_file(file_path)
        modified = False
        
        # Calculate depth to root
        rel_to_root = os.path.relpath(root_dir, dir_name).replace("\\", "/")
        if rel_to_root == ".":
            home_link = "index.html"
        else:
            home_link = f"{rel_to_root}/index.html"
            
        # 1. FIX BROKEN HREFS
        def replace_href(match):
            nonlocal modified, links_fixed
            full_match = match.group(0)
            quote = match.group(1)
            href = match.group(2)
            
            if href.startswith("#") or href.startswith("javascript:") or href.startswith("http") or href.startswith("mailto:") or href.startswith("https:"):
                return full_match
                
            clean_href = href.split("?")[0].split("#")[0]
            if not clean_href:
                return full_match
                
            target_path = os.path.normpath(os.path.join(dir_name, clean_href))
            if os.path.exists(target_path):
                return full_match
                
            target_fname = os.path.basename(clean_href).lower()
            
            # Specific known broken link fixes
            if target_fname == "05_dbms_and_data_structures.html":
                new_href = href.replace("05_DBMS_and_Data_Structures.html", "05_Programming_and_Modern_Tech.html")
                modified = True
                links_fixed += 1
                return f'href={quote}{new_href}{quote}'
            elif target_fname == "00_cpp_programming_master_notes.html":
                new_href = href.replace("00_cpp_programming_master_notes.html", "cpp_programming_master_notes.html")
                modified = True
                links_fixed += 1
                return f'href={quote}{new_href}{quote}'
            elif target_fname == "index.html":
                # Fix relative depth to index.html
                new_href = home_link
                if new_href != href:
                    modified = True
                    links_fixed += 1
                    return f'href={quote}{new_href}{quote}'
            elif target_fname in file_map:
                # Find best matching relative path
                possible_rels = file_map[target_fname]
                best_target = possible_rels[0]
                new_rel = os.path.relpath(os.path.join(root_dir, best_target), dir_name).replace("\\", "/")
                modified = True
                links_fixed += 1
                return f'href={quote}{new_rel}{quote}'
                
            return full_match

        content = re.sub(r'href=(["\'])([^"\']+)\1', replace_href, content)
        
        # 2. INJECT BACK BUTTON IF MISSING
        if rel_file not in ["index.html", "govt_portal.html", "database_portal.html"]:
            has_back = ("Back to Home" in content or "history.back()" in content or "back-btn" in content or "Back" in content)
            if not has_back:
                # Inject floating top-left Back button
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
                    modified = True
                    back_buttons_added += 1

        # 3. INJECT TOUCH HANDLERS FOR SIDEBAR IF MISSING
        if ".sidebar" in content and "touchstart" not in content and "sidebarToggle" in content:
            touch_js = """
    <script>
    (function() {
        var toggle = document.getElementById('sidebarToggle');
        var overlay = document.getElementById('sidebarOverlay');
        var sidebar = document.querySelector('.sidebar');
        if (!toggle || !sidebar) return;
        function openSidebar() { sidebar.classList.add('active'); if(overlay) overlay.classList.add('active'); }
        function closeSidebar() { sidebar.classList.remove('active'); if(overlay) overlay.classList.remove('active'); }
        toggle.addEventListener('touchstart', function(e) { if(e.cancelable) e.preventDefault(); sidebar.classList.contains('active') ? closeSidebar() : openSidebar(); }, {passive:false});
    })();
    </script>
"""
            if "</body>" in content:
                content = content.replace("</body>", touch_js + "\n</body>")
                modified = True
                touch_handlers_added += 1

        if modified:
            with open(file_path, "w", encoding=enc) as f:
                f.write(content)

    print(f"Fixed {links_fixed} broken links across files.")
    print(f"Added back buttons to {back_buttons_added} pages.")
    print(f"Added touch handlers to {touch_handlers_added} pages.")

if __name__ == "__main__":
    fix_all_qa()
