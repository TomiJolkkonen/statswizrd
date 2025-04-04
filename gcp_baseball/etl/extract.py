import requests
from bs4 import BeautifulSoup
import json
from google.cloud import storage

# Google Cloud Storage Configuration
BUCKET_NAME = "your-gcs-bucket"
GCS_FILE = "dodgers_stats.json"

def scrape_fangraphs():
    url = "https://www.fangraphs.com/teams/dodgers"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract stats (Modify this based on actual page structure)
    stats = {}
    for row in soup.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) > 1:
            stat_name = columns[0].text.strip()
            stat_value = columns[1].text.strip()
            stats[stat_name] = stat_value

    return stats

def upload_to_gcs(data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(GCS_FILE)
    blob.upload_from_string(json.dumps(data), content_type="application/json")
    print(f"Data uploaded to GCS: gs://{BUCKET_NAME}/{GCS_FILE}")

if __name__ == "__main__":
    data = scrape_fangraphs()
    upload_to_gcs(data)
