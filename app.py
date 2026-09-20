import streamlit as st

# =========================================================
# ⭐ PY★STAR — AI ИНФОРМАТИКА ҰСТАЗЫ
# =========================================================

st.set_page_config(
    page_title="PY★STAR — AI Информатика Ұстазы",
    page_icon="⭐",
    layout="wide"
)

# =========================================================
# ОЙЫН ДЕРЕКТЕРІ
# =========================================================

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "grade" not in st.session_state:
    st.session_state.grade = "7-сынып"

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "starcoin" not in st.session_state:
    st.session_state.starcoin = 0

if "mission_274_done" not in st.session_state:
    st.session_state.mission_274_done = False

if "mission_275_done" not in st.session_state:
    st.session_state.mission_275_done = False

if "test_done" not in st.session_state:
    st.session_state.test_done = False

# =========================================================
# ДИЗАЙН
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #16213e, #243b55, #141e30);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.hero {
    text-align: center;
    padding: 55px 20px;
}

.logo {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: 4px;
}

.subtitle {
    font-size: 21px;
    margin-top: 10px;
    opacity: 0.85;
}

.welcome {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    margin-top: 25px;
}

.player-card {
    padding: 22px;
    border-radius: 20px;
    background: rgba(20, 28, 48, 0.9);
    border: 1px solid #3c4968;
    text-align: center;
    margin-bottom: 20px;
}

.stat {
    padding: 18px;
    border-radius: 16px;
    background: rgba(18, 25, 43, 0.95);
    border: 1px solid #394763;
    text-align: center;
}

.mission {
    padding: 28px;
    border-radius: 22px;
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid #52617f;
    margin-top: 20px;
}

.mentor {
    padding: 20px;
    border-radius: 18px;
    background: rgba(28, 37, 63, 0.95);
    border: 1px solid #5b6988;
}

