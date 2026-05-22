import streamlit as st
import google.generativeai as genai
from datetime import date
from dotenv import load_dotenv
import os

# =========================================
# Load Environment Variables
# =========================================
load_dotenv()

# =========================================
# Configure Gemini API
# =========================================
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# =========================================
# Gemini Model
# =========================================
model = genai.GenerativeModel(
    model_name="models/gemini-flash-latest"
)

# =========================================
# Streamlit Page Config
# =========================================
st.set_page_config(
    page_title="WWE Mayhem AI Live Ops Agent",
    page_icon="🤼",
    layout="wide"
)

# =========================================
# System Prompt
# =========================================
SYSTEM_PROMPT = """
You are the Lead Live Ops Designer and WWE lore expert for WWE Mayhem.

Create engaging 7-day WWE event calendars.

Requirements:
- Use real WWE rivalries and storylines
- Include event variety
- Exactly 7 days
- 1-2 events per day
- Use markdown formatting
"""

# =========================================
# Session State
# =========================================
if "calendar" not in st.session_state:
    st.session_state.calendar = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================
# App Title
# =========================================
st.title("🤼 WWE Mayhem AI Live Ops Agent")

st.markdown("Generate WWE-themed Live Ops calendars using Gemini AI")

st.divider()

# =========================================
# Sidebar Inputs
# =========================================
with st.sidebar:

    st.header("⚙️ Settings")

    start_date = st.date_input(
        "Week Start Date",
        value=date.today()
    )

    theme = st.text_input(
        "Weekly Theme",
        placeholder="Example: Bloodline Civil War"
    )

    generate_button = st.button("🚀 Generate Calendar")

# =========================================
# Generate Calendar ONLY on Button Click
# =========================================
if generate_button:

    if not theme:
        theme = "General WWE Roster"

    prompt = f"""
{SYSTEM_PROMPT}

Create a 7-day WWE Mayhem Live Ops calendar.

Start Date: {start_date}

Theme:
{theme}
"""

    try:

        with st.spinner("🔥 Booking matches..."):

            response = model.generate_content(prompt)

            st.session_state.calendar = response.text

        st.success("✅ Calendar Generated Successfully!")

    except Exception as e:

        st.error(f"Error: {e}")

# =========================================
# Display Calendar
# =========================================
if st.session_state.calendar:

    st.subheader("📅 WWE Live Ops Calendar")

    st.markdown(st.session_state.calendar)

    st.divider()

    # =========================================
    # Follow-Up Changes
    # =========================================
    st.subheader("✏️ Modify Calendar")

    followup_prompt = st.text_input(
        "Enter modification request",
        placeholder="Example: Make Day 3 about Cody Rhodes"
    )

    modify_button = st.button("🔄 Update Calendar")

    # =========================================
    # Update ONLY on Button Click
    # =========================================
    if modify_button and followup_prompt:

        update_prompt = f"""
Current Calendar:

{st.session_state.calendar}

Modification Request:
{followup_prompt}

Regenerate the FULL updated 7-day calendar.
"""

        try:

            with st.spinner("🎯 Updating Storyline..."):

                response = model.generate_content(update_prompt)

                st.session_state.calendar = response.text

            st.success("✅ Calendar Updated!")

            st.rerun()

        except Exception as e:

            st.error(f"Error: {e}")

    # =========================================
    # Download Markdown
    # =========================================
    st.divider()

    st.download_button(
        label="📥 Download Markdown",
        data=st.session_state.calendar,
        file_name=f"WWE_Mayhem_LiveOps_{date.today().strftime('%Y%m%d')}.md",
        mime="text/markdown"
    )

# =========================================
# Footer
# =========================================
st.divider()

st.caption("Built with Streamlit + Gemini AI")