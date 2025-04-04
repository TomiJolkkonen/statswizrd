import requests
from bs4 import BeautifulSoup
import json
from hdfs import InsecureClient

# HDFS Configuration
HDFS_URL = "http://localhost:9870"
HDFS_DIR = "/user/hadoop/la_kings_stats/"
HDFS_FILE = "raw_data.json"

def scrape_naturalstattrick():
    url = "https://www.naturalstattrick.com/teamreport.php?team=L.A"
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

def upload_to_hdfs(data):
    client = InsecureClient(HDFS_URL, user="hadoop")
    with client.write(HDFS_DIR + HDFS_FILE, encoding="utf-8") as writer:
        json.dump(data, writer)
    print(f"Data uploaded to HDFS: {HDFS_DIR}{HDFS_FILE}")

if __name__ == "__main__":
    data = scrape_naturalstattrick()
    upload_to_hdfs(data)
