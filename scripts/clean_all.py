import pandas as pd
import os

def clean_events(input_path, output_path):
    df = pd.read_csv(input_path)
    df['Event_Name'] = df['Event_Name'].str.title().str.strip()
    df['Venue'] = df['Venue'].str.title().str.strip()
    df['Genre'] = df['Genre'].str.title().str.strip()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Event_ID', 'Venue', 'Event_Name', 'Date', 'Genre', 'Tickets_Available'], inplace=True)
    df['Event_ID'] = df['Event_ID'].astype(int)
    df['Tickets_Available'] = df['Tickets_Available'].astype(int)
    df.to_csv(output_path, index=False)
    print(f" Cleaned events → {output_path}")

def clean_sales(input_path, output_path):
    df = pd.read_csv(input_path)
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'], errors='coerce')
    df['Quantity'] = df['Quantity'].astype(int)
    df['Price_Per_Ticket'] = df['Price_Per_Ticket'].astype(float)
    df['Revenue'] = df['Quantity'] * df['Price_Per_Ticket']
    df.dropna(subset=['Event_ID', 'Sale_Date', 'Quantity', 'Price_Per_Ticket'], inplace=True)
    df.to_csv(output_path, index=False)
    print(f" Cleaned sales → {output_path}")

def clean_attendees(input_path, output_path):
    df = pd.read_csv(input_path)
    df['Age'] = df['Age'].astype(int)
    df['Gender'] = df['Gender'].str.title().str.strip()
    df['City'] = df['City'].str.title().str.strip()
    df.dropna(subset=['Event_ID', 'Age', 'Gender', 'City'], inplace=True)
    df.to_csv(output_path, index=False)
    print(f" Cleaned attendees → {output_path}")

if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)
    
    clean_events("data/raw/events.csv", "data/processed/events_clean.csv")
    clean_sales("data/raw/sales.csv", "data/processed/sales_clean.csv")
    clean_attendees("data/raw/attendees.csv", "data/processed/attendees_clean.csv")
