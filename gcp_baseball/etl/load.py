from google.cloud import bigquery

# BigQuery Configuration
BQ_PROJECT = "your-gcp-project"
BQ_DATASET = "baseball_stats"
BQ_TABLE = "dodgers_stats"
GCS_FILE_PATH = "gs://your-gcs-bucket/dodgers_cleaned-00000-of-00001.json"

def load_to_bigquery():
    client = bigquery.Client()
    dataset_ref = client.dataset(BQ_DATASET)
    table_ref = dataset_ref.table(BQ_TABLE)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
    )

    load_job = client.load_table_from_uri(
        GCS_FILE_PATH, table_ref, job_config=job_config
    )

    load_job.result()
    print("Data loaded into BigQuery.")

if __name__ == "__main__":
    load_to_bigquery()
