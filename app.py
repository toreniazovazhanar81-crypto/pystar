import streamlit as st

st.set_page_config(
    page_title="PyStar",
    page_icon="🌟",
    layout="centered"
)

st.markdown(
    """
    <div style="text-align:center;">
        <h1>🌟 P Y S T A R</h1>
        <h3>🐍 Python үйрен — жұлдыз бол!</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

name = st.text_input(
    "👤 Оқушының аты",
    placeholder="Атыңызды енгізіңіз"
)

grade = st.selectbox(
    "🎓 Сыныбыңызды таңдаңыз",
    ["7-сынып", "8-сынып", "9-сынып", "10-сынып"]
)

st.write("")

if st.button("🚀 ОЙЫНДЫ БАСТАУ", use_container_width=True):
    if name.strip():
        st.success(f"🌟 Қош келдіңіз, {name}!")
        st.write(f"🎓 Сыныбыңыз: {grade}")
        st.write("🚀 PyStar ойыны басталуға дайын!")
    else:
        st.warning("⚠️ Алдымен оқушының атын енгізіңіз.")
