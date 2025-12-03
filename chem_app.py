import streamlit as st

# ----------------- PAGE SETUP -----------------
st.set_page_config(
    page_title="Smart Chemistry Lab",
    page_icon="🧪",
    layout="wide",
)

# ----------------- THEME / CSS -----------------
st.markdown(
    """
    <style>
    /* Page background – soft cream like the poster */
    .stApp {
        background: #f7f1ee;
        color: #3b2f33;
        font-family: "Helvetica Neue", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main title – poster pink */
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #f25b9a;
        text-align: center;
        letter-spacing: 0.03em;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        text-align: center;
        font-size: 0.95rem;
        color: #5a4a4e;
        margin-bottom: 1.8rem;
    }

    /* Section headings – same pink as poster headings */
    .section-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #f25b9a;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.4rem;
    }

    /* Card-style boxes */
    .card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
        border: 1px solid #f0dbe7;
        margin-bottom: 0.8rem;
        font-size: 0.96rem;
        line-height: 1.5;
    }

    /* Bullet list spacing */
    .card ul {
        padding-left: 1.2rem;
    }

    /* Pink info pill */
    .pill {
        display: inline-block;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        background: #fbe3f0;
        color: #c53f7d;
        font-weight: 600;
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    /* Predict button – pink gradient like the poster accent */
    .stButton > button {
        background: linear-gradient(135deg, #f25b9a, #f89cc7);
        color: white;
        border-radius: 999px;
        border: none;
        padding: 0.5rem 2.4rem;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 10px rgba(242,91,154,0.35);
    }
    .stButton > button:hover {
        filter: brightness(1.05);
    }

    /* Safety message boxes */
    .safe-box {
        background: #e6f7ea;
        border-left: 6px solid #4caf50;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }

    .danger-box {
        background: #ffe8f0;
        border-left: 6px solid #e53967;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }

    .safe-label {
        font-weight: 800;
        color: #2e7d32;
    }
    .danger-label {
        font-weight: 800;
        color: #c2185b;
    }

    /* Make inputs a little rounder */
    .stTextInput > div > div > input {
        border-radius: 999px;
    }
    .stSelectbox > div > div {
        border-radius: 999px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- TITLE -----------------
st.markdown('<div class="main-title">SMART CHEMISTRY LAB</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Using Artificial Intelligence for Safer Experiments</div>',
    unsafe_allow_html=True,
)

st.markdown("---")

# ----------------- LAYOUT -----------------
col_left, col_mid, col_right = st.columns([1.1, 1.1, 1.1])

# ---------- LEFT: Problem & AI Solution ----------
with col_left:
    st.markdown('<div class="section-title">The Problem</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown(
            """
            <div class="card">
            Mixing certain chemicals can create toxic gases, strong heat, or even explosions.  
            Traditional lab manuals warn students, but they do not give **instant, real-time
            predictions** about dangerous reactions.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-title">AI-Powered Safety</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        Our tool acts like a **digital lab assistant**.  
        Students enter the names of two chemicals, and the system quickly estimates whether
        the combination is **safe** or **potentially hazardous** and shows a short explanation.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- MIDDLE: How it works & examples ----------
with col_mid:
    st.markdown('<div class="section-title">How the Software Works</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        <ul>
          <li><b>Chemical Database</b>: Stores basic hazard information.</li>
          <li><b>AI-Style Rules</b>: Encodes patterns of safe vs. unsafe mixes.</li>
          <li><b>User Interface</b>: Simple web app that runs on any device.</li>
          <li><b>Safety Engine</b>: Checks risk level and displays warnings instantly.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Example Scenarios</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        <ul>
          <li><b>Bleach + Ammonia</b> → risk of toxic chloramine gas (Dangerous)</li>
          <li><b>Vinegar + Baking Soda</b> → gentle CO₂ release (Safe)</li>
          <li><b>Water + Concentrated Sulfuric Acid</b> → intense heat (Hazard)</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- RIGHT: Interactive Demo ----------
with col_right:
    st.markdown('<div class="section-title">Try the Safety Checker</div>', unsafe_allow_html=True)
    st.markdown('<span class="pill">Demo</span>', unsafe_allow_html=True)
    st.write("")  # small spacing

    # Preset examples
    preset = st.selectbox(
        "Choose an example or type your own chemicals:",
        [
            "— type my own —",
            "Bleach + Ammonia",
            "Vinegar + Baking Soda",
            "Water + Concentrated Sulfuric Acid",
        ],
    )

    if preset == "Bleach + Ammonia":
        chem1_default, chem2_default = "Bleach", "Ammonia"
    elif preset == "Vinegar + Baking Soda":
        chem1_default, chem2_default = "Vinegar", "Baking Soda"
    elif preset == "Water + Concentrated Sulfuric Acid":
        chem1_default, chem2_default = "Water", "Concentrated Sulfuric Acid"
    else:
        chem1_default, chem2_default = "", ""

    chem1 = st.text_input("Chemical 1", value=chem1_default)
    chem2 = st.text_input("Chemical 2", value=chem2_default)

    st.write("")
    predict_clicked = st.button("Check safety")

    # --- simple rule-based "AI" ---
    def assess_mix(a, b):
        pair = {a.strip().lower(), b.strip().lower()}

        # Dangerous cases (high-level only, no lab instructions)
        if {"bleach", "ammonia"} <= pair:
            return "danger", (
                "This mix can create **toxic chloramine gases**. "
                "It should never be done in a normal lab setting."
            )
        if {"water", "concentrated sulfuric acid"} <= pair:
            return "danger", (
                "Adding water to concentrated sulfuric acid can release **intense heat** "
                "and cause splashes. This combination is considered hazardous."
            )

        # Clearly safe classroom-style reaction
        if {"vinegar", "baking soda"} <= pair:
            return "safe", (
                "This is a common classroom reaction. It releases **carbon dioxide gas** "
                "and is typically safe when done with normal lab precautions."
            )

        # Unknown / not in our mini-database
        if a == "" or b == "":
            return "none", "Enter two chemical names to check their combination."

        return "unknown", (
            "This combination is **not in our small demo database**. "
            "Treat it with care and always follow your teacher’s or lab manual’s instructions."
        )

    if predict_clicked:
        status, message = assess_mix(chem1, chem2)

        if status == "safe":
            st.markdown(
                f"""
                <div class="safe-box">
                  <span class="safe-label">Safety result: Likely safe</span><br>
                  {message}
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif status == "danger":
            st.markdown(
                f"""
                <div class="danger-box">
                  <span class="danger-label">Safety result: Potentially dangerous</span><br>
                  {message}
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif status == "unknown":
            st.markdown(
                f"""
                <div class="danger-box">
                  <span class="danger-label">Safety result: Unknown</span><br>
                  {message}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.info(message)

# ----------------- CONCLUSION -----------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; margin-top:0.3rem; font-size:0.95rem;">
      <span style="font-weight:800; color:#f25b9a;">Conclusion:</span>
      AI tools like this demo can support students, reduce accidents, and make chemistry
      experiments safer by checking combinations <b>before</b> they are mixed in the lab.
    </div>
    """,
    unsafe_allow_html=True,
)
