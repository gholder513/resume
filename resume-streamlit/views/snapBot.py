import streamlit as st
st.title("SnapBot")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/snapbot_logo.png", width=230)

with col2:
    st.title("SnapBot - Automated Mouse Clicking Tool", anchor=False)
    st.write(
        "An automated mouse-clicking tool that allows users to record mouse positions and replay clicks."
    )
    st.link_button("Snap App", "https://github.com/gholder513/Snapscore")
    st.link_button("User Guide", "https://www.notion.so/SnapChat-Bot-Documentation-127a4ce68431806aba13e4f436f153fc?pvs=4")
    st.link_button("Sign-In", "https://web.snapchat.com/")


# --- DESCRIPTION ---
st.write("\n")
st.subheader("Description", anchor=False)
st.write(
    """
    The SnapBot is an automated mouse-clicking tool that allows users to record specific mouse positions 
    and replay clicks at those positions for a defined number of iterations or indefinitely. It provides 
    a graphical user interface (GUI) built using `tkinter`, with customizable hotkeys, click delays, and control 
    options for the auto-clicker process. The SnapBot supports multi-threading, ensuring smooth operation.
    """
)

# --- KEY FUNCTIONALITIES ---
st.write("\n")
st.subheader("Key Functionalities", anchor=False)
st.write(
    """
    - **Auto-Clicking**: Automatically click at recorded positions for a set number of iterations or indefinitely.
    - **Recording Mouse Positions**: Activate the recording mode to store global mouse positions for future auto-clicking.
    - **Customizable Hotkeys**: Set hotkeys for recording, starting, and stopping the auto-clicker.
    - **Iteration Control**: Specify the number of iterations for the auto-clicker. Runs indefinitely if none are specified.
    - **Delay Adjustment**: Use a slider to adjust the delay between consecutive clicks (0.1 to 3 seconds).
    - **Click Position Management**: View and clear recorded click positions via the GUI.
    """
)

# --- MODULES & LIBRARIES ---
st.write("\n")
st.subheader("Modules and Libraries Used", anchor=False)
st.write(
    """
    - **pyautogui**: Automates mouse movements and clicks.
    - **tkinter**: Provides the graphical user interface.
    - **threading**: Ensures the application remains responsive during background tasks.
    - **configparser**: Reads and writes the configuration file for hotkey settings.
    - **keyboard**: Detects global key events for controlling the auto-clicker.
    """
)

# --- CONFIGURATION FILE ---
st.write("\n")
st.subheader("Configuration File (Config.ini)", anchor=False)
st.write(
    """
    The configuration file stores customized hotkey settings for recording, starting, and stopping SnapBot. 
    If the file is missing, it will be automatically created.
    
    **Default Hotkeys:**
    - Record: `enter`
    - Start: `space`
    - Stop: `ctrl`
    """
)

# --- USAGE INSTRUCTIONS ---
st.write("\n")
st.subheader("Usage Instructions", anchor=False)
st.write(
    """
    **Starting the Auto-Clicker**:
    - Use the "Record Position" button to record mouse positions.
    - Specify the number of iterations or leave it blank for infinite clicking.
    - Click the "Start/Stop" button to begin the auto-clicker.
    
    **Stopping the Auto-Clicker**:
    - Press the stop hotkey (`ctrl` by default) or click the "Stop" button in the GUI.
    
    **Adjusting Delay**:
    - Use the delay slider to set the delay between clicks (default: 0.1 seconds).
    
    **Customizing Hotkeys**:
    - Click the "Change Hotkeys" button in the GUI to assign new hotkeys for recording, starting, and stopping the auto-clicker.
    
    **Viewing and Clearing Recorded Positions**:
    - Recorded positions are displayed in the GUI. Click "Clear Positions" to remove all recorded positions.
    """
)
