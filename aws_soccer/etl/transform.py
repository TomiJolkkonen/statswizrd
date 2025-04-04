import boto3
import json
import pandas as pd

BUCKET_NAME = "your-s3-bucket"
S3_KEY = "arsenal_stats.json"
OUTPUT_KEY = "arsenal_cleaned.csv"

s3 = boto3.client("s3")

def transform_data():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=S3_KEY)
    raw_data = json.loads(obj["Body"].read().decode("utf-8"))
    
    df = pd.DataFrame(list(raw_data.items()), columns=["Stat", "Value"])
    
    output_csv = "/tmp/arsenal_cleaned.csv"
    df.to_csv(output_csv, index=False)

    s3.upload_file(output_csv, BUCKET_NAME, OUTPUT_KEY)
    print(f"Transformed data uploaded to s3://{BUCKET_NAME}/{OUTPUT_KEY}")

if __name__ == "__main__":
    transform_data()
