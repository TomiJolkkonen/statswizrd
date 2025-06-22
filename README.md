# statswizrd
data analytics of hockey, soccer, baseball

---------------------------------------------------------------------------------------------------
AWS:
Data Source: S3, DynamoDB, RDS, API Gateway, Kinesis

Ingest: AWS Glue Crawlers, Lambda, Kinesis Firehose

Transformation: AWS Glue (Spark/PySpark), EMR, Athena (SQL)

Storage & Modeling: Amazon S3 (data lake), Amazon Redshift (DWH), Glue Data Catalog

Visualization: Amazon QuickSight

--------------------------------------------------------------------------------------------------
GCP:
Data Source: Google Cloud Storage, Cloud SQL, Pub/Sub, APIs

Ingest: Dataflow (Apache Beam), Cloud Functions, Pub/Sub

Transformation: Dataflow (Python/Java), BigQuery SQL

Storage & Modeling: BigQuery (lakehouse/DWH), Cloud Storage

Visualization: Looker Studio (formerly Data Studio)

-----------------------------------------------------------------------------------------------------
Databricks:
Data Source: Any cloud storage, Kafka, APIs, Delta Live Tables

Ingest: Auto Loader, Structured Streaming, dbutils, REST APIs

Transformation: PySpark, SQL, Notebooks, MLlib

Storage & Modeling: Delta Lake, Unity Catalog

Visualization: Built-in dashboards, or Power BI, Looker, Tableau

---------------------------------------------------------------------------------------------------------
Apache Superset:
Data Source: PostgreSQL, MySQL, Presto, Trino, Druid, BigQuery, etc.

Ingest: Not handled by Superset – use external tools (Airflow, dbt, Spark, etc.)

Transformation: Done in the data source (via SQL, dbt, etc.)

Storage & Modeling: Superset doesn't store data – uses external DBs or views

Visualization: Dashboards and charts from SQL queries or datasets
