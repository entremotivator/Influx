import streamlit as st
from datetime import date, timedelta
import pandas as pd

# List of participants with optional descriptions
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

# Function to initialize a blank weekly schedule
def create_blank_schedule():
    return {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

# App title and introduction
st.title("Influx Podcast Plan")
st.subheader("Collaborative Weekly Podcast and Teaching Schedule")

# Get the current date and week
today = date.today()
start_of_week = today - timedelta(days=today.weekday())
end_of_week = start_of_week + timedelta(days=6)

# Calendar Section
st.header("Current Week Schedule")
st.write(f"**Week: {start_of_week.strftime('%B %d, %Y')} - {end_of_week.strftime('%B %d, %Y')}**")

# Weekly schedule initialization
schedule = create_blank_schedule()

# Assign participants to podcast episodes (1 per week)
for i, (name, description) in enumerate(participants.items()):
    day = list(schedule.keys())[i % 7]
    schedule[day].append(f"Podcast Episode: Hosted by {name} - {description}")

# Assign a teaching session (Wednesday by default)
schedule["Wednesday"].append("Teaching Session: Hosted by RENEE")

# Display the current schedule
for day, events in schedule.items():
    st.subheader(day)
    if events:
        for event in events:
            st.write(event)
    else:
        st.write("No events scheduled.")

# Add or Modify Events
st.header("Manage Events")
event_name = st.text_input("Enter Event Name", "")
event_day = st.selectbox("Select Day", list(schedule.keys()))
event_host = st.selectbox("Select Host", list(participants.keys()))
is_recurring = st.checkbox("Make this a weekly recurring event")

if st.button("Add Event"):
    if event_name and event_day and event_host:
        new_event = f"{event_name}: Hosted by {event_host}"
        schedule[event_day].append(new_event)
        st.success(f"Added event: {new_event} on {event_day}")
        if is_recurring:
            st.info(f"This event will repeat weekly on {event_day}.")
    else:
        st.error("Please complete all fields to add an event.")

# Plan for Future Weeks
st.header("Plan for Future Weeks or Months")
weeks_ahead = st.number_input("Weeks Ahead", min_value=1, max_value=52, value=1)
future_start = start_of_week + timedelta(weeks=weeks_ahead * 7)
future_end = future_start + timedelta(days=6)
st.write(f"**Future Week: {future_start.strftime('%B %d, %Y')} - {future_end.strftime('%B %d, %Y')}**")

future_event_name = st.text_input("Future Event Name", "")
future_event_day = st.selectbox("Select Day for Future Event", list(schedule.keys()))
future_event_host = st.selectbox("Select Host for Future Event", list(participants.keys()))

if st.button("Add Future Event"):
    if future_event_name and future_event_day and future_event_host:
        st.success(f"Future Event Added: '{future_event_name}' on {future_event_day}, hosted by {future_event_host}")
    else:
        st.error("Please complete all fields to add a future event.")

# Export Schedule
st.header("Export Schedule")
if st.button("Export Current Week"):
    df = pd.DataFrame([
        {"Day": day, "Events": ", ".join(events)} 
        for day, events in schedule.items()
    ])
    csv = df.to_csv(index=False)
    st.download_button("Download Schedule as CSV", data=csv, file_name="weekly_schedule.csv", mime="text/csv")
    st.success("Schedule exported successfully!")

# Display Participant Profiles
st.header("Host Profiles")
for name, description in participants.items():
    st.subheader(name)
    st.write(description)

# Footer
st.write("---")
st.write("**Influx Podcast Plan** - Designed for Collaboration, Learning, and Growth")
