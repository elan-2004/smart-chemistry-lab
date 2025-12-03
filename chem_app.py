# chem_app.py
import streamlit as st

# ------------------------------
# 1) CONFIG & PAGE STYLE
# ------------------------------
st.set_page_config(
    page_title="Smart Chemistry Lab",
    page_icon="🧪",
    layout="wide",
)

# Custom CSS to match your cute poster vibe
st.markdown(
    """
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
    }

    .main {
        background: radial-gradient(circle at top left, #f7f0ff 0, #fff8f3 45%, #ffffff 100%);
    }

    h1, h2, h3 {
        color: #3f2b96;
        font-weight: 800;
    }

    .section-title {
        letter-spacing: 0.18em;
        font-size: 0.9rem;
        text-transform: uppercase;
        color: #7b4fff;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 0.25rem;
    }

    .info-card {
        border-radius: 18px;
        padding: 1.1rem 1.3rem;
        background: rgba(255, 255, 255, 0.8);
        box-shadow: 0 12px 35px rgba(63, 43, 150, 0.08);
        border: 1px solid rgba(128, 90, 213, 0.10);
    }

    .pill-badge {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        font-size: 0.75rem;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.15em;
        background: linear-gradient(90deg, #7b4fff, #ff73b3);
        color: white;
        margin-bottom: 0.6rem;
    }

    .predict-btn > button {
        background: linear-gradient(90deg, #7b4fff, #ff73b3);
        border-radius: 999px !important;
        border: none;
        color: white !important;
        font-weight: 600;
        padding: 0.5rem 2.3rem;
        font-size: 1rem;
    }

    .predict-btn > button:hover {
        filter: brightness(1.03);
        box-shadow: 0 10px 25px rgba(123, 79, 255, 0.4);
    }

    .safe-box {
        background: #e6ffed;
        border-radius: 18px;
        padding: 1.1rem 1.3rem;
        border: 1px solid #22c55e55;
    }

    .danger-box {
        background: #fee2e2;
        border-radius: 18px;
        padding: 1.1rem 1.3rem;
        border: 1px solid #ef444455;
    }

    .neutral-box {
        background: #eff6ff;
        border-radius: 18px;
        padding: 1.1rem 1.3rem;
        border: 1px solid #3b82f655;
    }

    .chem-pill {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
        border-radius: 999px;
        background: rgba(123, 79, 255, 0.08);
        font-size: 0.8rem;
        color: #4b0082;
        border: 1px solid rgba(123, 79, 255, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# 2) KNOWLEDGE BASE
# ------------------------------


def norm(name: str) -> str:
    return name.strip().lower()


# Basic info about some chemicals
CHEM_INFO = {
    "bleach": {
        "display": "Bleach (Sodium Hypochlorite)",
        "type": "Strong oxidizer, basic solution",
        "hazard": "Corrosive, can release chlorine-based gases with acids or ammonia.",
    },
    "ammonia": {
        "display": "Ammonia (NH₃, household cleaner)",
        "type": "Weak base, volatile",
        "hazard": "Irritating gas, forms toxic chloramine gas with bleach.",
    },
    "vinegar": {
        "display": "Vinegar (Acetic acid ~5%)",
        "type": "Weak acid",
        "hazard": "Mild irritant, generally safe in small lab amounts.",
    },
    "baking soda": {
        "display": "Baking Soda (Sodium Bicarbonate)",
        "type": "Weak base",
        "hazard": "Very low hazard, common in safe demonstrations.",
    },
    "water": {
        "display": "Water (H₂O)",
        "type": "Solvent",
        "hazard": "Usually safe, but mixing with strong acids can release heat.",
    },
    "concentrated sulfuric acid": {
        "display": "Concentrated Sulfuric Acid (H₂SO₄)",
        "type": "Strong acid, very exothermic with water",
        "hazard": "Highly corrosive, causes severe burns, reacts vigorously with water and organics.",
    },
}


# Specific combination rules (you can add more later)
COMBO_RULES = {
    tuple(sorted([norm("Bleach"), norm("Ammonia")])): {
        "status": "danger",
        "title": "🚨 Dangerous Combination",
        "description": "Bleach and ammonia react to form toxic **chloramine gas** and related compounds.",
        "details": [
            "Can cause serious breathing problems.",
            "Should never be mixed in a lab or at home.",
        ],
        "risk": 10,
        "hazard_type": "Toxic gas release",
    },
    tuple(sorted([norm("Vinegar"), norm("Baking Soda")])): {
        "status": "safe",
        "title": "✅ Safe Demonstration",
        "description": "Vinegar (acid) and baking soda (base) react to form **carbon dioxide gas, water, and a salt**.",
        "details": [
            "Common school experiment.",
            "Still use safety goggles and a tray for spills.",
        ],
        "risk": 2,
        "hazard_type": "Mild foaming reaction",
    },
    tuple(sorted([norm("Water"), norm("Concentrated Sulfuric Acid")])): {
        "status": "danger",
        "title": "🔥 Exothermic & Hazardous",
        "description": "Mixing water and concentrated sulfuric acid releases **a lot of heat**.",
        "details": [
            "Can cause splattering and severe burns.",
            "In real labs, we always **add acid to water**, never water to acid.",
        ],
        "risk": 9,
        "hazard_type": "Extreme heat (exothermic)",
    },
}


def analyze_mixture(chem1_raw: str, chem2_raw: str):
    """Return analysis dict based on two chemical names."""
    c1 = norm(chem1_raw)
    c2 = norm(chem2_raw)

    if not c1 or not c2:
        return None

    key = tuple(sorted([c1, c2]))

    # Exact rule known?
    if key in COMBO_RULES:
        combo = COMBO_RULES[key]
        return {
            "known": True,
            "status": combo["status"],
            "title": combo["title"],
            "description": combo["description"],
            "details": combo["details"],
            "risk": combo["risk"],
            "hazard_type": combo["hazard_type"],
        }

    # No exact rule -> generic advice
    info1 = CHEM_INFO.get(c1)
    info2 = CHEM_INFO.get(c2)

    # Generic high caution if strong acid is involved
    if c1 == "concentrated sulfuric acid" or c2 == "concentrated sulfuric acid":
        return {
            "known": False,
            "status": "warning",
            "title": "⚠️ Use Extreme Caution",
            "description": "Concentrated sulfuric acid is very dangerous. Mixing it with other chemicals can release heat or toxic fumes.",
            "details": [
                "Only mix under teacher supervision in a proper lab.",
                "Always use goggles, gloves, and lab coat.",
            ],
            "risk": 8,
            "hazard_type": "Corrosive / exothermic",
        }

    # Otherwise neutral / unknown
    return {
        "known": False,
        "status": "neutral",
        "title": "ℹ️ Unknown Combination",
        "description": "This exact mixture is not in the app's safety list.",
        "details": [
            "Always check your lab manual or safety data sheets (SDS).",
            "Ask your teacher or supervisor before mixing.",
        ],
        "risk": 5,
        "hazard_type": "Not classified by this app",
    }


# ------------------------------
# 3) PAGE LAYOUT
# ------------------------------

# Title section
st.markdown('<span class="pill-badge">Science Fair Project</span>', unsafe_allow_html=True)
st.title("Smart Chemistry Lab – Safety Checker")

st.write(
    "This app acts like a **digital lab assistant**. Type two chemicals and it "
    "will estimate whether the mixture is likely to be **safe**, **risky**, or **dangerous**, "
    "based on example scenarios and safety rules."
)

st.write("Instructor: **Dr. Najma Saleem**  •  Course: **Science Fair – Chemistry**")

st.markdown("---")

# 3 columns: info, examples, demo
col1, col2, col3 = st.columns([1.1, 1.1, 1.2])

# --- Column 1: Overview ---
with col1:
    st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.subheader("What this AI-style assistant does")

    st.markdown(
        """
        - Checks **example reactions** from a small safety database.  
        - Highlights **dangerous combinations** (toxic gas, heat, etc.).  
        - Gives a **risk level from 1–10** (1 = very low, 10 = very high).  
        - Reminds students to always follow real lab safety rules.
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Column 2: Inputs / Examples ---
with col2:
    st.markdown('<div class="section-title">Example scenarios</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.subheader("Try these combinations")

    st.markdown(
        """
        - **Bleach + Ammonia** → Toxic chloramine gas (**Dangerous**)  
        - **Vinegar + Baking Soda** → CO₂ gas and water (**Safe demo**)  
        - **Water + Concentrated Sulfuric Acid** → Very hot mixture (**Hazard**)  
        """
    )

    st.markdown("You can also type your own names and see how the app responds.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Column 3: Demo ---
with col3:
    st.markdown('<div class="section-title">Try the checker</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.subheader("Check a mixture")

    # Quick chips to tap
    st.caption("Click a chip to autofill:")
    chip_cols = st.columns(3)
    with chip_cols[0]:
        if st.button("Bleach + Ammonia"):
            chem1_default, chem2_default = "Bleach", "Ammonia"
        else:
            chem1_default, chem2_default = "", ""
    with chip_cols[1]:
        if st.button("Vinegar + Baking Soda"):
            chem1_default, chem2_default = "Vinegar", "Baking Soda"
    with chip_cols[2]:
        if st.button("Water + Conc. H₂SO₄"):
            chem1_default, chem2_default = "Water", "Concentrated Sulfuric Acid"

    # To avoid weird behaviour, use session_state to store last chip click
    if "chem1" not in st.session_state:
        st.session_state["chem1"] = ""
    if "chem2" not in st.session_state:
        st.session_state["chem2"] = ""

    # If any default set by a button, update session state
    if chem1_default:
        st.session_state["chem1"] = chem1_default
        st.session_state["chem2"] = chem2_default

    chem1 = st.text_input("Chemical 1", value=st.session_state["chem1"])
    chem2 = st.text_input("Chemical 2", value=st.session_state["chem2"])

    st.write("")  # small space

    predict_clicked = st.container()
    with predict_clicked:
        st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
        run = st.button("Check safety")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# 4) SHOW RESULT
# ------------------------------
st.markdown("")

if "chem1" not in st.session_state:
    st.session_state["chem1"] = ""
if "chem2" not in st.session_state:
    st.session_state["chem2"] = ""

# When button pressed
if run:
    result = analyze_mixture(chem1, chem2)

    if not result:
        st.warning("Please enter both chemical names.")
    else:
        status = result["status"]

        # Choose box style
        if status == "safe":
            box_class = "safe-box"
        elif status == "danger":
            box_class = "danger-box"
        elif status == "warning":
            box_class = "danger-box"
        else:
            box_class = "neutral-box"

        st.markdown(f'<div class="{box_class}">', unsafe_allow_html=True)

        # Title line (green or red depending on box)
        st.markdown(f"### {result['title']}")
        st.write(result["description"])

        # Risk + hazard type
        st.write(
            f"**Risk level:** {result['risk']}/10  •  **Hazard type:** {result['hazard_type']}"
        )

        if result["details"]:
            st.markdown("**Notes:**")
            for d in result["details"]:
                st.markdown(f"- {d}")

        st.markdown("</div>", unsafe_allow_html=True)

        # Extra info about individual chemicals (if we have it)
        c1_norm = norm(chem1)
        c2_norm = norm(chem2)
        info1 = CHEM_INFO.get(c1_norm)
        info2 = CHEM_INFO.get(c2_norm)

        if info1 or info2:
            st.markdown("#### Chemical details")
            chem_cols = st.columns(2)
            if info1:
                with chem_cols[0]:
                    st.markdown('<div class="info-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"**{info1['display']}**  \n"
                        f"*Type:* {info1['type']}  \n"
                        f"*Hazard:* {info1['hazard']}"
                    )
                    st.markdown("</div>", unsafe_allow_html=True)
            if info2:
                with chem_cols[1]:
                    st.markdown('<div class="info-card">', unsafe_allow_html=True)
                    st.markdown(
                        f"**{info2['display']}**  \n"
                        f"*Type:* {info2['type']}  \n"
                        f"*Hazard:* {info2['hazard']}"
                    )
                    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("👆 Type two chemical names above and click **Check safety** to see the result.")
