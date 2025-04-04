import psycopg2

# Redshift Configuration
REDSHIFT_HOST = "your-redshift-cluster-endpoint"
REDSHIFT_DB = "yourdb"
REDSHIFT_USER = "youruser"
REDSHIFT_PASSWORD = "yourpassword"
REDSHIFT_PORT = 5439

def load_to_redshift():
    conn = psycopg2.connect(
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    cursor = conn.cursor()

    cursor.execute("""
        COPY arsenal_stats FROM 's3://your-s3-bucket/arsenal_cleaned.csv'
        IAM_ROLE 'your-iam-role'
        CSV IGNOREHEADER 1;
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded into Redshift.")

if __name__ == "__main__":
    load_to_redshift()
