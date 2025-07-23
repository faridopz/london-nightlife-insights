import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 7)
os.makedirs("visuals", exist_ok=True)

# Load data
venue_demo = pd.read_csv("outputs/venue_demo_tickets.csv")
demo_totals = pd.read_csv("outputs/demo_ticket_totals.csv")
solo_rate = pd.read_csv("outputs/solo_attendance_rate_by_demo.csv")
avg_tickets = pd.read_csv("outputs/avg_tickets_per_purchase_demo.csv")

#  Venue ticket sales by demographic heatmap (Age vs Gender per Venue)
plt.figure(figsize=(14, 10))
pivot_venue_demo = venue_demo.pivot_table(
    index="Age_Group", columns=["Venue", "Gender"], values="Quantity", aggfunc='sum', fill_value=0
)
sns.heatmap(pivot_venue_demo, cmap="YlGnBu", linewidths=.5)
plt.title("Ticket Sales by Age Group & Gender across Venues")
plt.xlabel("Venue and Gender")
plt.ylabel("Age Group")
plt.tight_layout()
plt.savefig("visuals/venue_ticket_sales_heatmap.png")
plt.close()
print("Saved visuals/venue_ticket_sales_heatmap.png")

#  Top demographics overall (Total tickets bought)
top_demos = demo_totals.sort_values("Quantity", ascending=False)
plt.figure()
sns.barplot(data=top_demos, x="Quantity", y="Age_Group", hue="Gender", palette="pastel")
plt.title("Total Tickets Bought by Age Group and Gender")
plt.xlabel("Tickets Bought")
plt.ylabel("Age Group")
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig("visuals/total_tickets_by_demo.png")
plt.close()
print("Saved visuals/total_tickets_by_demo.png")

#  Solo Attendance Rate (who tends to attend alone)
plt.figure()
sns.barplot(data=solo_rate, x="Solo_Rate", y="Age_Group", hue="Gender", palette="coolwarm")
plt.title("Solo Attendance Rate by Age Group and Gender")
plt.xlabel("Average Solo Attendance Rate")
plt.ylabel("Age Group")
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig("visuals/solo_attendance_rate.png")
plt.close()
print("Saved visuals/solo_attendance_rate.png")

#  Average Tickets per Purchase (group buying tendencies)
plt.figure()
sns.barplot(data=avg_tickets, x="Quantity", y="Age_Group", hue="Gender", palette="muted")
plt.title("Average Tickets per Purchase by Age Group and Gender")
plt.xlabel("Average Tickets per Purchase")
plt.ylabel("Age Group")
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig("visuals/avg_tickets_per_purchase.png")
plt.close()
print("Saved visuals/avg_tickets_per_purchase.png")

print("All demographic and venue audience insights visuals saved in 'visuals/' folder.")
