"""
Fix Mobile Responsive Layout for All HTML Files with Sidebar
Injects:
  1. Responsive CSS (@media queries) for mobile/tablet
  2. Hamburger menu button in the body
  3. JavaScript for sidebar toggle
"""

import os
import re
import glob

PROJECT_ROOT = r"e:\My Projects\Notes"

# The responsive CSS to inject before </style>
RESPONSIVE_CSS = """
        /* ===== MOBILE RESPONSIVE ===== */
        .sidebar-toggle {
            display: none;
            position: fixed;
            top: 12px;
            left: 12px;
            z-index: 1001;
            background: #1e293b;
            color: #fff;
            border: none;
            border-radius: 8px;
            width: 44px;
            height: 44px;
            font-size: 1.4rem;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }
        .sidebar-toggle:hover { background: #334155; }
        .sidebar-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.5);
            z-index: 99;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .sidebar-overlay.active {
            display: block;
            opacity: 1;
        }

        @media (max-width: 1024px) {
            .main-content {
                padding: 30px 24px !important;
            }
        }

        @media (max-width: 768px) {
            .sidebar-toggle {
                display: flex;
            }
            .sidebar {
                transform: translateX(-110%);
                transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                z-index: 1000;
                width: 280px !important;
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                height: 100vh !important;
                height: 100dvh !important;
                box-shadow: 4px 0 20px rgba(0,0,0,0.3);
            }
            .sidebar.active {
                transform: translateX(0);
            }
            .main-content {
                margin-left: 0 !important;
                width: 100% !important;
                padding: 70px 16px 30px 16px !important;
                max-width: 100% !important;
            }
            body {
                flex-direction: column;
            }
            h1 { font-size: 1.5rem !important; }
            h2 { font-size: 1.3rem !important; }
            h3 { font-size: 1.15rem !important; }
            table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; font-size: 0.9rem; }
            th, td { padding: 8px 10px !important; white-space: nowrap; }
            pre, code { font-size: 0.85rem !important; overflow-x: auto; }
            pre { padding: 12px !important; }
            .code-block, .code-container { overflow-x: auto; max-width: 100%; }
            img, svg, .visual-container { max-width: 100% !important; height: auto !important; overflow: hidden; }
            .visual-container { padding: 15px !important; }
        }

        @media (max-width: 480px) {
            .main-content {
                padding: 65px 10px 20px 10px !important;
            }
            h1 { font-size: 1.25rem !important; }
            h2 { font-size: 1.15rem !important; }
            p, li { font-size: 0.95rem !important; }
            .sidebar { width: 260px !important; }
            th, td { padding: 6px 8px !important; font-size: 0.8rem; }
        }
        /* ===== END MOBILE RESPONSIVE ===== */
"""

# Hamburger button HTML to inject right after <body> (or <body ...>)
HAMBURGER_HTML = """
    <!-- Mobile Sidebar Toggle -->
    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle navigation">&#9776;</button>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
"""

# JavaScript for sidebar toggle - inject before </body>
TOGGLE_JS = """
    <script>
    /* Mobile Sidebar Toggle */
    (function() {
        var toggle = document.getElementById('sidebarToggle');
        var overlay = document.getElementById('sidebarOverlay');
        var sidebar = document.querySelector('.sidebar');
        if (!toggle || !sidebar) return;
        
        function openSidebar() {
            sidebar.classList.add('active');
            overlay.classList.add('active');
            toggle.innerHTML = '&#10005;';
        }
        function closeSidebar() {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            toggle.innerHTML = '&#9776;';
        }
        toggle.addEventListener('click', function() {
            if (sidebar.classList.contains('active')) {
                closeSidebar();
            } else {
                openSidebar();
            }
        });
        overlay.addEventListener('click', closeSidebar);
        
        // Close sidebar when a navigation link is clicked (smooth UX)
        sidebar.querySelectorAll('a[href^="#"]').forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 768) closeSidebar();
            });
        });
    })();
    </script>
"""


def find_html_files_with_sidebar(root):
    """Find all HTML files that have class='sidebar' """
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip .git and scripts directories
        dirnames[:] = [d for d in dirnames if d not in ['.git', 'node_modules', 'backups']]
        for fname in filenames:
            if fname.endswith('.html'):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if 'class="sidebar"' in content:
                        files.append(fpath)
                except Exception as e:
                    print(f"  [SKIP] Error reading {fpath}: {e}")
    return files


def already_has_responsive(content):
    """Check if file already has our responsive CSS"""
    return '/* ===== MOBILE RESPONSIVE =====' in content or 'sidebar-toggle' in content


def inject_responsive(filepath):
    """Inject responsive CSS, hamburger button, and toggle JS into an HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if already_has_responsive(content):
        return False, "Already has responsive CSS"

    if '@media' in content and 'sidebar-toggle' in content:
        return False, "Already responsive"

    original = content

    # 1. Inject responsive CSS before </style>
    if '</style>' in content:
        content = content.replace('</style>', RESPONSIVE_CSS + '    </style>', 1)
    else:
        return False, "No </style> tag found"

    # 2. Inject hamburger button after <body> or <body ...>
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        insert_pos = body_match.end()
        content = content[:insert_pos] + HAMBURGER_HTML + content[insert_pos:]
    else:
        return False, "No <body> tag found"

    # 3. Inject toggle JS before </body>
    if '</body>' in content:
        content = content.replace('</body>', TOGGLE_JS + '</body>', 1)
    else:
        return False, "No </body> tag found"

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, "Injected responsive CSS + hamburger + toggle JS"


def main():
    print("=" * 60)
    print("  Mobile Responsive Fix for All Sidebar HTML Files")
    print("=" * 60)
    print(f"\nScanning: {PROJECT_ROOT}\n")

    files = find_html_files_with_sidebar(PROJECT_ROOT)
    print(f"Found {len(files)} HTML files with sidebar.\n")

    fixed = 0
    skipped = 0
    errors = 0

    for fpath in sorted(files):
        rel = os.path.relpath(fpath, PROJECT_ROOT)
        try:
            success, msg = inject_responsive(fpath)
            if success:
                print(f"  [FIXED] {rel}")
                fixed += 1
            else:
                print(f"  [SKIP]  {rel} — {msg}")
                skipped += 1
        except Exception as e:
            print(f"  [ERROR] {rel} — {e}")
            errors += 1

    print(f"\n{'=' * 60}")
    print(f"  Done! Fixed: {fixed} | Skipped: {skipped} | Errors: {errors}")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
