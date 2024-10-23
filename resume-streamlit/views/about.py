import streamlit as st

#from forms.contact import contact_form

# Custom CSS to round the corners of the image
st.markdown(
    """
    <style>
    .round-img {
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# @st.experimental_dialog("Contact Me")
# def show_contact_form():
#     contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/dev_pic.png", width=230)

with col2:
    st.title("Gabriel Holder - Software Engineer", anchor=False)
    st.write(
        ""
    )
    # if st.button("✉️ Contact Me"):
    #     show_contact_form()

st.link_button("Resume", "https://drive.google.com/file/d/1X-VZmn3XdoQb2CEvvsy-gTkqLIpK2VCF/view")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 3 years of industry software engineering experience
    - Hands-on experience and knowledge in Java and TypeScript/React
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Java, Python, C, ServiceNow, VBA
    - Logistical: Agile Methodology, JIRA, Confluence
    - Databases and Modeling: Memory management, linear regression, binary decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)

# --- Eductation ---
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - Bachelors: Virginia Tech
    - Major: Computer Science
    - Minor: Mathematics
    - Year: Senior Year
    - Undergraduate Graduation: May 2025
    """
)