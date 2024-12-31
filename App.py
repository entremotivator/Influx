import streamlit as st
from datetime import date, timedelta

# List of participants from the room
participants = [
    "Influx", "Jasmine", "CEEZ", "Richard", 
    "EntreMotivator", "One_Love", "3partner", 
    "Radio", "Pierre", "RENEE", "Mr.Chris", "Michelle"
]

# App Title
st.title("Influx Podcast Plan")

# Current date and week range
today = date.today()
start_of_week = today - timedelta(days=today.weekday())
end_of_week = start_of_week + timedelta(days=6)

# Calendar Section
st.header("Weekly Calendar")
st.write(f"Week: {start_of_week.strftime('%B %d, %Y')} - {end_of_week.strftime('%B %d, %Y')}")

# Generate a weekly calendar
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
schedule = {day: [] for day in days_of_week}

# Assign participants to podcast episodes (one per day)
for i, day in enumerate(days_of_week):
    schedule[day].append(f"Podcast Host: {participants[i % len(participants)]}")

# Teaching session on Wednesday
schedule["Wednesday"].append("Teaching Session: Hosted by RENEE")

# Display the schedule
for day, events in schedule.items():
    st.subheader(day)
    for event in events:
        st.write(event)

# Additional Features
st.header("Add Events")
event_name = st.text_input("Event Name", "")
event_day = st.selectbox("Select Day", days_of_week)
event_host = st.selectbox("Select Host", participants)

if st.button("Add Event"):
    if event_name and event_day and event_host:
        schedule[event_day].append(f"{event_name}: Hosted by {event_host}")
        st.success(f"Added event '{event_name}' to {event_day}, hosted by {event_host}")
    else:
        st.error("Please fill out all fields to add an event.")

# Footer
st.write("**Created for the Influx Entrepreneur Room**")
