import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "pages/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
snapBot = st.Page(
    "pages/snapBot.py",
    title="SnapBot",
    icon=":material/photo_camera:",
)

codeKids = st.Page(
    "pages/codeKids.py",
    title="CodeKids",
    icon=":material/family_restroom:",
)

workExperience = st.Page(
    "pages/work_experience.py",
    title="Work Experience",
    icon=":material/work:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, snapBot, codeKids, workExperience])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Home": [about_page, workExperience],
        "Projects": [snapBot, codeKids],
    }
)


# --- SHARED ON ALL PAGES ---
#st.logo(":material/computer:")
st.sidebar.markdown("✍🏽 By [Gabriel Holder](https://www.linkedin.com/in/gabrielholderr/)")


# --- RUN NAVIGATION ---
pg.run()