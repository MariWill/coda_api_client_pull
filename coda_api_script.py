import requests

# Coda API setup
API_KEY = "4235673c-2125-48ad-bc20-98e668416a35"
DOC_ID = "4LndUt65jh"  # replace with your doc ID if different
TABLE_ID = "table-RsILecYX3x"  # Top 250 Status table

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Fetch all rows from the Top 250 Status table
url = f"https://coda.io/apis/v1/docs/{DOC_ID}/tables/{TABLE_ID}/rows"
response = requests.get(url, headers=headers)
data = response.json()

# Column IDs
cols = {
    "ClientNumber": "c-I3SFyMjYXU",
    "ClientName": "c-hL1jysM-hb",
    "WorkedFees": "c-YvBPP50qTj",
    "RateProcessStatus": "c-ECTgzxg_H9"
}

# Extract the rows
top_clients = []
for row in data.get('items', []):
    top_clients.append({
        "ClientNumber": row['values'].get(cols["ClientNumber"]),
        "ClientName": row['values'].get(cols["ClientName"]),
        "WorkedFees": row['values'].get(cols["WorkedFees"]),
        "RateProcessStatus": row['values'].get(cols["RateProcessStatus"])
    })

# Sort by Worked Fees descending
top_clients_sorted = sorted(top_clients, key=lambda x: x['WorkedFees'] or 0, reverse=True)

# Keep only top 250
top_250 = top_clients_sorted[:250]

# Print results
for client in top_250:
    print(client)
    
import csv

# CSV filename
filename = "top_250_clients.csv"

# Columns for CSV
fieldnames = ["ClientNumber", "ClientName", "WorkedFees", "RateProcessStatus"]

# Write CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for client in top_250:
        writer.writerow(client)

print(f"CSV exported successfully as {filename}")












