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

def fix_android_sidebar():
    root_dir = r"e:\My Projects\Notes"
    html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
    
    updated_count = 0
    
    new_css_block = """
        /* Android & Mobile Cross-Platform Sidebar Styles */
        @media (max-width: 992px) {
            .sidebar-toggle {
                display: flex !important;
                position: fixed !important;
                top: 12px !important;
                left: 12px !important;
                z-index: 1001 !important;
                background: #1e293b !important;
                color: #ffffff !important;
                border: 1px solid rgba(255,255,255,0.2) !important;
                border-radius: 8px !important;
                width: 44px !important;
                height: 44px !important;
                font-size: 1.4rem !important;
                cursor: pointer !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.4) !important;
                align-items: center !important;
                justify-content: center !important;
                touch-action: manipulation !important;
                -webkit-tap-highlight-color: transparent !important;
            }
            .sidebar-overlay {
                z-index: 999 !important;
            }
            .sidebar {
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
                box-shadow: 4px 0 20px rgba(0,0,0,0.4) !important;
                padding-top: 70px !important;
                overflow-y: auto !important;
                display: block !important;
                -webkit-overflow-scrolling: touch !important;
            }
            .sidebar.active {
                transform: translateX(0) !important;
            }
            .main-content {
                margin-left: 0 !important;
                width: 100% !important;
                padding: 70px 16px 30px 16px !important;
                max-width: 100% !important;
            }
        }
        @media (max-width: 480px) {
            .sidebar { width: 260px !important; max-height: none !important; height: 100vh !important; height: 100dvh !important; }
        }
"""

    new_js_block = """    /* Mobile Sidebar Toggle - Cross-Platform Android/iOS */
    (function() {
        var toggle = document.getElementById('sidebarToggle');
        var overlay = document.getElementById('sidebarOverlay');
        var sidebar = document.querySelector('.sidebar');
        if (!toggle || !sidebar) return;
        
        function openSidebar() {
            sidebar.classList.add('active');
            if (overlay) overlay.classList.add('active');
            toggle.innerHTML = '&#10005;';
            document.body.style.overflow = 'hidden';
        }
        function closeSidebar() {
            sidebar.classList.remove('active');
            if (overlay) overlay.classList.remove('active');
            toggle.innerHTML = '&#9776;';
            document.body.style.overflow = '';
        }
        
        function handleToggle(e) {
            if (e) {
                if (e.cancelable) e.preventDefault();
                e.stopPropagation();
            }
            if (sidebar.classList.contains('active')) {
                closeSidebar();
            } else {
                openSidebar();
            }
        }

        // Android / Touch & Click event listeners
        toggle.addEventListener('click', handleToggle);
        toggle.addEventListener('touchstart', handleToggle, { passive: false });

        if (overlay) {
            overlay.addEventListener('click', closeSidebar);
            overlay.addEventListener('touchstart', function(e) {
                if (e.cancelable) e.preventDefault();
                closeSidebar();
            }, { passive: false });
        }
        
        // Close sidebar when any link inside is clicked on mobile
        sidebar.querySelectorAll('a, .nav-link').forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 992) closeSidebar();
            });
        });
    })();"""

    for file_path in html_files:
        content, enc = read_file(file_path)
            
        if ".sidebar" not in content and "sidebarToggle" not in content:
            continue
            
        modified = False
        
        # Replace old mobile sidebar CSS block
        if "/* ===== MOBILE RESPONSIVE ===== */" in content and "/* ===== END MOBILE RESPONSIVE ===== */" in content:
            start_idx = content.find("/* ===== MOBILE RESPONSIVE ===== */")
            end_idx = content.find("/* ===== END MOBILE RESPONSIVE ===== */") + len("/* ===== END MOBILE RESPONSIVE ===== */")
            old_block = content[start_idx:end_idx]
            content = content[:start_idx] + "/* ===== MOBILE RESPONSIVE ===== */" + new_css_block + "\n        /* ===== END MOBILE RESPONSIVE ===== */" + content[end_idx:]
            modified = True
        elif ".sidebar-toggle" in content:
            # Update media queries for .sidebar-toggle from 768px to 992px
            content = content.replace("@media (max-width: 768px)", "@media (max-width: 992px)")
            modified = True

        # Replace old Mobile Sidebar Toggle JS script
        if "/* Mobile Sidebar Toggle */" in content or "/* Mobile Sidebar Toggle - Cross-Platform Android/iOS */" in content:
            js_start = content.find("/* Mobile Sidebar Toggle")
            if js_start != -1:
                # Find the enclosing <script> tag end
                script_end = content.find("</script>", js_start)
                if script_end != -1:
                    content = content[:js_start] + new_js_block + "\n    " + content[script_end:]
                    modified = True

        # Ensure touch-action and z-index on .sidebar-toggle
        if "sidebar-toggle" in content and "touch-action: manipulation" not in content:
            content = content.replace(".sidebar-toggle {", ".sidebar-toggle {\n            touch-action: manipulation !important;\n            -webkit-tap-highlight-color: transparent !important;\n            z-index: 1001 !important;")
            modified = True

        if modified:
            with open(file_path, "w", encoding=enc) as f:
                f.write(content)
            updated_count += 1

    print(f"Updated {updated_count} files for Android sidebar filter support.")

if __name__ == "__main__":
    fix_android_sidebar()
