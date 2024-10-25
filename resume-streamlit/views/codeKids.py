import streamlit as st

# --- Independent Study Section ---
st.title("Computer Science Independent Study - Virginia Tech")
st.image("./assets/codekids.png", width=200)
# GitHub and Figma Links
st.subheader("Project Resources")
st.write("You can access the GitHub repository and the Figma mock-ups used throughout the project below:")

# Create buttons for GitHub and Figma
github_url = "https://github.com/codekids-vt/codekids"
website_url = "https://codekids.cs.vt.edu/"

st.link_button("CodeKids", website_url)
st.link_button("GitHub Repository", github_url)

# Description of the project
st.subheader("Project Overview")
st.write(
    """
    Since Spring 2024, I have been engaged in a CS Independent Study at Virginia Tech. This project focuses on developing 
    a fully functioning front-end using TypeScript, JavaScript, and React, incorporating event handlers and complex styling 
    within a hierarchical component structure (props, parents, and children).
    
    I make weekly commit changes to the main project branch on GitHub and utilize Figma to present mock-ups for potential 
    user interface revisions. Additionally, I am developing a full-stack website employing various data structures to create 
    interactive games and activities aimed at elementary school students (ages 6-11) with no prior experience in computer science.
    """
)

# Accomplishments section
st.subheader("Key Accomplishments")
st.write(
    """
    Over the course of this Independent Study, I've achieved several significant milestones:
    
    - **Developed a fully functioning front-end using TypeScript, JavaScript, and React**, implementing complex event handling and styling structures.
    - **Designed and deployed interactive educational tools** (games and activities) aimed at teaching computer science concepts to elementary school students, allowing for an engaging, hands-on learning experience.
    - **Resolved key technical challenges** such as implementing multi-selection features for interactive books and fixing UI/UX bugs related to layout and user input, significantly improving user interaction.
    - **Completed and published several educational resources**, including the "How the Internet Works" book, which translates complex internet concepts into an accessible format for young learners.
    - **Collaborated weekly using GitHub and Figma** to track progress and refine user interface designs, ensuring high-quality development with continuous feedback and improvements.
    """
)

# User Feedback
st.subheader("Provide Feedback")
st.write(
    """
    If you would like to provide feedback on any of the books or suggest new features, you can do so below:
    """
)

# Feedback text area
feedback = st.text_area("Enter your feedback or suggestions:")

# Submit button
if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.error("Please enter some feedback before submitting.")

