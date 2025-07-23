import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/processed/merged.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Age group bins & labels
age_bins = [0, 17, 24, 34, 44, 54, 64, 120]
age_labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Ticket Volume by Venue & Demographic (Age + Gender)
venue_demo_tickets = df.groupby(['Venue', 'Age_Group', 'Gender'])['Quantity'].sum().reset_index()
venue_demo_tickets.to_csv("outputs/venue_demo_tickets.csv", index=False)

#  Total tickets bought per demographic across all venues (age+gender)
demo_ticket_totals = df.groupby(['Age_Group', 'Gender'])['Quantity'].sum().reset_index()
demo_ticket_totals = demo_ticket_totals.sort_values('Quantity', ascending=False)
demo_ticket_totals.to_csv("outputs/demo_ticket_totals.csv", index=False)

#  Solo Attendance Rate by Demographic
# Count unique (Attendee_ID, Event_ID) pairs = event visits
attendee_event_counts = df.groupby(['Attendee_ID', 'Event_ID']).size().reset_index(name='Tickets')
# Identify solo visits where attendee bought exactly 1 ticket for event
solo_visits = attendee_event_counts[attendee_event_counts['Tickets'] == 1]

# Merge solo visits back to main df to get demographics per solo visit
solo_demo = pd.merge(solo_visits, df[['Attendee_ID', 'Age_Group', 'Gender']], on='Attendee_ID', how='left').drop_duplicates()

# Calculate solo attendance rate by demographic
total_visits = df.groupby('Attendee_ID').size().reset_index(name='Total_Visits')
solo_visits_count = solo_demo.groupby('Attendee_ID').size().reset_index(name='Solo_Visits')
attendance_rates = pd.merge(total_visits, solo_visits_count, on='Attendee_ID', how='left').fillna(0)
attendance_rates['Solo_Rate'] = attendance_rates['Solo_Visits'] / attendance_rates['Total_Visits']

# Merge back demographic info and average solo rate by demographic
attendee_demo = df[['Attendee_ID', 'Age_Group', 'Gender']].drop_duplicates()
solo_rate_demo = pd.merge(attendance_rates, attendee_demo, on='Attendee_ID', how='left')
solo_rate_summary = solo_rate_demo.groupby(['Age_Group', 'Gender'])['Solo_Rate'].mean().reset_index()
solo_rate_summary.to_csv("outputs/solo_attendance_rate_by_demo.csv", index=False)

#  Average Tickets per Purchase by Demographic (age+gender)
avg_tickets_demo = df.groupby(['Age_Group', 'Gender'])['Quantity'].mean().reset_index()
avg_tickets_demo.to_csv("outputs/avg_tickets_per_purchase_demo.csv", index=False)

print("Deep demographic and venue insights analysis complete. CSVs saved to outputs/")
