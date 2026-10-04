import os

source_file = r"e:\My Projects\Notes\full_stack_portal.html"
target_file = r"e:\My Projects\Notes\Linux Administration\00_master_notes_portal.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace("Full Stack Development | Master Portal", "Linux Administration | Master Portal")

# Replace back button link
content = content.replace('href="index.html"', 'href="../index.html"')

# Replace the grid content
grid_start = content.find('<div class="grid">')
footer_start = content.find('<footer>')

linux_card = """
            <!-- Linux Administration -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-brands fa-linux" style="color: #facc15;"></i></span> Linux Administration</h2>
                <ul class="links-list">
                    <li><a href="01_linux_fundamentals_setup_notes.html">01. Fundamentals & VM Setup</a></li>
                    <li><a href="02_filesystem_directory_management_notes.html">02. Filesystem & File Operations</a></li>
                    <li><a href="03_permissions_users_groups_acl_notes.html">03. Permissions, Users & ACL</a></li>
                    <li><a href="04_text_processing_processes_cron_notes.html">04. Text, Processes & Cron</a></li>
                    <li><a href="05_packages_systemd_boot_storage_notes.html">05. Packages, Boot, LVM & RAID</a></li>
                    <li><a href="06_networking_dns_ssh_security_notes.html">06. Networking, SSH & SELinux</a></li>
                    <li><a href="07_logs_monitoring_performance_scripting_notes.html">07. Logs, Performance & Scripting</a></li>
                    <li><a href="08_services_containers_cloud_ansible_interviews_notes.html">08. Enterprise, Cloud & Interviews</a></li>
                    <li><a href="00_linux_administration_master_notes.html">Linux Master Notes</a></li>
                </ul>
            </div>
            
            <!-- Coming Soon -->
            <div class="card" style="justify-content: center; align-items: center; text-align: center; opacity: 0.7; border: 2px dashed var(--border); background: rgba(20, 20, 20, 0.4);">
                <h2><span class="card-icon"><i class="fa-solid fa-hourglass-half"></i></span> Coming Soon</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.5rem;">More advanced Linux notes are on the way!</p>
            </div>
"""

new_content = content[:grid_start + len('<div class="grid">')] + linux_card + """\n        </div>\n    </div>\n\n    """ + content[footer_start:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Linux portal successfully recreated.")
