import glob
import re

clean_top_part = '''
    <!-- Floating Background Coding Icons -->
    <div class="floating-icons">
        <i class="fa-brands fa-python bg-icon icon-1"></i>
        <i class="fa-solid fa-code bg-icon icon-2"></i>
        <i class="fa-brands fa-html5 bg-icon icon-3"></i>
        <i class="fa-solid fa-database bg-icon icon-4"></i>
        <i class="fa-brands fa-js bg-icon icon-5"></i>
    </div>

    <div class="bg-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
    </div>

    <!-- Theme Toggle Button -->
    <button class="theme-toggle" id="themeToggle" title="Toggle Light/Dark Theme">
        <i class="fa-solid fa-sun"></i>
    </button>

    <!-- Chatbot Floating Button -->
    <button class="chatbot-float" id="chatbotToggle" title="Chat with Assistant">
        <i class="fa-brands fa-whatsapp"></i>
    </button>

    <!-- Chatbot Window -->
    <div class="chatbot-window" id="chatbotWindow">
        <div class="chatbot-header">
            <h3><i class="fa-solid fa-robot"></i> Assistant</h3>
            <button id="closeChatbot"><i class="fa-solid fa-times"></i></button>
        </div>
        <div class="chatbot-body" id="chatbotBody">
            <div class="chat-message bot">
                <p>Hi there! How can I help you today?</p>
                <div class="chat-options">
                    <button class="chat-option" onclick="handleOption(this, 'contact')">Contacting 📞</button>
                    <button class="chat-option" onclick="handleOption(this, 'flirt')">Want tips in flirting? 😉</button>
                    <button class="chat-option" onclick="handleOption(this, 'depression')">In depression? 🫂</button>
                    <button class="chat-option" onclick="handleOption(this, 'career')">Want career guidance? 📈</button>
                    <button class="chat-option" onclick="handleOption(this, 'notes')">Want notes? 📚</button>
                </div>
            </div>
        </div>
    </div>

    <div style="position: absolute; top: 20px; left: 20px; z-index: 100;">
        <a href="index.html" style="background: var(--primary); color: #000; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; font-family: 'Outfit', sans-serif;"><i class="fa-solid fa-arrow-left"></i> Back to Home</a>
    </div>

    <div class="container" style="max-width: 95%; padding-top: 100px;">
        <div class="grid">
'''

for f in glob.glob('*_portal.html'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    body_idx = content.find('<body>')
    if body_idx == -1:
        continue
    
    body_tag_end = body_idx + 6
    
    parts = content.split('<div class="grid">')
    if len(parts) > 1:
        cards_content = parts[-1]
        
        new_content = content[:body_tag_end] + '\n' + clean_top_part + cards_content
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f + ' cleaned!')
