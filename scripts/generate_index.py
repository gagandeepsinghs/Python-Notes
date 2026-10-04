index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn with Gagan Sir</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-dark: #0b0b0b;
            --card-bg: rgba(20, 20, 20, 0.7);
            --card-border: rgba(255, 255, 255, 0.1);
            --primary-yellow: #ffcc00;
            --text-main: #ffffff;
            --text-muted: #a1a1aa;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                radial-gradient(circle at 90% 80%, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem 4rem;
        }

        /* --- HERO SECTION --- */
        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 4rem;
            margin-bottom: 3rem;
            margin-top: 1rem;
        }

        .hero-left {
            display: flex;
            align-items: center;
            gap: 3rem;
            flex: 1.2;
        }

        /* Logo Profile */
        .profile-wrapper {
            position: relative;
        }
        
        .profile-img-container {
            width: 280px;
            height: 280px;
            border-radius: 50%;
            border: 4px solid var(--primary-yellow);
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
        
        /* Floating acccents behind/around logo */
        .accent-crown {
            position: absolute;
            top: -20px;
            left: 20px;
            color: var(--primary-yellow);
            font-size: 2.5rem;
            transform: rotate(-15deg);
            z-index: 1;
        }
        .accent-lines {
            position: absolute;
            top: 50%;
            left: -40px;
            color: var(--primary-yellow);
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
            background-color: var(--primary-yellow);
            border-radius: 5px;
            transform: rotate(-20deg);
        }

        /* Hero Text */
        .hero-text {
            flex: 1;
        }

        .hero-cursive {
            font-family: 'Caveat', cursive;
            font-size: 3.5rem;
            color: #ffffff;
            margin-bottom: -15px;
            display: block;
            transform: rotate(-3deg);
        }

        .hero-title {
            font-size: 4.5rem;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
        }

        .hero-title .name-yellow {
            color: var(--primary-yellow);
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 2rem;
            max-width: 450px;
        }

        /* Feature Badges */
        .feature-badges {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        
        .f-badge {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .f-icon {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
        }
        .f-text {
            font-size: 0.85rem;
            font-weight: 600;
            color: #ddd;
            line-height: 1.2;
        }
        
        .f-icon.gold { color: #eab308; box-shadow: 0 0 15px rgba(234, 179, 8, 0.2); border: 1px solid rgba(234, 179, 8, 0.3); }
        .f-icon.blue { color: #38bdf8; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.3); }
        .f-icon.purple { color: #a855f7; box-shadow: 0 0 15px rgba(168, 85, 247, 0.2); border: 1px solid rgba(168, 85, 247, 0.3); }


        /* Right Side Box */
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
            color: var(--primary-yellow);
            font-size: 2rem;
        }
        
        .learn-title {
            font-family: 'Caveat', cursive;
            font-size: 2.8rem;
            color: #fff;
            transform: rotate(-3deg);
        }
        
        .learn-arrow {
            color: var(--primary-yellow);
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
        .tag-btn i {
            font-size: 1.2rem;
        }
        .tag-btn .i-orange { color: #f97316; }
        .tag-btn .i-cyan { color: #06b6d4; }
        .tag-btn .i-blue { color: #3b82f6; }
        .tag-btn .i-purple { color: #a855f7; }
        .tag-btn .i-white { color: #e2e8f0; }
        .tag-btn .i-robot { color: #ef4444; }

        /* Whatsapp Connect Button */
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
            color: var(--primary-yellow);
            font-size: 1.6rem;
            font-weight: 800;
        }
        .wa-arrow {
            margin-left: auto;
            color: var(--primary-yellow);
            font-size: 1.5rem;
        }


        /* --- MODULES GRID --- */
        .modules-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
        }

        .mod-card {
            background: rgba(20, 20, 20, 0.6);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 1.25rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            position: relative;
        }

        .mod-card:hover {
            transform: translateY(-3px);
            background: rgba(30, 30, 30, 0.8);
        }

        .mod-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255,255,255,0.1);
        }

        .mod-info {
            flex: 1;
        }
        .mod-info h3 {
            font-size: 1.1rem;
            font-weight: 600;
        }

        .mod-open {
            font-size: 0.85rem;
            padding: 6px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: all 0.3s;
        }
        
        .mod-open i {
            font-size: 0.7rem;
        }

        /* Specific Mod Card Glows */
        .mod-python { border-color: rgba(59, 130, 246, 0.3); box-shadow: inset 0 0 20px rgba(59, 130, 246, 0.05); }
        .mod-python .mod-icon { color: #3b82f6; border-color: rgba(59, 130, 246, 0.4); }
        .mod-python .mod-open { border-color: rgba(59, 130, 246, 0.5); color: #e2e8f0; }

        .mod-java { border-color: rgba(239, 68, 68, 0.3); box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.05); }
        .mod-java .mod-icon { color: #ef4444; border-color: rgba(239, 68, 68, 0.4); }
        .mod-java .mod-open { border-color: rgba(239, 68, 68, 0.5); color: #e2e8f0; }

        .mod-govt { border-color: rgba(255, 255, 255, 0.2); box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.05); }
        .mod-govt .mod-icon { color: #f8fafc; border-color: rgba(255, 255, 255, 0.3); }
        .mod-govt .mod-open { border-color: rgba(255, 255, 255, 0.3); color: #e2e8f0; }

        .mod-excel { border-color: rgba(34, 197, 94, 0.3); box-shadow: inset 0 0 20px rgba(34, 197, 94, 0.05); }
        .mod-excel .mod-icon { color: #22c55e; border-color: rgba(34, 197, 94, 0.4); }
        .mod-excel .mod-open { border-color: rgba(34, 197, 94, 0.5); color: #e2e8f0; }

        .mod-pbi { border-color: rgba(234, 179, 8, 0.3); box-shadow: inset 0 0 20px rgba(234, 179, 8, 0.05); }
        .mod-pbi .mod-icon { color: #eab308; border-color: rgba(234, 179, 8, 0.4); }
        .mod-pbi .mod-open { border-color: rgba(234, 179, 8, 0.5); color: #e2e8f0; }

        .mod-sql { border-color: rgba(14, 165, 233, 0.3); box-shadow: inset 0 0 20px rgba(14, 165, 233, 0.05); }
        .mod-sql .mod-icon { color: #0ea5e9; border-color: rgba(14, 165, 233, 0.4); }
        .mod-sql .mod-open { border-color: rgba(14, 165, 233, 0.5); color: #e2e8f0; }

        .mod-other { border-color: rgba(226, 232, 240, 0.2); box-shadow: inset 0 0 20px rgba(226, 232, 240, 0.05); }
        .mod-other .mod-icon { color: #e2e8f0; border-color: rgba(226, 232, 240, 0.3); }
        .mod-other .mod-open { border-color: rgba(226, 232, 240, 0.3); color: #e2e8f0; }

        .mod-web { border-color: rgba(56, 189, 248, 0.3); box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.05); }
        .mod-web .mod-icon { color: #38bdf8; border-color: rgba(56, 189, 248, 0.4); }
        .mod-web .mod-open { border-color: rgba(56, 189, 248, 0.5); color: #e2e8f0; }

        .mod-data { border-color: rgba(168, 85, 247, 0.3); box-shadow: inset 0 0 20px rgba(168, 85, 247, 0.05); }
        .mod-data .mod-icon { color: #a855f7; border-color: rgba(168, 85, 247, 0.4); }
        .mod-data .mod-open { border-color: rgba(168, 85, 247, 0.5); color: #e2e8f0; }

        .mod-card:hover .mod-open {
            background: rgba(255,255,255,0.1);
        }

        /* Add hover glows to cards */
        .mod-python:hover { box-shadow: inset 0 0 20px rgba(59, 130, 246, 0.05), 0 0 20px rgba(59, 130, 246, 0.2); }
        .mod-java:hover { box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.05), 0 0 20px rgba(239, 68, 68, 0.2); }
        .mod-govt:hover { box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.05), 0 0 20px rgba(255, 255, 255, 0.1); }
        .mod-excel:hover { box-shadow: inset 0 0 20px rgba(34, 197, 94, 0.05), 0 0 20px rgba(34, 197, 94, 0.2); }
        .mod-pbi:hover { box-shadow: inset 0 0 20px rgba(234, 179, 8, 0.05), 0 0 20px rgba(234, 179, 8, 0.2); }
        .mod-sql:hover { box-shadow: inset 0 0 20px rgba(14, 165, 233, 0.05), 0 0 20px rgba(14, 165, 233, 0.2); }
        .mod-other:hover { box-shadow: inset 0 0 20px rgba(226, 232, 240, 0.05), 0 0 20px rgba(226, 232, 240, 0.1); }
        .mod-web:hover { box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.05), 0 0 20px rgba(56, 189, 248, 0.2); }
        .mod-data:hover { box-shadow: inset 0 0 20px rgba(168, 85, 247, 0.05), 0 0 20px rgba(168, 85, 247, 0.2); }

        /* Responsive */
        @media (max-width: 1200px) {
            .hero { flex-direction: column; }
            .hero-left, .hero-right { width: 100%; }
        }
        @media (max-width: 1000px) {
            .modules-grid { grid-template-columns: repeat(2, 1fr); }
            .tag-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 650px) {
            .hero-left { flex-direction: column; text-align: center; gap: 1.5rem; }
            .hero-cursive { text-align: center; }
            .feature-badges { justify-content: center; flex-wrap: wrap; }
            .modules-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        
        <!-- HERO SECTION -->
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
                    <h1 class="hero-title">Gagan <span class="name-yellow">Sir</span></h1>
                    <p class="hero-subtitle">Your Ultimate Learning Portal for Python, Data Structures, SQL, Data Analytics and Beyond.</p>
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

        <!-- MODULES GRID -->
        <div class="modules-grid">
            
            <a href="notes/python_programming_master_notes.html" class="mod-card mod-python">
                <div class="mod-icon"><i class="fa-brands fa-python"></i></div>
                <div class="mod-info"><h3>Python</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>
            
            <a href="java/master_notes_portal.html" class="mod-card mod-java">
                <div class="mod-icon"><i class="fa-brands fa-java"></i></div>
                <div class="mod-info"><h3>Java</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="govt/SSC_Master_Notes_Hub.html" class="mod-card mod-govt">
                <div class="mod-icon"><i class="fa-solid fa-building-columns"></i></div>
                <div class="mod-info"><h3>Govt Exams</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="notes/excel_complete_notes.html" class="mod-card mod-excel">
                <div class="mod-icon"><i class="fa-solid fa-file-excel"></i></div>
                <div class="mod-info"><h3>Excel</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="notes/powerbi_complete_notes.html" class="mod-card mod-pbi">
                <div class="mod-icon"><i class="fa-solid fa-chart-simple"></i></div>
                <div class="mod-info"><h3>Power BI</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="notes/sql_fundamentals_and_analytics_notes.html" class="mod-card mod-sql">
                <div class="mod-icon"><i class="fa-solid fa-database"></i></div>
                <div class="mod-info"><h3>SQL</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="notes/git_github_master_notes.html" class="mod-card mod-other">
                <div class="mod-icon"><i class="fa-solid fa-briefcase"></i></div>
                <div class="mod-info"><h3>Other Tools</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="full_stack/html/00_master_notes_portal.html" class="mod-card mod-web">
                <div class="mod-icon"><i class="fa-solid fa-globe"></i></div>
                <div class="mod-info"><h3>Web Development</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

            <a href="notes/sql_fundamentals_and_analytics_notes.html" class="mod-card mod-data">
                <div class="mod-icon"><i class="fa-solid fa-chart-line"></i></div>
                <div class="mod-info"><h3>Data Analytics</h3></div>
                <div class="mod-open">Open <i class="fa-solid fa-chevron-right"></i></div>
            </a>

        </div>
        
    </div>
</body>
</html>
"""

open('index.html', 'w', encoding='utf-8').write(index_html)
print("index.html rewritten successfully.")
