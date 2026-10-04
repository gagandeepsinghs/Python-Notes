import re

def modify_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_css = """
    /* --- NEW HERO SECTION CSS --- */
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap');
    
    .hero {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 4rem;
        margin-bottom: 3rem;
        margin-top: 1rem;
        padding: 0 2rem;
        max-width: 1400px;
        margin-left: auto;
        margin-right: auto;
    }

    .hero-left {
        display: flex;
        align-items: center;
        gap: 3rem;
        flex: 1.2;
    }

    .profile-wrapper {
        position: relative;
    }
    
    .profile-img-container {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        border: 4px solid #ffcc00;
        padding: 5px;
        box-shadow: 0 0 40px rgba(255, 204, 0, 0.3), inset 0 0 20px rgba(255, 204, 0, 0.2);
        position: relative;
        z-index: 2;
    }
    
    .profile-img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        background-color: #111;
    }
    
    .accent-crown {
        position: absolute;
        top: -20px;
        left: 20px;
        color: #ffcc00;
        font-size: 2.5rem;
        transform: rotate(-15deg);
        z-index: 1;
    }
    
    .accent-lines {
        position: absolute;
        top: 50%;
        left: -40px;
        color: #ffcc00;
        font-size: 1.5rem;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    .accent-lines span {
        display: block;
        width: 25px;
        height: 3px;
        background-color: #ffcc00;
        border-radius: 5px;
        transform: rotate(-20deg);
    }

    .hero-text {
        flex: 1;
        text-align: left;
    }

    .hero-cursive {
        font-family: 'Caveat', cursive;
        font-size: 3.5rem;
        color: #ffffff;
        margin-bottom: -15px;
        display: block;
        transform: rotate(-3deg);
    }

    .hero-title-new {
        font-size: 4.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        letter-spacing: -1px;
        color: white;
    }

    .hero-title-new .name-yellow {
        color: #ffcc00;
    }

    .hero-subtitle-new {
        font-size: 1.1rem;
        color: var(--text-muted);
        line-height: 1.6;
        margin-bottom: 2rem;
        max-width: 450px;
    }

    .hero-right {
        flex: 0.8;
        background: rgba(20, 20, 20, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2.5rem;
        position: relative;
    }
    
    .learn-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 2rem;
    }
    
    .bulb-icon {
        color: #ffcc00;
        font-size: 2rem;
    }
    
    .learn-title {
        font-family: 'Caveat', cursive;
        font-size: 2.8rem;
        color: #fff;
        transform: rotate(-3deg);
    }
    
    .learn-arrow {
        color: #ffcc00;
        font-size: 1.5rem;
        margin-left: auto;
        transform: rotate(30deg);
    }

    .tag-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 15px;
        margin-bottom: 2rem;
    }

    .tag-btn {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 12px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        color: #ddd;
        font-size: 0.9rem;
        font-weight: 600;
        transition: all 0.3s;
        cursor: default;
    }
    .tag-btn i { font-size: 1.2rem; }
    .tag-btn .i-orange { color: #f97316; }
    .tag-btn .i-cyan { color: #06b6d4; }
    .tag-btn .i-blue { color: #3b82f6; }
    .tag-btn .i-purple { color: #a855f7; }
    .tag-btn .i-white { color: #e2e8f0; }
    .tag-btn .i-robot { color: #ef4444; }

    .connect-btn {
        display: flex;
        align-items: center;
        background: rgba(20, 20, 20, 0.8);
        border: 1px solid rgba(255, 204, 0, 0.3);
        border-radius: 16px;
        padding: 1rem 1.5rem;
        gap: 20px;
        text-decoration: none;
        box-shadow: 0 0 20px rgba(255, 204, 0, 0.1);
        transition: all 0.3s ease;
    }
    .connect-btn:hover {
        box-shadow: 0 0 30px rgba(255, 204, 0, 0.2);
        transform: translateY(-2px);
    }
    .wa-icon {
        width: 50px;
        height: 50px;
        background: #25D366;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.8rem;
        box-shadow: 0 0 20px rgba(37, 211, 102, 0.4);
    }
    .wa-text p {
        color: #ddd;
        font-size: 0.85rem;
        margin-bottom: 2px;
    }
    .wa-text h3 {
        color: #ffcc00;
        font-size: 1.6rem;
        font-weight: 800;
    }
    .wa-arrow {
        margin-left: auto;
        color: #ffcc00;
        font-size: 1.5rem;
    }

    @media (max-width: 1200px) {
        .hero { flex-direction: column; }
        .hero-left, .hero-right { width: 100%; }
    }
    @media (max-width: 1000px) {
        .tag-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 650px) {
        .hero-left { flex-direction: column; text-align: center; gap: 1.5rem; }
        .hero-text { text-align: center; }
        .hero-cursive { text-align: center; }
        .hero-title-new { font-size: 3rem; }
    }
    /* ------------------------------ */
    </style>
    """

    new_html = """
    <!-- NEW HERO SECTION -->
    <div class="hero">
        <div class="hero-left">
            <!-- Logo -->
            <div class="profile-wrapper">
                <i class="fa-solid fa-crown accent-crown"></i>
                <div class="accent-lines">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <div class="profile-img-container">
                    <img src="assets/logo.png" alt="Python with Gagan Sir" class="profile-img">
                </div>
            </div>

            <!-- Text -->
            <div class="hero-text">
                <span class="hero-cursive">Learn with</span>
                <h1 class="hero-title-new">Gagan <span class="name-yellow">Sir</span></h1>
                <p class="hero-subtitle-new">Your Ultimate Learning Portal for Python, Data Structures, SQL, Data Analytics and Beyond.</p>
            </div>
        </div>

        <!-- Right Box -->
        <div class="hero-right">
            <div class="learn-header">
                <i class="fa-regular fa-lightbulb bulb-icon"></i>
                <h2 class="learn-title">Wants to Learn?</h2>
                <i class="fa-solid fa-arrow-turn-down learn-arrow"></i>
            </div>
            
            <div class="tag-grid">
                <div class="tag-btn"><i class="fa-solid fa-chart-column i-orange"></i> Data Analytics</div>
                <div class="tag-btn"><i class="fa-solid fa-microchip i-cyan"></i> AI</div>
                <div class="tag-btn"><i class="fa-brands fa-python i-blue"></i> Python</div>
                <div class="tag-btn"><i class="fa-solid fa-atom i-purple"></i> Data Science</div>
                <div class="tag-btn"><i class="fa-solid fa-wrench i-white"></i> AI Tools</div>
                <div class="tag-btn"><i class="fa-solid fa-robot i-robot"></i> AI Agents</div>
            </div>
            
            <a href="#" class="connect-btn">
                <div class="wa-icon"><i class="fa-brands fa-whatsapp"></i></div>
                <div class="wa-text">
                    <p>Connect with Me</p>
                    <h3>+91 98765 43210</h3>
                </div>
                <i class="fa-regular fa-paper-plane wa-arrow"></i>
            </a>
        </div>
    </div>
    <!-- END NEW HERO SECTION -->
    """

    # Replace CSS
    html = html.replace('</style>', new_css)

    # Replace <header> block
    html = re.sub(r'<header>.*?</header>', new_html, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done injecting new hero section while keeping original grid!")

if __name__ == '__main__':
    modify_index()
