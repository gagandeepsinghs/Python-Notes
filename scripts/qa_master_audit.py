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

def run_qa_audit():
    root_dir = r"e:\My Projects\Notes"
    html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
    
    # Exclude backups directory if present
    html_files = [f for f in html_files if "backups" not in f and "node_modules" not in f]
    
    print(f"=== STARTING SENIOR QA AUDIT ON {len(html_files)} HTML FILES ===")
    
    audit_results = {
        "missing_viewport": [],
        "broken_internal_links": [],
        "missing_sidebar_touch": [],
        "table_overflow_risk": [],
        "code_overflow_risk": [],
        "back_button_missing": [],
        "fixed_files": 0
    }
    
    # Map of all real file paths relative to root (for link validation)
    existing_paths = set()
    for f in html_files:
        rel_path = os.path.relpath(f, root_dir).replace("\\", "/")
        existing_paths.add(rel_path.lower())
        
    for file_path in html_files:
        rel_file = os.path.relpath(file_path, root_dir).replace("\\", "/")
        content, enc = read_file(file_path)
        modified = False
        
        # 1. Check viewport meta tag
        if '<meta name="viewport"' not in content and "<meta name='viewport'" not in content:
            audit_results["missing_viewport"].append(rel_file)
            # Fix missing viewport tag in head
            if "</head>" in content:
                content = content.replace("</head>", '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n</head>')
                modified = True
                
        # 2. Check internal link integrity
        href_matches = re.findall(r'href=["\']([^"\']+)["\']', content)
        dir_name = os.path.dirname(file_path)
        for href in href_matches:
            if href.startswith("#") or href.startswith("javascript:") or href.startswith("http") or href.startswith("mailto:") or href.startswith("https:"):
                continue
            # Strip query params or hash
            clean_href = href.split("?")[0].split("#")[0]
            if not clean_href:
                continue
            
            # Resolve relative path
            target_path = os.path.normpath(os.path.join(dir_name, clean_href))
            rel_target = os.path.relpath(target_path, root_dir).replace("\\", "/").lower()
            
            if rel_target not in existing_paths and not os.path.exists(target_path):
                audit_results["broken_internal_links"].append((rel_file, href))
                
        # 3. Check for .sidebar files lacking touch events
        if ".sidebar" in content and "touchstart" not in content:
            audit_results["missing_sidebar_touch"].append(rel_file)
            
        # 4. Check for table responsiveness styles
        if "<table" in content and "table-responsive" not in content and "overflow-x" not in content and "max-width: 100%" not in content:
            audit_results["table_overflow_risk"].append(rel_file)
            
        # 5. Check for code block responsiveness
        if ("<pre" in content or "<code" in content) and "overflow-x" not in content:
            audit_results["code_overflow_risk"].append(rel_file)
            
        # 6. Check for Back / Home button in sub-pages
        if rel_file not in ["index.html", "govt_portal.html", "database_portal.html", "full_stack/html/master_notes_portal.html", "full_stack/css/master_notes_portal.html"]:
            if "Back to Home" not in content and "history.back()" not in content and "back-btn" not in content and "index.html" not in content and "portal.html" not in content:
                audit_results["back_button_missing"].append(rel_file)

        # Apply global responsive & viewport safety patches if modified
        if modified:
            with open(file_path, "w", encoding=enc) as f:
                f.write(content)
            audit_results["fixed_files"] += 1
            
    print("\n--- QA AUDIT SUMMARY REPORT ---")
    print(f"Total HTML files audited: {len(html_files)}")
    print(f"Missing Viewport Meta Tags (Fixed): {len(audit_results['missing_viewport'])}")
    print(f"Missing Sidebar Touch Handlers: {len(audit_results['missing_sidebar_touch'])}")
    print(f"Table Overflow Risks: {len(audit_results['table_overflow_risk'])}")
    print(f"Code Overflow Risks: {len(audit_results['code_overflow_risk'])}")
    print(f"Broken Internal Links Found: {len(audit_results['broken_internal_links'])}")
    if audit_results["broken_internal_links"]:
        print("Sample broken links:")
        for source, link in audit_results["broken_internal_links"][:10]:
            print(f"  In {source} -> {link}")
    print(f"Missing Back Buttons: {len(audit_results['back_button_missing'])}")
    if audit_results["back_button_missing"]:
        print("Files missing navigation back buttons:")
        for f in audit_results["back_button_missing"][:10]:
            print(f"  {f}")
            
if __name__ == "__main__":
    run_qa_audit()
