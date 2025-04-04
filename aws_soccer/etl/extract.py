import requests
from bs4 import BeautifulSoup
import json
import boto3

# AWS S3 Configuration
BUCKET_NAME = "your-s3-bucket"
S3_KEY = "arsenal_stats.json"

def scrape_whoscored():
    url = "https://www.whoscored.com/teams/13/show/england-arsenal"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Extract team statistics (modify this based on structure)
    stats = {}
    for stat in soup.find_all("div", class_="stat"):
        stat_name = stat.find("span", class_="stat-name").text.strip()
        stat_value = stat.find("span", class_="stat-value").text.strip()
        stats[stat_name] = stat_value

    return stats

def upload_to_s3(data):
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=S3_KEY,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    print(f"Data uploaded to S3: s3://{BUCKET_NAME}/{S3_KEY}")

if __name__ == "__main__":
    data = scrape_whoscored()
    upload_to_s3(data)
