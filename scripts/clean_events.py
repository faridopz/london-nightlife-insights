import pandas as pd
import os

def clean_events(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)
    
    # Convert to title case and strip spaces
    df['Event_Name'] = df['Event_Name'].str.title().str.strip()
    df['Venue'] = df['Venue'].str.title().str.strip()
    df['Genre'] = df['Genre'].str.title().str.strip()
    
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Drop any rows with missing critical fields
    df.dropna(subset=['Event_ID', 'Venue', 'Event_Name', 'Date', 'Genre', 'Tickets_Available'], inplace=True)
    
    # Ensure correct types
    df['Event_ID'] = df['Event_ID'].astype(int)
    df['Tickets_Available'] = df['Tickets_Available'].astype(int)
    
    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f" Cleaned events saved to: {output_path}")

if __name__ == "__main__":
    input_file = "data/raw/events.csv"
    output_file = "data/processed/events_clean.csv"
    clean_events(input_file, output_file)
