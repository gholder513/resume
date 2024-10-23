import streamlit as st

# --- WORK EXPERIENCE SECTION ---
st.title("Work Experience")

# Boeing
col1, col2 = st.columns([2, 1])  # Create two columns, with more width for the text (col1)
with col1:
    st.subheader("Boeing:\nSoftware Engineering Intern (May 2024 - August 2024)")
    st.write(
        """
        - Merged pull requests for 8 stories over a 10-week internship period.
        - Performed 5+ pull request reviews for full-time and senior developer pull requests.
        - Used a tech stack consisting of Java, Jira, Bitbucket, Confluence, SonarQube, and others to add functionality to the user interface for our product.
        - Created stories to enhance our product and collaborated with the Product Owner to consistently meet sprint deadlines, ensuring timely releases.
        """
    )
with col2:
    st.image("./assets/boeing.png", width=400)

# NTTDATA
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("NTTDATA:\nSoftware Engineering Intern (May 2023 - August 2023)")
    st.write(
        """
        - Security Clearance: Secret Level DHS.
        - Worked on the US Customs and Border Protection (CBP) contract.
        - Developed and maintained a web application (CBP Business Connection).
        """)
    st.link_button("Business Connection Web App", "https://cbpbusinessconnection.cbp.dhs.gov/vmp?id=vmpindex")
    st.write(
        """
        - Tested functionality using ServiceNow, JavaScript, HTML, and CSS.
        - Collaborated in sprints on Jira stories with team members, following the Agile Scrum methodology.
        - Created front-end web flow diagrams to improve user navigation.
        """
    )
with col2:
    st.image("./assets/nttdata.png", width=300)

# Logistics Applications Inc.
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Logistics Applications Inc.:\nDevOps Intern (May 2021 – August 2021)")
    st.write(
        """
        - Supported Senior Systems Administrator on a Department of Homeland Security IT project.
        - Gained hands-on experience with CPU and GPU performance optimization across various models.
        """
    )
with col2:
    st.image("./assets/lai.png", width=200)

# ESPN - ACCN
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("ESPN - ACCN - Production Assistant (August 2021 – Present, Part-Time)")
    st.write(
        """
        - Created trailers for ESPNW social media accounts using Adobe Premiere Pro.
        - Served as a Division 1 Football Replay Operator for the Emmy-winning Virginia Tech broadcast crew.
        - Nationally televised live action camera operator and replay technician for ESPN2 and ACC Network.
        """
    )
with col2:
    st.image("./assets/espn.png", width=300)

# Virginia Tech - Undergraduate Teaching Assistant
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Tenure at Virginia Tech & Leadership Experience\n")
    st.subheader("Virginia Tech Computer Science Department:\nUndergraduate Teaching Assistant (Spring 2024 - Present)")
    st.write(
        """
        - Teach over 500 students in Data Structures & Algorithms (via Java) and Computer Organization II.
        - Topics covered include Memory Management, Time Complexity, Algorithm Analysis, Data Structures (e.g., Hash Tables, Linked Lists), and RISC-V instruction set programming.
        """
    )
with col2:
    st.image("./assets/vt_computer_science.png", width=400)

# Virginia Tech - Independent Study
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Virginia Tech Computer Science Department:\nIndependent Study (Spring 2024 - Present)")
    st.write(
        """
        - Developed front-end using TypeScript, JavaScript, and React, with complex styling and hierarchical component structures.
        - Committed weekly changes to the project’s GitHub repository.
        - Used Figma for weekly mock-ups and user interface revisions.
        - Developed a full-stack website for elementary students, introducing them to computer science.
        """
    )

# Computer Science Careers Club
st.write("\n")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Virginia Tech - Director of Logistics, Computer Science Careers Club (October 2022 – Present)")
    st.write(
        """
        - Led events to enhance underclassmen technical skills (e.g., Coding Practice Seminars, Leetcode Workshops).
        - Coordinated with recruiters to arrange mixers and other networking events.
        - Worked with Virginia Tech alumni and the Computer Science department to organize guest speaker events and create job opportunities.
        """
    )
with col2:
    st.write("")  # No image provided
