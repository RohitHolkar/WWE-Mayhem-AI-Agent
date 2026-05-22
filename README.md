# 🤼 WWE Mayhem AI Live Ops Calendar Generator

An AI-powered Live Ops Calendar Generator designed for WWE Mayhem, built using Python, Streamlit, and Large Language Models (LLMs). The application generates engaging 7-day in-game event calendars inspired by real WWE storylines, rivalries, factions, and championship narratives.

The project demonstrates practical implementation of Prompt Engineering, Generative AI, Interactive Web Applications, and Dynamic Content Generation for gaming Live Operations.

---

# 📌 Project Overview

This application acts as an AI-powered Live Ops Designer for WWE Mayhem. Users can generate themed weekly event calendars by providing a storyline or WWE theme such as:

- The Bloodline Civil War
- WrestleMania Season
- Cody Rhodes Championship Storyline
- Judgment Day Rivalries
- CM Punk Return

The generated calendar includes:
- Daily WWE-themed events
- Different event categories
- Storyline-driven gameplay descriptions
- Interactive regeneration and customization

---

# 🚀 Key Features

- AI-generated 7-day WWE event calendars
- Interactive Streamlit web interface
- Storyline-based event generation
- Dynamic event customization
- Markdown export functionality
- Prompt-engineered LLM responses
- Real WWE narrative integration

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Web Application UI |
| Gemini API / OpenAI API | AI Content Generation |
| Prompt Engineering | Structured LLM Responses |
| Markdown | Exportable Calendar Format |
| dotenv | Secure API Key Management |

---

# 📂 Project Structure

```bash
WWE_Mayhem_AI_App/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/WWE-Mayhem-AI-Agent.git
```

---

## 2. Navigate to the Project Directory

```bash
cd WWE-Mayhem-AI-Agent
```

---

## 3. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root directory.

### For Gemini API

```env
GOOGLE_API_KEY=your_api_key_here
```

### For OpenAI API

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 6. Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 🧠 Prompt Engineering Approach

The project uses a carefully designed system prompt to simulate the behavior of a professional WWE Live Ops Designer.

The prompt engineering strategy focuses on:

## ✅ Role-Based Prompting
The model is assigned a domain-specific role:

> “Lead Live Ops Designer and WWE lore expert for WWE Mayhem”

This improves WWE-specific creativity and narrative quality.

---

## ✅ Structured Output Enforcement
The prompt enforces:
- Exactly 7 days
- 1–2 events per day
- Consistent markdown formatting
- Defined event categories

This ensures clean and exportable outputs.

---

## ✅ Event-Type Constraints
Only approved event formats are allowed:

- Tournament
- Login Streak
- Special Match
- Challenge Mode
- Character Spotlight
- Boss Raid
- Limited-Time Mode

This maintains gameplay realism and consistency.

---

## ✅ Contextual WWE Storyline Integration
The model is guided to incorporate:
- WWE factions
- Current rivalries
- Championship arcs
- WrestleMania narratives
- Superstar feuds

This significantly improves thematic authenticity.

---

## ✅ Regenerative Conversation Design
The AI is instructed to regenerate the complete calendar after every modification request, ensuring consistency across all generated days.

---

# 🏆 WWE Storylines Incorporated

The application integrates real WWE narratives and storytelling elements into event generation.

## Example Storylines Used

### 🔥 The Bloodline Civil War
- Roman Reigns vs Solo Sikoa
- Tribal Chief storyline conflicts
- Bloodline faction warfare

---

### 🔥 Cody Rhodes Championship Storyline
- “Finish the Story” narrative
- Championship redemption arc
- WrestleMania-inspired progression

---

### 🔥 Judgment Day Rivalries
- Damian Priest leadership conflicts
- Finn Balor faction tension
- Rhea Ripley dominance storylines

---

### 🔥 CM Punk Return
- Return-themed challenge events
- Rivalry-driven special matches
- Surprise comeback narratives

---

### 🔥 Women’s Division Storylines
- Rhea Ripley vs Liv Morgan
- Championship-focused challenge modes
- Character spotlight events

---

# 📅 Sample Weekly Calendar

## Day 1
- **Event Name:** Bloodline Ascension  
- **Event Type:** Tournament  
- **Description:** Compete in a faction-based tournament inspired by The Bloodline Civil War and battle for Tribal dominance.

---

## Day 2
- **Event Name:** Cody’s Redemption  
- **Event Type:** Character Spotlight  
- **Description:** Relive Cody Rhodes’ championship journey through exclusive story-driven matches and progression rewards.

---

## Day 3
- **Event Name:** Judgment Day Chaos  
- **Event Type:** Special Match  
- **Description:** Experience internal faction warfare as tensions rise within Judgment Day in high-stakes encounters.

---

## Day 4
- **Event Name:** Best in the World Returns  
- **Event Type:** Limited-Time Mode  
- **Description:** Celebrate CM Punk’s explosive return with exclusive comeback-inspired gameplay events.

---

## Day 5
- **Event Name:** Rhea’s Dominance  
- **Event Type:** Boss Raid  
- **Description:** Challenge Rhea Ripley in a high-difficulty raid featuring elite women’s division rewards.

---

## Day 6
- **Event Name:** WrestleMania Clash  
- **Event Type:** Challenge Mode  
- **Description:** Participate in WrestleMania-inspired legendary encounters and unlock premium rewards.

---

## Day 7
- **Event Name:** Champion’s Legacy  
- **Event Type:** Login Streak  
- **Description:** Complete the weekly login streak to unlock exclusive superstar shards and bonus items.

---

# 📦 Export Functionality

The application supports exporting generated calendars in:

- Markdown (`.md`)

This enables easy sharing, documentation, and content reuse.

---

# 🔒 Security & Environment Management

Sensitive API credentials are securely managed using environment variables through `.env` configuration files.

Example:

```env
GOOGLE_API_KEY=your_api_key
```

The `.env` file is excluded from version control using `.gitignore`.

---

# 🚀 Future Enhancements

- PDF export functionality
- Multi-theme event generation
- Real-time WWE API integration
- Admin dashboard for Live Ops teams
- Drag-and-drop event editing
- User authentication
- Analytics and engagement tracking
- Database integration

---

# 👨‍💻 Author

Developed by Rohit Holkar

---

# 📜 License

This project is developed for educational and demonstration purposes.
