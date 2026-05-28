import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HR/Admin Management System",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>
    .stApp {
        background-color: white;
    }

    /* HEADER */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #000000;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 35px;
    }

    /* CARD DESIGN */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 18px;
        border-left: 6px solid #ff6b00;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 15px;
        border: 1px solid #f3f4f6;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
    }

    .card h3 {
        color: #000000;
        margin-bottom: 10px;
    }

    .card p {
        color: #4b5563;
        line-height: 1.6;
        font-size: 15px;
    }

    /* BUTTONS */
    div.stLinkButton > a {
        background: #ff6b00 !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 12px 18px !important;
        font-weight: bold !important;
        text-align: center !important;
        width: 100% !important;
        display: block !important;
        text-decoration: none !important;
        margin-bottom: 30px !important;
    }

    /* REMOVE EXTRA TOP SPACE */
    .block-container {
        padding-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO & HEADER
# =========================================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo.png", width=400)

st.markdown('<div class="main-title">HR/ADMIN MANAGEMENT SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart HR Operations & Employee Analytics Platform</div>', unsafe_allow_html=True)

# =========================================
# SECURE LOGIN SYSTEM (USERNAME & PASSWORD)
# =========================================
if not st.session_state.authenticated:
    login_col1, login_col2, login_col3 = st.columns([1, 1.5, 1])
    
    with login_col2:
        st.subheader("🔑 System Login")
        
        # Text fields for explicit input
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")  # Fixed function here
        
        if st.button("Login", use_container_width=True):

        
        # Text fields for explicit input
    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")
        
        
        if st.button("Login", use_container_width=True):
            # Normalize user input to find matches in secrets.toml keys
            # (e.g., "Managing Director" or "md" -> "managing_director")
            formatted_user = username_input.strip().lower().replace(" ", "_")
            
            # Map simplified inputs to display roles cleanly
            role_mapping = {
                "managing_director": "Managing Director",
                "md": "Managing Director",
                "hr_admin": "HR/Admin",
                "hr": "HR/Admin",
                "admin": "HR/Admin",
                "ciso": "CISO",
                "general_user": "General User",
                "general": "General User"
            }
            
            # Determine mapped key format
            matched_key = None
            for shortcut, full_role in role_mapping.items():
                if formatted_user == shortcut:
                    matched_key = shortcut if "_" in shortcut or shortcut in ["ciso", "admin", "hr", "md"] else None
                    # Normalize back to the target secret keys in secrets.toml
                    if shortcut == "md": matched_key = "managing_director"
                    if shortcut in ["hr", "admin"]: matched_key = "hr_admin"
                    if shortcut == "general": matched_key = "general_user"
                    break
            
            # If no shortcut match found, use the direct raw formatted input
            if not matched_key:
                matched_key = formatted_user

            # Check if key exists in secrets framework and match values securely
            if matched_key in st.secrets and password_input == st.secrets[matched_key]:
                st.session_state.authenticated = True
                st.session_state.user_role = role_mapping.get(matched_key, username_input)
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")
    st.stop()

# Logout Option in Main View
out_col1, out_col2 = st.columns([5, 1])
with out_col2:
    if st.button("Log Out", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.user_role = None
        st.rerun()

st.info(f"Logged in as: **{st.session_state.user_role}**")
st.markdown("---")

# =========================================
# APP LINKS & HUB PLATFORM
# =========================================
links = {
    "Attendance": "https://staff-attendance.streamlit.app/",
    "Business Department Appraisal": "https://business-department.streamlit.app/",
    "Staff Performance Appraisal": "https://staff-performance.streamlit.app/",
    "Admin Panel": "https://management-panel.streamlit.app/"
}

# Grid Layout Display
left_col, right_col = st.columns(2)

with left_col:
    # Section 1: Attendance
    st.markdown("""
    <div class="card">
        <h3>📅 Attendance Management</h3>
        <p>Track employee attendance records, punctuality, daily check-ins, and workforce presence.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Attendance System", links["Attendance"])

    # Section 2: Staff Performance
    st.markdown("""
    <div class="card">
        <h3>📝 Staff Performance Appraisal</h3>
        <p>Analyze employee productivity, conduct staff appraisals, reviews, and assessment processes efficiently.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Staff Performance Appraisal", links["Staff Performance Appraisal"])

with right_col:
    # Section 3: Business Department
    st.markdown("""
    <div class="card">
        <h3>💼 Business Department Appraisal</h3>
        <p>Tracks business department productivity, targets, efficiency, and overall departmental performance.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Business Department Appraisal", links["Business Department Appraisal"])

    # Section 4: Admin Panel
    st.markdown("""
    <div class="card">
        <h3>🛠️ Admin Panel</h3>
        <p>Manage high-level administrative tasks, operational setups, and office activities.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Admin Panel", links["Admin Panel"])
