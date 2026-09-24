"""
Generates high-precision Japanese-styled Skill Matrix SVGs for both Dark and Light themes.
Features authentic Japanese Hanko seals, vector tech logos, and bilingual typography.
"""

def generate_svg(theme="dark"):
    is_dark = theme == "dark"
    bg_card = "#121018" if is_dark else "#FFFFFF"
    tile_bg = "#191624" if is_dark else "#F4F0E8"
    tile_border = "#2B2638" if is_dark else "#DCD5C5"
    hanko_bg = "#E0503D" if is_dark else "#C8382B"
    text_primary = "#E8E3D8" if is_dark else "#1C1B19"
    text_muted = "#8C867B" if is_dark else "#756F67"
    category_header_fill = "#E8E3D8" if is_dark else "#1C1B19"
    category_sub_fill = "#E0503D" if is_dark else "#C8382B"
    gold_accent = "#D4AF37" if is_dark else "#B8860B"

    # SVG header
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 430" width="100%" height="430" fill="none">
  <defs>
    <filter id="tile-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="{"#000000" if is_dark else "#888888"}" flood-opacity="{"0.3" if is_dark else "0.08"}" />
    </filter>
  </defs>

  <style>
    .font-mono {{ font-family: ui-monospace, 'SF Mono', 'Cascadia Code', 'Fira Code', Menlo, monospace; }}
    .font-jp {{ font-family: 'Hiragino Mincho ProN', 'Yu Mincho', 'Noto Serif JP', 'Source Han Serif', serif; }}
    .skill-tile {{ transition: all 0.25s ease; }}
  </style>

  <!-- Background Base Container -->
  <rect x="0" y="0" width="880" height="430" rx="14" fill="{bg_card}" stroke="{tile_border}" stroke-width="1.2" />

  <!-- Top Decorative Header with Japanese Mon pattern -->
  <g transform="translate(24, 20)">
    <circle cx="8" cy="8" r="4" fill="{category_sub_fill}" />
    <text x="20" y="12" class="font-jp" font-size="14" font-weight="700" fill="{category_header_fill}" letter-spacing="1.5">技術兵器廠 <tspan class="font-mono" font-size="11" font-weight="400" fill="{category_sub_fill}">// SKILLS &amp; ARSENAL</tspan></text>
    <text x="832" y="12" class="font-mono" font-size="10" fill="{text_muted}" text-anchor="end">AUTHENTIC JAPANESE MON STAMP MATRIX · 17 MODULES</text>
    <line x1="0" y1="24" x2="832" y2="24" stroke="{tile_border}" stroke-width="1" />
  </g>
