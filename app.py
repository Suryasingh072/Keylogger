import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Keylogger Research Demo", page_icon="🔐", layout="wide")

st.title("🔐 Keylogger Research — Safe Demo")
st.write("Yeh project ek **educational demo** hai jo keylogging ke concept ko safe environment me samjhata hai. "
         "Yeh koi actual keylogger nahi hai — yeh sirf aapke Streamlit app ke andar likhe gaye text ko monitor karta hai.")

st.sidebar.header("📋 Menu")
page = st.sidebar.radio("Select Section", ["Overview", "Live Typing Demo", "Data Log", "About Project"])

# Directory to store logs
LOG_FILE = "demo_logs.csv"
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Typed_Text"])
    df.to_csv(LOG_FILE, index=False)

# ---- Overview ----
if page == "Overview":
    st.subheader("📘 Understanding Keyloggers (For Research & Awareness)")
    st.markdown("""
    - **Keylogger** ek aisa software hota hai jo user ke keyboard inputs ko silently record karta hai.  
    - Iska use **malicious** (data theft) ya **ethical** (security analysis, parental control) purpose se hota hai.  
    - Research purpose ke liye hum sirf yeh samajhte hain ki data capture aur security breach kaise avoid karein.

    ### ⚠️ Ethical Use Only
    Yeh demo sirf **cybersecurity research aur awareness** ke liye banaya gaya hai.  
    Kisi system me bina permission ke keylogger chalana **illegal** hai (IT Act ke tahat punishable offense).
    """)

# ---- Live Typing Demo ----
elif page == "Live Typing Demo":
    st.subheader("💻 Type Something Below — Safe Simulation")
    st.write("Yahaan likha gaya text locally record hota hai aur koi bhi background capture nahi hota.")

    user_input = st.text_area("Type here...", height=150)
    if st.button("Log This Entry"):
        if user_input.strip() != "":
            new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input]],
                                     columns=["Timestamp", "Typed_Text"])
            old_df = pd.read_csv(LOG_FILE)
            updated_df = pd.concat([old_df, new_entry], ignore_index=True)
            updated_df.to_csv(LOG_FILE, index=False)
            st.success("✅ Text logged successfully!")
        else:
            st.warning("⚠️ Please type something first!")

# ---- Data Log ----
elif page == "Data Log":
    st.subheader("🗂️ Logged Data (Demo)")
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        st.dataframe(df)
        if st.button("Clear Logs"):
            df = pd.DataFrame(columns=["Timestamp", "Typed_Text"])
            df.to_csv(LOG_FILE, index=False)
            st.success("🧹 Logs cleared!")
    else:
        st.info("No logs available yet.")

# ---- About Project ----
elif page == "About Project":
    st.subheader("📄 About this Project")
    st.markdown("""
    - **Project Name:** Keylogger Research — Safe Demo  
    - **Framework:** Streamlit (Python)  
    - **Goal:** To demonstrate keystroke tracking concept safely in a controlled environment.  
    - **Developer:** Surya Pratap Singh (for educational purpose)

    ### 🧩 How It Works
    1. User text ko app ke andar type karta hai.  
    2. App usko timestamp ke sath ek CSV file (`demo_logs.csv`) me store karta hai.  
    3. User logs ko dekh ya clear kar sakta hai.  

    ### ☁️ Deployment Guide
    1. Create a repo with `app.py` and `requirements.txt`.  
    2. Example `requirements.txt`:
       ```
       streamlit
       pandas
       ```
    3. Run locally:
       ```bash
       pip install -r requirements.txt
       streamlit run app.py
       ```
    4. Or deploy on [Streamlit Cloud](https://share.streamlit.io).

    ⚠️ Note: Yeh app real key capture nahi karta — sirf input text area se data leta hai.
    """)
