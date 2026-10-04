import os
import shutil

source_file = r"e:\My Projects\Notes\java\00_master_notes_portal.html"
target_file = r"e:\My Projects\Notes\Gen AI\00_master_notes_portal.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace("<title>Java Programming Master Suite", "<title>Generative AI Master Suite")
content = content.replace("<h1>Java Programming Master Learning Suite</h1>", "<h1>Generative AI Master Learning Suite</h1>")

grid_start = content.find('<div class="grid">')
footer_start = content.find('<footer>')

genai_cards = """
            <!-- Foundations & Prompting -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-brain"></i></span> Foundations & Prompting</h2>
                <ul class="links-list">
                    <li><a href="01_genai_foundations_transformers_tokens_embeddings_notes.html">01. Foundations & Transformers</a></li>
                    <li><a href="02_llm_concepts_prompting_structured_tooluse_apis_notes.html">02. LLM Concepts & Prompting</a></li>
                </ul>
            </div>

            <!-- RAG, Tuning & Agents -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-network-wired"></i></span> RAG, Tuning & Agents</h2>
                <ul class="links-list">
                    <li><a href="03_rag_chunking_vectordb_retrieval_evaluation_notes.html">03. RAG & Retrieval</a></li>
                    <li><a href="04_finetuning_peft_lora_multimodal_image_speech_video_notes.html">04. Fine-Tuning & Multimodal</a></li>
                    <li><a href="05_ai_agents_multiagent_langchain_langgraph_llamaindex_notes.html">05. AI Agents & Langchain</a></li>
                </ul>
            </div>

            <!-- Architecture & Security -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-shield-halved"></i></span> Architecture & Security</h2>
                <ul class="links-list">
                    <li><a href="06_genai_fastapi_databases_streaming_caching_observability_notes.html">06. FastAPI & Caching</a></li>
                    <li><a href="07_security_guardrails_prompt_injection_architecture_mlops_notes.html">07. Security & Guardrails</a></li>
                </ul>
            </div>

            <!-- Practice & Master Manual -->
            <div class="card">
                <h2><span class="card-icon"><i class="fa-solid fa-code"></i></span> Practice & Manual</h2>
                <ul class="links-list">
                    <li><a href="08_projects_cheatsheet_interview_prep_roadmap_blueprint_notes.html">08. Projects & Interview Prep</a></li>
                    <li><a href="00_genai_master_notes.html">GenAI Master Notes</a></li>
                </ul>
            </div>
"""

new_content = content[:grid_start + len('<div class="grid">')] + genai_cards + "\n        </div>\n    </div>\n\n    " + content[footer_start:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Copy to master_notes_portal.html as well
shutil.copy(target_file, r"e:\My Projects\Notes\Gen AI\master_notes_portal.html")

print("Gen AI portal updated with the multi-card layout.")