.locked {
    padding: 20px;
    border-radius: 18px;
    background: rgba(30, 35, 48, 0.8);
    border: 1px solid #343b4d;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 1. КІРІСПЕ ЭКРАН
# =========================================================

if not st.session_state.game_started:

    st.markdown("""
    <div class="hero">

        <div class="logo">⭐ PY★STAR</div>

        <div class="subtitle">
        AI Информатика Ұстазы
        </div>

        <br>

        <div class="welcome">
        🚀 Қош келдің, болашақ CODE MASTER!
        </div>

        <p style="font-size:18px;">
        Білімді жина • Миссияларды орында • StarCoin тап • Деңгейіңді көтер!
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("### 👤 Ойыншы профилі")

        name = st.text_input(
            "Аты-жөнің",
            placeholder="Мысалы: Аян"
        )

        grade = st.selectbox(
            "Сыныбыңды таңда",
            ["7-сынып", "8-сынып", "9-сынып"]
        )

        st.write("")

        if st.button(
            "🎮 ОЙЫНДЫ БАСТАУ",
            use_container_width=True
        ):

            if name.strip() == "":
                st.warning("⚠️ Алдымен аты-жөніңді енгіз!")

            else:

                st.session_state.student_name = name
                st.session_state.grade = grade
                st.session_state.game_started = True

                st.rerun()

    st.divider()

    st.markdown(
        """
        <div style="text-align:center; opacity:0.7;">
        🎯 7–9 сынып • 💻 Информатика • 🤖 AI Mentor • ⭐ StarCoin
        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()

# =========================================================
# 2. НЕГІЗГІ ОЙЫН ЭКРАНЫ
# =========================================================

name = st.session_state.student_name
grade = st.session_state.grade

st.markdown(
    f"""
    <div class="player-card">

        <div style="font-size:32px;">
        ⭐ PY★STAR
        </div>

        <div style="font-size:22px;">
        Қош келдің, <b>{name}</b>!
        </div>

        <div style="opacity:0.8;">
        🎓 {grade} • 🚀 Ойын басталды!
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 3. СТАТИСТИКА
# =========================================================

level = "STARTER"

if st.session_state.xp >= 300:
    level = "GAME DEVELOPER"
elif st.session_state.xp >= 100:
    level = "CODER"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="stat">
        <h3>⭐ StarCoin</h3>
        <h2>{st.session_state.starcoin}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="stat">
        <h3>⚡ XP</h3>
        <h2>{st.session_state.xp}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="stat">
        <h3>🏆 Деңгей</h3>
        <h2>{level}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    completed = 0

    if st.session_state.mission_274_done:
        completed += 1

    if st.session_state.mission_275_done:
        completed += 1

    st.markdown(
        f"""
        <div class="stat">
        <h3>🎯 Миссия</h3>
        <h2>{completed}/2</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# =========================================================
# 4. ОЙЫН ӘЛЕМІ
# =========================================================

st.markdown("## 🗺️ ОЙЫН ӘЛЕМІ")

world1, world2, world3 = st.columns(3)

with world1:
    st.markdown("""
    <div class="mission">
    <h2>🌐 01 — DIGITAL WORLD</h2>
    <p>Информатика әлеміне алғашқы қадам.</p>
    <b>Миссиялар: 274+</b>
    </div>
    """, unsafe_allow_html=True)

with world2:
    st.markdown("""
    <div class="mission">
    <h2>🐍 02 — PYTHON WORLD</h2>
    <p>Алгоритмдер мен бағдарламалау.</p>
    <b>Жақында ашылады</b>
    </div>
    """, unsafe_allow_html=True)

with world3:
    st.markdown("""
    <div class="locked">
    <h2>🤖 03 — AI WORLD</h2>
    <p>Жасанды интеллект әлемі.</p>
    🔒 Құлыптаулы
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 5. МИССИЯ 274
# =========================================================

st.markdown("## 🎯 МИССИЯ 274")

st.markdown(
    """
    <div class="mission">

    <h2>🔐 ҚАУІПСІЗДІК КІЛТІ</h2>

    <p style="font-size:18px;">
    Сен Digital World әлеміндегі алғашқы қауіпсіздік қақпасына келдің.
    </p>

    <p>
    Мақсат: жеке ақпаратты қорғау және қауіпсіз пароль құру
    қағидаларын түсіну.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

q1 = st.radio(
    "❓ 1. Қай пароль қауіпсіздеу?",
    [
        "123456",
        "qwerty",
        "Ayan2000",
        "Kz!7mQ#92Lp"
    ],
    key="q1"
)

q2 = st.radio(
    "❓ 2. Парольді кімге берген дұрыс?",
    [
        "Досыма",
        "Бейтаныс адамға",
        "Ешкімге бермеу керек",
        "Әлеуметтік желіге жазу керек"
    ],
    key="q2"
)

q3 = st.radio(
    "❓ 3. Күмәнді сілтеме келсе не істейсің?",
    [
        "Бірден басамын",
        "Досыма жіберемін",
        "Ашпай, тексеремін немесе өшіремін",
        "Барлық жеке мәліметімді енгіземін"
    ],
    key="q3"
)

if not st.session_state.mission_274_done:

    if st.button(
        "⚔️ МИССИЯНЫ ТЕКСЕРУ",
        use_container_width=True
    ):

        correct = 0

        if q1 == "Kz!7mQ#92Lp":
            correct += 1

        if q2 == "Ешкімге бермеу керек":
            correct += 1

        if q3 == "Ашпай, тексеремін немесе өшіремін":
            correct += 1

        if correct == 3:

            st.session_state.mission_274_done = True
            st.session_state.xp += 50
            st.session_state.starcoin += 20

            st.success("🎉 МИССИЯ 274 ОРЫНДАЛДЫ!")
            st.balloons()

            st.info(
                "⭐ +20 StarCoin   |   ⚡ +50 XP"
            )

            st.rerun()

        else:

            st.warning(
                f"⚠️ {correct}/3 дұрыс. "
                "AI Mentor көмегін пайдаланып, қайта ойланып көр!"
            )

else:

    st.success("✅ МИССИЯ 274 ОРЫНДАЛДЫ")
    st.info("⭐ +20 StarCoin • ⚡ +50 XP")

# =========================================================
# 6. AI MENTOR
# =========================================================

st.markdown("## 🤖 AI MENTOR")

st.markdown(
    """
    <div class="mentor">

    <h3>🧠 Мен саған бірден жауап бермеймін.</h3>

    <p>
    Менің міндетім — дұрыс жауапты өзің табуыңа көмектесу.
    </p>

    <p>
    💡 Кеңес: қауіпсіз парольде әртүрлі таңбалар,
    бас және кіші әріптер, сандар қолданылғаны жақсы.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 7. ӨЗІҢ ШЫҒАР
# =========================================================

st.markdown("## ✍️ ӨЗІҢ ШЫҒАР")

student_answer = st.text_area(
    "💭 Қауіпсіз пароль қандай болуы керек?",
    placeholder="Өз ойыңды жаз..."
)

if st.button("🤖 AI ТЕКСЕРУ", use_container_width=True):

    if student_answer.strip() == "":

        st.warning("Алдымен өз жауабыңды жаз.")

    else:

        answer = student_answer.lower()

        keywords = [
            "ұзын",
            "әріп",
            "сан",
            "таңба",
            "символ",
            "күрделі"
        ]

        found = sum(word in answer for word in keywords)

        if found >= 2:

            st.success(
                "🌟 Жақсы! Сен негізгі қауіпсіздік қағидаларын түсіндің."
            )

            st.info(
                "AI Mentor: Жауабыңда бірнеше маңызды белгі бар."
            )

        else:

            st.warning(
                "💡 AI Mentor: Парольдің ұзындығы, әріптер, "
                "сандар және арнайы таңбалар туралы ойланып көр."
            )

# =========================================================
# 8. MINI TEST
# =========================================================

st.markdown("## 📝 MINI TEST")

test_answer = st.radio(
    "Компьютердегі жеке мәліметті қорғаудың бір жолы:",
    [
        "Пароль қолдану",
        "Парольді барлығына айту",
        "Күмәнді файлдарды ашу",
        "Жеке мәліметті жариялау"
    ],
    key="mini_test"
)

if not st.session_state.test_done:

    if st.button(
        "📝 ТЕСТІ АЯҚТАУ",
        use_container_width=True
    ):

        if test_answer == "Пароль қолдану":

            st.session_state.test_done = True
            st.session_state.xp += 30
            st.session_state.starcoin += 10

            st.success("🎉 Дұрыс жауап!")
            st.info("⚡ +30 XP • ⭐ +10 StarCoin")

            st.rerun()

        else:

            st.warning(
                "AI Mentor: Жеке мәліметті қорғау туралы қайта ойланып көр."
            )

else:

    st.success("✅ MINI TEST ОРЫНДАЛДЫ")

# =========================================================
# 9. МИССИЯ 275
# =========================================================

st.markdown("## 🚀 КЕЛЕСІ МИССИЯ")

if st.session_state.mission_274_done:

    st.markdown(
        """
        <div class="mission">

        <h2>🔓 МИССИЯ 275 — АҚПАРАТ ӨЛШЕМІ</h2>

        <p>
        Келесі қақпа ашылды!
        Ақпараттың өлшем бірліктерін зерттеуге дайынсың ба?
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    answer275 = st.radio(
        "❓ 1 байтта қанша бит бар?",
        [
            "2 бит",
            "4 бит",
            "8 бит",
            "16 бит"
        ],
        key="q275"
    )

    if not st.session_state.mission_275_done:

        if st.button(
            "🚀 275-Миссияны орындау",
            use_container_width=True
        ):

            if answer275 == "8 бит":

                st.session_state.mission_275_done = True
                st.session_state.xp += 50
                st.session_state.starcoin += 20

                st.success("🏆 МИССИЯ 275 ОРЫНДАЛДЫ!")
                st.balloons()

                st.info("⭐ +20 StarCoin • ⚡ +50 XP")

                st.rerun()

            else:

                st.warning(
                    "💡 AI Mentor: 1 байт = бірнеше биттен тұратын "
                    "ақпарат өлшемі. Қайта ойланып көр."
                )

    else:

        st.success("🏆 МИССИЯ 275 ОРЫНДАЛДЫ!")

else:

    st.markdown(
        """
        <div class="locked">

        🔒 Миссия 275 құлыптаулы

        <p>
        Алдымен 274-миссияны орында.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 10. ЖЕТІСТІК
# =========================================================

if (
    st.session_state.mission_274_done
    and st.session_state.mission_275_done
):

    st.divider()

    st.markdown("## 🏆 ЖЕТІСТІК!")

    st.success(
        f"🎉 {name}, сен алғашқы екі миссияны орындадың!"
    )

    st.markdown(
        """
        ### ⭐ Сенің нәтижелерің

        - 🔐 Қауіпсіздік
        - 💾 Ақпарат өлшемі
        - 🤖 AI Mentor
        - ⭐ StarCoin жинау
        - ⚡ XP жинау

        **Келесі әлемдер кейін ашылады...**
        """,
    )

# =========================================================
# 11. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; opacity:0.65; padding:20px;">

    ⭐ <b>PY★STAR</b> — AI Информатика Ұстазы

    <br>

    Білім → Миссия → AI Mentor → Тәжірибе → Жетістік

    <br><br>

    🚀 Python үйрен. Код жаз. Жұлдыз бол!

    </div>
    """,
    unsafe_allow_html=True
)
