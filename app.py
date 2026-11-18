import streamlit as st
import google.generativeai as genai
from PIL import Image

# ---------------- CONFIG ----------------
API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="AI Biology Tutor", layout="wide")
st.title("🧠 AI Biology Interactive Tutor")

# ---------------- CACHE ----------------
if "ai_cache" not in st.session_state:
    st.session_state.ai_cache = {}

# ---------------- SAFE AI FUNCTION ----------------
def safe_ai(prompt, key):

    # Return cached response if already generated
    if key in st.session_state.ai_cache:
        return st.session_state.ai_cache[key]

    try:
        with st.spinner("AI is thinking... 🧠"):
            response = model.generate_content(prompt)

        result = response.text

        st.session_state.ai_cache[key] = result

        return result

    except Exception as e:
        return f"⚠️ AI Error: {e}"

# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "Choose Module",
    ["Home", "Lung Explorer", "Heart Explorer", "Cell Explorer", "Quiz"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("Welcome 👋")

    st.write(
        "Learn Biology using AI explanations, interactive 3D models, "
        "and quizzes designed for students."
    )

    st.success("Features")
    st.write("✔ AI Explanations")
    st.write("✔ Interactive 3D Models")
    st.write("✔ Biology Quiz")
    st.write("✔ Visual Learning")

# ---------------- LUNG ----------------
elif menu == "Lung Explorer":

    st.header("🫁 Human Lung Explorer")

    img = Image.open(
        r"C:/Users/punna/OneDrive/Desktop/AI_Biology_Tutor/images/lung.jpg.jpeg"
    )
    st.image(img, caption="Human Lung Diagram")

    st.caption("🖱️ Drag to rotate • Scroll to zoom")

    if st.button("Explain Lung"):
        lung_text = safe_ai(
            """
            Explain human lungs in detailed textbook style.

            Include:
            - trachea
            - bronchi
            - bronchioles
            - alveoli
            - gas exchange process
            - respiratory system
            - importance of lungs

            Write a detailed student-friendly paragraph.
            """,
            "lung_ai"
        )

        st.subheader("🧠 AI Explanation")
        st.write(lung_text)

    if "lung_ai" in st.session_state.ai_cache:
        st.subheader("🧠 AI Explanation")
        st.write(st.session_state.ai_cache["lung_ai"])

    st.subheader("🌐 3D Lung Model")

    st.components.v1.html(
        """
        <iframe width="100%" height="500"
        src="https://sketchfab.com/models/ce09f4099a68467880f46e61eb9a3531/embed"
        frameborder="0"
        allowfullscreen>
        </iframe>
        """,
        height=520
    )

# ---------------- HEART ----------------
elif menu == "Heart Explorer":

    st.header("❤️ Human Heart Explorer")

    img = Image.open(
        r"C:/Users/punna/OneDrive/Desktop/AI_Biology_Tutor/images/heart.jpg.jpeg"
    )
    st.image(img, caption="Human Heart Diagram")

    st.caption("🖱️ Drag to rotate • Scroll to zoom")

    if st.button("Explain Heart"):
        heart_text = safe_ai(
            """
            Explain the human heart in detailed textbook style.

            Include:
            - right atrium
            - left atrium
            - right ventricle
            - left ventricle
            - valves
            - blood circulation
            - oxygenated blood
            - deoxygenated blood

            Write a detailed student-friendly explanation.
            """,
            "heart_ai"
        )

        st.subheader("🧠 AI Explanation")
        st.write(heart_text)

    if "heart_ai" in st.session_state.ai_cache:
        st.subheader("🧠 AI Explanation")
        st.write(st.session_state.ai_cache["heart_ai"])

    st.subheader("🌐 3D Heart Model")

    st.components.v1.html(
        """
        <iframe width="100%" height="500"
        src="https://sketchfab.com/models/775d6629622740de8a5ed61a959c7506/embed"
        frameborder="0"
        allowfullscreen>
        </iframe>
        """,
        height=520
    )

# ---------------- CELL ----------------
elif menu == "Cell Explorer":

    st.header("🧬 Cell Structure Explorer")

    img = Image.open(
        r"C:/Users/punna/OneDrive/Desktop/AI_Biology_Tutor/images/cell.jpg.webp"
    )
    st.image(img, caption="Cell Diagram")

    st.caption("🖱️ Drag to rotate • Scroll to zoom")

    if st.button("Explain Cell"):
        cell_text = safe_ai(
            """
            Explain cell structure in detail.

            Include:
            - nucleus
            - mitochondria
            - cytoplasm
            - cell membrane
            - ribosomes
            - endoplasmic reticulum
            - Golgi apparatus

            Write a detailed explanation suitable for students.
            """,
            "cell_ai"
        )

        st.subheader("🧠 AI Explanation")
        st.write(cell_text)

    if "cell_ai" in st.session_state.ai_cache:
        st.subheader("🧠 AI Explanation")
        st.write(st.session_state.ai_cache["cell_ai"])

    st.subheader("🌐 3D Cell Model")

    st.components.v1.html(
        """
        <iframe width="100%" height="500"
        src="https://sketchfab.com/models/1f37ec86999a4c9289de207b9ca7435a/embed"
        frameborder="0"
        allowfullscreen>
        </iframe>
        """,
        height=520
    )

# ---------------- QUIZ ----------------
elif menu == "Quiz":

    st.header("🎯 Biology Quiz")

    q1 = st.radio(
        "1. What is the function of alveoli?",
        ["Digestion", "Gas exchange", "Blood pumping"]
    )

    q2 = st.radio(
        "2. Which organ pumps blood?",
        ["Lungs", "Heart", "Kidney"]
    )

    q3 = st.radio(
        "3. Basic unit of life is?",
        ["Tissue", "Organ", "Cell"]
    )

    q4 = st.radio(
        "4. Which part of the cell contains genetic material?",
        ["Cytoplasm", "Nucleus", "Cell membrane"]
    )

    q5 = st.radio(
        "5. What do lungs mainly do?",
        ["Pump blood", "Exchange gases", "Digest food"]
    )

    if st.button("Submit Quiz"):

        score = 0

        if q1 == "Gas exchange":
            score += 1

        if q2 == "Heart":
            score += 1

        if q3 == "Cell":
            score += 1

        if q4 == "Nucleus":
            score += 1

        if q5 == "Exchange gases":
            score += 1

        st.success(f"Your Score: {score}/5")

        if score == 5:
            st.balloons()
            st.write("Excellent! 🧠🔥")

        elif score >= 3:
            st.write("Good job 👍")

        else:
            st.write("Revise and try again 📚")