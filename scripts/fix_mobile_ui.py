import os
import glob
import re

workspace_dir = r"e:\My Projects\Notes"
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith("_notes.html") and "master_notes.html" not in file:
            html_files.append(os.path.join(root, file))

mobile_css = """
        /* Mobile UI Fixes */
        @media (max-width: 900px) {
            body { 
                flex-direction: column !important; 
                display: flex !important;
            }
            .sidebar { 
                width: 100% !important; 
                position: relative !important; 
                height: auto !important; 
                padding: 20px !important;
                border-bottom: 2px solid var(--border-light, #e2e8f0);
            }
            .main-content { 
                margin-left: 0 !important; 
                padding: 20px 15px !important; 
                width: 100% !important;
            }
            .def-box-blue, .def-box-yellow {
                border-radius: 8px !important;
                padding: 15px !important;
            }
            .code-block, pre, .output-box {
                font-size: 0.8rem !important;
                overflow-x: auto !important;
            }
            .header-card h1 {
                font-size: 1.5rem !important;
            }
            .brand-badge {
                display: inline-block !important;
                margin-bottom: 10px !important;
            }
        }
"""

files_updated = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    if "/* Mobile UI Fixes */" not in content and "@media (max-width: 900px)" not in content:
        content = content.replace("</style>", mobile_css + "    </style>")
    elif "/* Mobile UI Fixes */" not in content and "@media (max-width: 900px)" in content:
        # Some files like Java have basic media query, let's reinforce it
        # Wait, if they already have media query, adding this might duplicate.
        # I'll just append my robust mobile_css if they don't have it, or overwrite the old one if they do?
        # Let's just append it anyway, CSS later in the file overrides earlier rules!
        content = content.replace("</style>", mobile_css + "    </style>")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Added Mobile UI fixes to: {os.path.basename(filepath)}")

print(f"Successfully processed {files_updated} notes files.")