'''

    # Categories definitions
    categories = [
        {
            "name": "言語",
            "en": "PROGRAMMING LANGUAGES",
            "y": 62,
            "skills": [
                {
                    "kanji": "核", "name": "C", "sub": "Core Systems",
                    "logo": '''<circle cx="12" cy="12" r="11" fill="#A8B9CC" /><path d="M16 8.5C14.8 7.3 12.8 7 11 7.8C8.8 8.8 7.5 11 7.5 13.5C7.5 16.5 9.5 18.5 12.5 18.5C14.5 18.5 16 17.5 17 16" stroke="#004482" stroke-width="2.2" stroke-linecap="round" fill="none" />'''
                },
                {
                    "kanji": "刃", "name": "C++", "sub": "Blade Speed",
                    "logo": '''<polygon points="12,1 22,6.5 22,17.5 12,23 2,17.5 2,6.5" fill="#00599C" /><path d="M9.5 8C8.5 7.2 7 7.2 5.8 7.8C4.5 8.5 3.8 9.8 3.8 11.8C3.8 14.2 5 15.5 7.2 15.5C8.4 15.5 9.5 14.8 10 14" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" fill="none" /><path d="M12.5 11.8H15.5M14 10.3V13.3M17.5 11.8H20.5M19 10.3V13.3" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" />'''
                },
                {
                    "kanji": "蛇", "name": "Python", "sub": "Data & ML",
                    "logo": '''<path d="M11.8 2.2C6.8 2.2 7.1 4.4 7.1 4.4L7.1 6.6H12V7.4H4.5C4.5 7.4 2 7.1 2 12C2 16.8 4.2 16.6 4.2 16.6H5.7L5.7 14.3C5.7 11.6 8.1 11.6 8.1 11.6H13C13 11.6 15.2 11.7 15.2 9.5C15.2 7.3 15.2 4.4 15.2 4.4C15.2 4.4 15.5 2.2 11.8 2.2ZM9.4 3.7C9.9 3.7 10.3 4.1 10.3 4.6C10.3 5.1 9.9 5.5 9.4 5.5C8.9 5.5 8.5 5.1 8.5 4.6C8.5 4.1 8.9 3.7 9.4 3.7Z" fill="#387EB8"/><path d="M12.2 21.8C17.2 21.8 16.9 19.6 16.9 19.6L16.9 17.4H12V16.6H19.5C19.5 16.6 22 16.9 22 12C22 7.2 19.8 7.4 19.8 7.4H18.3L18.3 9.7C18.3 12.4 15.9 12.4 15.9 12.4H11C11 11.6 8.8 12.3 8.8 14.5C8.8 16.7 8.8 19.6 8.8 19.6C8.8 19.6 8.5 21.8 12.2 21.8ZM14.6 20.3C14.1 20.3 13.7 19.9 13.7 19.4C13.7 18.9 14.1 18.5 14.6 18.5C15.1 18.5 15.5 18.9 15.5 19.4C15.5 19.9 15.1 20.3 14.6 20.3Z" fill="#FFE052"/>'''
                },
                {
                    "kanji": "型", "name": "TypeScript", "sub": "Strict Static",
                    "logo": '''<rect x="2" y="2" width="20" height="20" rx="4" fill="#3178C6" /><path d="M5.5 8.5H12M8.7 8.5V17M13.5 15.2C14 16.2 15.2 17 16.8 17C18.5 17 19.5 16 19.5 14.7C19.5 13.3 18.4 12.7 16.7 12.1C14.8 11.4 13.8 10.6 13.8 9.2C13.8 7.6 15.1 6.5 17 6.5C18.3 6.5 19.3 7.1 19.8 8" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" fill="none" />'''
                },
                {
                    "kanji": "電", "name": "JavaScript", "sub": "Async Dynamic",
                    "logo": '''<rect x="2" y="2" width="20" height="20" rx="4" fill="#F7DF1E" /><path d="M7 14.8C7.5 15.8 8.4 16.5 9.5 16.5C10.8 16.5 11.5 15.7 11.5 14.2V8.5M13.8 14.8C14.4 15.8 15.6 16.5 17 16.5C18.6 16.5 19.8 15.5 19.8 14.2C19.8 12.8 18.7 12.2 17 11.6C15.2 10.9 14.3 10.2 14.3 8.9C14.3 7.5 15.5 6.5 17.2 6.5C18.5 6.5 19.4 7.1 19.8 8" stroke="#000000" stroke-width="2" stroke-linecap="round" fill="none" />'''
                }
            ]
        },
        {
            "name": "基盤",
            "en": "RUNTIMES & BACKEND FRAMEWORKS",
            "y": 152,
            "skills": [
                {
                    "kanji": "炎", "name": "Bun", "sub": "Fast Runtime",
                    "logo": '''<path d="M12 4C7.5 4 4 7.5 4 12C4 16.5 7.5 20 12 20C16.5 20 20 16.5 20 12C20 7.5 16.5 4 12 4Z" fill="#FBF0DF" stroke="#D1C3B7" stroke-width="1.2" /><circle cx="9" cy="11" r="1.5" fill="#1C1B19" /><circle cx="15" cy="11" r="1.5" fill="#1C1B19" /><circle cx="7.5" cy="13" r="1.2" fill="#FFAAA6" /><circle cx="16.5" cy="13" r="1.2" fill="#FFAAA6" /><path d="M10.5 14.5C11.2 15.2 12.8 15.2 13.5 14.5" stroke="#1C1B19" stroke-width="1.2" stroke-linecap="round" fill="none" />'''
                },
                {
                    "kanji": "網", "name": "Node.js", "sub": "Event Driven",
                    "logo": '''<polygon points="12,2 21,7.2 21,17.8 12,23 3,17.8 3,7.2" fill="#339933" /><path d="M7.5 16V9.5L12 7L16.5 9.5V14.5L12 17L9.5 15.5V11.5L14.5 9V13.5" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" />'''
                },
                {
                    "kanji": "迅", "name": "FastAPI", "sub": "High Perf APIs",
                    "logo": '''<circle cx="12" cy="12" r="10" fill="#009688" /><path d="M13 3L6 13H12L11 21L18 11H12L13 3Z" fill="#FFFFFF" />'''
                },
                {
                    "kanji": "瓶", "name": "Flask", "sub": "Micro Engine",
                    "logo": '''<path d="M10 3V8L5 18C4 20 5.5 21.5 7.5 21.5H16.5C18.5 21.5 20 20 19 18L14 8V3H10Z" fill="none" stroke="{category_sub_fill}" stroke-width="1.8" /><path d="M6.5 16C8 15 11 17 13 16C15 15 16.5 15.5 17.5 16" stroke="{category_sub_fill}" stroke-width="1.5" stroke-linecap="round" fill="none" /><circle cx="10" cy="18" r="1" fill="{category_sub_fill}" /><circle cx="14" cy="17.5" r="0.8" fill="{category_sub_fill}" />'''
                }
            ]
        },
        {
            "name": "知能",
            "en": "ARTIFICIAL INTELLIGENCE & DATA",
            "y": 242,
            "skills": [
                {
                    "kanji": "鎖", "name": "LangChain", "sub": "Agent Chains",
                    "logo": '''<rect x="2" y="2" width="20" height="20" rx="5" fill="#1C3C3C" /><path d="M6 14L10 10M14 10L18 14M8 12C8 9.5 10.5 7 13 7M11 17C13.5 17 16 14.5 16 12" stroke="#2ED1A2" stroke-width="1.8" stroke-linecap="round" fill="none" /><circle cx="14" cy="9" r="1.5" fill="#2ED1A2" />'''
                },
                {
                    "kanji": "索", "name": "RAG & Ollama", "sub": "Vector Search",
                    "logo": '''<circle cx="12" cy="12" r="10" fill="#1E1E2E" stroke="{gold_accent}" stroke-width="1.2" /><circle cx="12" cy="12" r="6" stroke="#E0503D" stroke-width="1" stroke-dasharray="2 2" fill="none" /><circle cx="12" cy="12" r="2.5" fill="{gold_accent}" /><path d="M12 2V6M12 18V22M2 12H6M18 12H22" stroke="{gold_accent}" stroke-width="1.2" />'''
                },
                {
                    "kanji": "智", "name": "scikit-learn", "sub": "Predictive ML",
                    "logo": '''<circle cx="9" cy="9" r="6" fill="#F89939" opacity="0.85" /><circle cx="15" cy="15" r="6" fill="#3499CD" opacity="0.85" /><path d="M6 18L18 6" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" />'''
                },
                {
                    "kanji": "算", "name": "Pandas", "sub": "Data Frames",
                    "logo": '''<rect x="3" y="4" width="4" height="16" rx="2" fill="#150458" /><rect x="8" y="7" width="4" height="13" rx="2" fill="#E70488" /><rect x="13" y="4" width="4" height="16" rx="2" fill="#00A3E0" /><rect x="18" y="9" width="3" height="11" rx="1.5" fill="#FFD43B" />'''
                }
            ]
        },
        {
            "name": "兵站",
            "en": "STORAGE, TOOLS & INFRASTRUCTURE",
            "y": 332,
            "skills": [
                {
                    "kanji": "葉", "name": "MongoDB", "sub": "Document NoSQL",
                    "logo": '''<path d="M12 2C12 2 6 7 6 13C6 17 8.5 20.5 12 22C15.5 20.5 18 17 18 13C18 7 12 2 12 2Z" fill="#13AA52" /><path d="M12 3V21C11.5 20.5 11 19 11 13C11 8 12 3 12 3Z" fill="#116149" />'''
                },
                {
                    "kanji": "魚", "name": "MySQL", "sub": "Relational SQL",
                    "logo": '''<circle cx="12" cy="12" r="10" fill="#00758F" /><path d="M7 15C9 13.5 11 13 14 13.5C16 14 17.5 13 18 11.5C18.5 10 17.5 9 15.5 9C13 9 11.5 11 9 11.5C7.5 11.8 6.5 11 6 10" stroke="#F29111" stroke-width="1.8" stroke-linecap="round" fill="none" />'''
                },
                {
                    "kanji": "枝", "name": "Git & GitHub", "sub": "Version Tree",
                    "logo": '''<rect x="3" y="3" width="18" height="18" rx="4" transform="rotate(45 12 12)" fill="#F05032" /><path d="M12 7V17M12 12L15 9" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" fill="none" /><circle cx="12" cy="7" r="2" fill="#FFFFFF" /><circle cx="12" cy="17" r="2" fill="#FFFFFF" /><circle cx="15" cy="9" r="2" fill="#FFFFFF" />'''
                },
                {
                    "kanji": "極", "name": "Linux & OS", "sub": "Kernel Runtime",
                    "logo": '''<rect x="2" y="2" width="20" height="20" rx="4" fill="#222222" /><path d="M6 7L10 11L6 15" stroke="{category_sub_fill}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" /><line x1="12" y1="15" x2="18" y2="15" stroke="{category_sub_fill}" stroke-width="2" stroke-linecap="round" />'''
                }
            ]
        }
    ]

    for cat in categories:
        cy = cat["y"]
        cname = cat["name"]
        cen = cat["en"]
        skills = cat["skills"]
        num_skills = len(skills)

        # Category Header
        svg += f'''
  <!-- Category: {cname} // {cen} -->
  <g transform="translate(24, {cy})">
    <text x="0" y="10" class="font-jp" font-size="12" font-weight="700" fill="{category_header_fill}">{cname} <tspan class="font-mono" font-size="9.5" font-weight="400" fill="{text_muted}">// {cen}</tspan></text>
  </g>
'''

        # Render Skills
        tile_y = cy + 18
        if num_skills == 5:
            tile_w = 158
            gap = 10.5
        else:
            tile_w = 200.5
            gap = 10

        for i, sk in enumerate(skills):
            tile_x = 24 + i * (tile_w + gap)
            kanji = sk["kanji"]
            name = sk["name"]
            sub = sk["sub"]
            logo = sk["logo"]

            svg += f'''
  <g transform="translate({tile_x:.1f}, {tile_y})" class="skill-tile" filter="url(#tile-shadow)">
    <!-- Base Tile -->
    <rect x="0" y="0" width="{tile_w:.1f}" height="46" rx="8" fill="{tile_bg}" stroke="{tile_border}" stroke-width="1.1" />
    
    <!-- Japanese Hanko Stamp (Kanji Seal) -->
    <rect x="7" y="8" width="30" height="30" rx="5" fill="{hanko_bg}" />
    <text x="22" y="28" class="font-jp" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">{kanji}</text>
    
    <!-- Tech Logo Vector -->
    <g transform="translate(44, 11)">
      {logo}
    </g>

    <!-- Labels -->
    <text x="74" y="22" class="font-mono" font-size="11.5" font-weight="700" fill="{text_primary}">{name}</text>
    <text x="74" y="34" class="font-mono" font-size="8.5" fill="{text_muted}">{sub}</text>
  </g>
'''

    svg += '</svg>\n'
    return svg

# Generate both
with open("d:/git/Pratyaksh0x1/assets/skills-matrix-dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("dark"))
print("Generated skills-matrix-dark.svg successfully")

with open("d:/git/Pratyaksh0x1/assets/skills-matrix-light.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("light"))
print("Generated skills-matrix-light.svg successfully")
