import streamlit as st
from datetime import date, timedelta
import pandas as pd
import random

# ----------------------------
# Participant Profiles
# ----------------------------
participants = {
    "Influx": "Tech enthusiast and podcast visionary",
    "Jasmine": "Marketing strategist and critical thinker",
    "CEEZ": "Content creator and SEO expert",
    "Richard": "Top business advisor and entrepreneur",
    "EntreMotivator": "Inspiring motivator and artist",
    "One_Love": "Culture and community advocate",
    "3partner": "Real estate and investment expert",
    "Radio": "Music and entertainment specialist",
    "Pierre": "Digital marketer and website designer",
    "RENEE": "Experienced educator and public speaker",
    "Mr.Chris": "Nature enthusiast and podcast storyteller",
    "Michelle": "Creative thinker and pet lover"
}

# ----------------------------
# Helper Functions
# ----------------------------
def create_blank_schedule():
    """Create a blank weekly schedule with days as keys."""
    return {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

def get_motivational_quote():
    quotes = [
        "“Success usually comes to those who are too busy to be looking for it.” – Henry David Thoreau",
        "“Don’t be afraid to give up the good to go for the great.” – John D. Rockefeller",
        "“Opportunities don’t happen. You create them.” – Chris Grosser",
        "“Work hard in silence, let your success be the noise.” – Frank Ocean",
        "“Great things never come from comfort zones.” – Unknown",
        "“Push yourself, because no one else is going to do it for you.” – Unknown"
    ]
    return random.choice(quotes)

# ----------------------------
# App Layout
# ----------------------------
st.title("🎙️ Influx Podcast & Teaching Plan")
st.subheader("A Collaborative Hub for Podcasts, Teaching & Growth")

st.markdown("""
Welcome to the **Influx Podcast Plan**, a space where **creators, motivators, educators, and entrepreneurs**  
come together to share knowledge, inspire others, and build powerful conversations.  

This hub will help us:  
- 🗓 **Organize weekly podcast episodes** with rotating hosts  
- 📖 **Schedule teaching sessions and workshops**  
- 🤝 **Collaborate across fields** like tech, marketing, business, culture, and community  
- 🚀 **Plan months ahead** so every voice has its spotlight  
""")

# ----------------------------
# Daily Motivation
# ----------------------------
st.header("🌟 Motivation of the Day")
st.info(get_motivational_quote())

# ----------------------------
# Date & Calendar Setup
# ----------------------------
today = date.today()
start_of_week = today - timedelta(days=today.weekday())
end_of_week = start_of_week + timedelta(days=6)

st.header("📅 Current Week Schedule")
st.write(f"**Week: {start_of_week.strftime('%B %d, %Y')} - {end_of_week.strftime('%B %d, %Y')}**")

schedule = create_blank_schedule()

# Assign participants to podcast slots
for i, (name, description) in enumerate(participants.items()):
    day = list(schedule.keys())[i % 7]
    schedule[day].append(f"🎧 Podcast: Hosted by {name} – {description}")

# Teaching session (default midweek)
schedule["Wednesday"].append("📖 Teaching Session: Hosted by RENEE")
# Add a weekend collaboration
schedule["Saturday"].append("🤝 Collaboration Roundtable: Multi-host special")

# ----------------------------
# Display Current Schedule
# ----------------------------
for day, events in schedule.items():
    st.subheader(day)
    if events:
        for event in events:
            st.write(event)
    else:
        st.write("_No events scheduled yet._")

# ----------------------------
# Add / Modify Events
# ----------------------------
st.header("🛠 Manage & Customize Events")
event_name = st.text_input("Event Name", "")
event_day = st.selectbox("Select Day", list(schedule.keys()))
event_host = st.selectbox("Select Host", list(participants.keys()))
event_type = st.selectbox("Event Type", ["Podcast", "Teaching", "Workshop", "Live Q&A", "Special Project"])
is_recurring = st.checkbox("Repeat weekly?")

if st.button("➕ Add Event"):
    if event_name and event_day and event_host:
        new_event = f"{event_type}: {event_name} – Hosted by {event_host}"
        schedule[event_day].append(new_event)
        st.success(f"✅ Added: {new_event} on {event_day}")
        if is_recurring:
            st.info(f"🔁 This will repeat weekly on {event_day}.")
    else:
        st.error("⚠️ Please complete all fields to add an event.")

# ----------------------------
# Future Planning
# ----------------------------
st.header("📌 Plan for Future Weeks & Months")
weeks_ahead = st.number_input("Plan how many weeks ahead?", min_value=1, max_value=52, value=4)
for i in range(1, weeks_ahead+1):
    future_start = start_of_week + timedelta(weeks=i)
    future_end = future_start + timedelta(days=6)
    st.markdown(f"**Week {i}: {future_start.strftime('%B %d')} – {future_end.strftime('%B %d, %Y')}**")

future_event_name = st.text_input("Future Event Name", "")
future_event_day = st.selectbox("Future Event Day", list(schedule.keys()))
future_event_host = st.selectbox("Future Event Host", list(participants.keys()))

if st.button("➕ Add Future Event"):
    if future_event_name and future_event_day and future_event_host:
        st.success(f"📌 Future Event: '{future_event_name}' on {future_event_day}, hosted by {future_event_host}")
    else:
        st.error("⚠️ Please fill out all fields for future event.")

# ----------------------------
# Export Schedule
# ----------------------------
st.header("📤 Export Weekly Schedule")
if st.button("⬇️ Export Current Week"):
    df = pd.DataFrame([
        {"Day": day, "Events": ", ".join(events)} 
        for day, events in schedule.items()
    ])
    csv = df.to_csv(index=False)
    st.download_button("Download as CSV", data=csv, file_name="weekly_schedule.csv", mime="text/csv")
    st.success("✅ Schedule exported successfully!")

# ----------------------------
# Participant Profiles
# ----------------------------
st.header("👥 Meet the Hosts")
st.markdown("Our hosts bring a **unique mix of talents** from across industries. Explore their profiles below:")

for name, description in participants.items():
    st.markdown(f"""
    <div style="padding:10px; border:1px solid #ddd; border-radius:8px; margin-bottom:10px;">
        <strong>{name}</strong><br>
        <em>{description}</em>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Quick Links
# ----------------------------
st.header("🔗 Quick Links & Resources")
st.markdown("""
- 🌐 [EntreMotivator Cards](http://entremotivator.com/landing/more)  
- 🎧 Community Podcast Hub (coming soon)  
- 📖 Workshop Materials (upload & share)  
- 📊 Growth Dashboard (future feature)  
""")

# ----------------------------
# Footer
# ----------------------------
st.write("---")
st.markdown("""
🌟 **Influx Podcast Plan** – Built for Collaboration, Learning, and Growth  
💡 Plan smarter. Collaborate better. Inspire together.  
👉 Discover more at **[EntreMotivator Cards](http://entremotivator.com/landing/more)**  
""")
