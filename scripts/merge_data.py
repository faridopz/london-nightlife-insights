import pandas as pd
import os

def merge_data(events_path, sales_path, attendees_path, output_path):
    # Load cleaned datasets
    events = pd.read_csv(events_path)
    sales = pd.read_csv(sales_path)
    attendees = pd.read_csv(attendees_path)

    # Merge events ↔ sales
    events_sales = pd.merge(events, sales, on="Event_ID", how="left")

    # Merge with attendees
    merged = pd.merge(events_sales, attendees, on="Event_ID", how="left")

    # Save to output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged.to_csv(output_path, index=False)
    print(f" Merged dataset saved → {output_path}")
    return merged

if __name__ == "__main__":
    merge_data(
        "data/processed/events_clean.csv",
        "data/processed/sales_clean.csv",
        "data/processed/attendees_clean.csv",
        "data/processed/merged.csv"
    )
