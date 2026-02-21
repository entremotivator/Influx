import streamlit as st
from datetime import datetime, timedelta
import time

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="AI Agents & Automations Control Center",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

if "login_time" not in st.session_state:
    st.session_state.login_time = None

if "activity_log" not in st.session_state:
    st.session_state.activity_log = []

# -----------------------------------
# AUTH FUNCTION
# -----------------------------------
def authenticate(username, password):
    users = st.secrets["users"]
    if username in users and users[username]["password"] == password:
        return True, users[username]["role"]
    return False, None

# -----------------------------------
# SESSION TIMEOUT (30 MINUTES)
# -----------------------------------
def check_timeout():
    if st.session_state.login_time:
        if datetime.now() - st.session_state.login_time > timedelta(minutes=30):
            st.session_state.authenticated = False
            st.warning("Session expired. Please login again.")
            time.sleep(1)
            st.rerun()

# -----------------------------------
# LOGIN PAGE
# -----------------------------------
if not st.session_state.authenticated:

    st.title("🔐 Secure AI Agents & Automations Portal")
    st.subheader("Private Access Only")

    st.markdown("""
    Access your private AI infrastructure:
    
    - 🤖 Intelligent AI Agents  
    - ⚙️ Advanced Business Automations  
    - 📊 Growth & Analytics Systems  
    - 🧠 Custom AI Workflows  
    - 🚀 Internal Deployment Tools  
    """)

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Username")

    with col2:
        password = st.text_input("Password", type="password")

    if st.button("Login Securely"):
        valid, role = authenticate(username, password)
        if valid:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = role
            st.session_state.login_time = datetime.now()
            st.session_state.activity_log.append(
                f"{datetime.now().strftime('%H:%M:%S')} - {username} logged in"
            )
            st.success("Access Granted")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid credentials")

# -----------------------------------
# DASHBOARD
# -----------------------------------
else:

    check_timeout()

    st.title("🚀 AI Control Center Dashboard")

    st.markdown(f"""
    **User:** {st.session_state.username}  
    **Role:** {st.session_state.role.upper()}  
    **Session Started:** {st.session_state.login_time.strftime('%B %d, %Y at %I:%M %p')}
    """)

    st.divider()

    # -----------------------------------
    # METRICS
    # -----------------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Active AI Agents", 7)
    col2.metric("Running Automations", 5)
    col3.metric("System Status", "Operational")

    st.divider()

    # -----------------------------------
    # AI AGENTS SECTION
    # -----------------------------------
    st.header("🤖 AI Agents")

    agents = {
        "AI Landing Page Generator": "Generate high-converting landing pages instantly.",
        "Credit Dispute Letter AI": "Create structured dispute letters automatically.",
        "Grant Finder Automation": "Discover grant opportunities using AI research.",
        "Ollama Local AI Assistant": "Fully local AI workflow system.",
        "Business Plan Builder": "Create investor-ready business plans.",
        "Content Repurposing Engine": "Transform long-form content into multi-platform posts.",
        "Sales Funnel Architect": "Design automated funnel sequences."
    }

    for name, description in agents.items():
        with st.expander(name):
            st.write(description)
            if st.button(f"Launch {name}"):
                st.session_state.activity_log.append(
                    f"{datetime.now().strftime('%H:%M:%S')} - Launched {name}"
                )
                st.success(f"{name} launching soon...")

    st.divider()

    # -----------------------------------
    # AUTOMATIONS SECTION
    # -----------------------------------
    st.header("⚙️ Business Automations")

    automations = [
        "Lead Capture → CRM Sync",
        "Email Follow-Up Sequences",
        "AI Grant Research Workflow",
        "Client Onboarding Pipeline",
        "Podcast Publishing Automation",
        "Content Distribution Engine"
    ]

    for auto in automations:
        col1, col2 = st.columns([3,1])
        col1.write(f"🔄 {auto}")
        if col2.button("Activate", key=auto):
            st.session_state.activity_log.append(
                f"{datetime.now().strftime('%H:%M:%S')} - Activated {auto}"
            )
            st.success(f"{auto} Activated")

    st.divider()

    # -----------------------------------
    # ADMIN SECTION
    # -----------------------------------
    if st.session_state.role == "admin":

        st.header("🛡 Admin Controls")

        st.write("Manage internal system configurations.")

        if st.button("Clear Activity Log"):
            st.session_state.activity_log = []
            st.success("Activity log cleared.")

        st.write("### System Logs")
        for log in st.session_state.activity_log:
            st.write(log)

    st.divider()

    # -----------------------------------
    # LOGOUT
    # -----------------------------------
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.login_time = None
        st.rerun()

    st.caption("AI Agents & Automations Enterprise Portal")
