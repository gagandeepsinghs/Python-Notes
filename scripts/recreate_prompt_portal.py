import os
import shutil

source_file = r"e:\My Projects\Notes\java\00_master_notes_portal.html"
target_file = r"e:\My Projects\Notes\Prompt Engineering\00_master_notes_portal.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace("<title>Java Programming Master Suite", "<title>Prompt Engineering Master Suite")
content = content.replace("<h1>Java Programming Master Learning Suite</h1>", "<h1>Prompt Engineering Master Learning Suite</h1>")

grid_start = content.find('<div class="grid">')
footer_start = content.find('<footer>')

prompt_cards = """
            <!-- Foundations & Techniques -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-graduation-cap"></i></span> Foundations & Techniques</h2>
                <ul class="links-list">
                    <li><a href="01_prompt_foundations_anatomy_roles_constraints_notes.html">01. Prompt Foundations & Anatomy</a></li>
                    <li><a href="02_prompt_techniques_fewshot_cot_chaining_frameworks_notes.html">02. Techniques & Frameworks</a></li>
                </ul>
            </div>

            <!-- Domain & Security -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-shield-halved"></i></span> Domain & Security</h2>
                <ul class="links-list">
                    <li><a href="03_domain_prompts_coding_sql_data_rag_agents_notes.html">03. Domain Prompts (Coding, Data)</a></li>
                    <li><a href="04_prompt_security_injection_privacy_context_tokens_notes.html">04. Security & Context</a></li>
                </ul>
            </div>

            <!-- Evaluation & Use Cases -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-list-check"></i></span> Evaluation & Use Cases</h2>
                <ul class="links-list">
                    <li><a href="05_prompt_evaluation_rubrics_abtesting_golden_sets_notes.html">05. Evaluation & Rubrics</a></li>
                    <li><a href="06_usecase_prompts_business_education_marketing_code_review_notes.html">06. Use Case Prompts</a></li>
                    <li><a href="07_advanced_patterns_critic_guardrails_optimization_notes.html">07. Advanced Patterns</a></li>
                </ul>
            </div>

            <!-- Practice & Master Manual -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-code"></i></span> Practice & Manual</h2>
                <ul class="links-list">
                    <li><a href="08_line_by_line_prompts_rubrics_projects_interview_roadmap_notes.html">08. Projects & Interview Prep</a></li>
                    <li><a href="00_prompt_engineering_master_notes.html">Prompt Engineering Master Notes</a></li>
                </ul>
            </div>
"""

new_content = content[:grid_start + len('<div class="grid">')] + prompt_cards + "\n        </div>\n    </div>\n\n    " + content[footer_start:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Copy to master_notes_portal.html as well
shutil.copy(target_file, r"e:\My Projects\Notes\Prompt Engineering\master_notes_portal.html")

print("Prompt Engineering portal updated with the multi-card layout.")
