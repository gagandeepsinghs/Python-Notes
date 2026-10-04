import os
import shutil

source_file = r"e:\My Projects\Notes\java\00_master_notes_portal.html"
target_file = r"e:\My Projects\Notes\AI_ML\00_master_notes_portal.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace("<title>Java Programming Master Suite", "<title>AI & ML Master Suite")

grid_start = content.find('<div class="grid">')
footer_start = content.find('<footer>')

aiml_cards = """
            <!-- Foundations & Math -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-calculator"></i></span> Foundations & Math</h2>
                <ul class="links-list">
                    <li><a href="01_aiml_foundations_python_numpy_pandas_notes.html">01. Foundations, Python & Pandas</a></li>
                    <li><a href="02_eda_math_statistics_probability_notes.html">02. EDA, Math & Statistics</a></li>
                </ul>
            </div>

            <!-- Machine Learning -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-brain"></i></span> Machine Learning</h2>
                <ul class="links-list">
                    <li><a href="03_ml_preprocessing_pipelines_validation_notes.html">03. ML Preprocessing & Validation</a></li>
                    <li><a href="04_supervised_regression_classification_ensembles_notes.html">04. Supervised ML</a></li>
                    <li><a href="05_unsupervised_pca_anomaly_recommendations_timeseries_notes.html">05. Unsupervised ML</a></li>
                </ul>
            </div>

            <!-- Deep Learning & NLP -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-network-wired"></i></span> Deep Learning & NLP</h2>
                <ul class="links-list">
                    <li><a href="06_deeplearning_neuralnets_tensorflow_pytorch_cv_notes.html">06. Deep Learning, NN & CV</a></li>
                    <li><a href="07_nlp_transformers_llms_genai_rag_deployment_notes.html">07. NLP, Transformers & GenAI</a></li>
                </ul>
            </div>

            <!-- Practice & Master Manual -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-code"></i></span> Practice & Manual</h2>
                <ul class="links-list">
                    <li><a href="08_projects_cheatsheet_interview_prep_checklist_notes.html">08. Projects & Interview Prep</a></li>
                    <li><a href="00_aiml_master_notes.html">AI/ML Master Notes</a></li>
                </ul>
            </div>
"""

new_content = content[:grid_start + len('<div class="grid">')] + aiml_cards + "\n        </div>\n    </div>\n\n    " + content[footer_start:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Copy to master_notes_portal.html as well
shutil.copy(target_file, r"e:\My Projects\Notes\AI_ML\master_notes_portal.html")

print("AI/ML portal updated with the multi-card layout.")
