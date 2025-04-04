CREATE EXTERNAL TABLE IF NOT EXISTS la_kings_stats (
    Stat STRING,
    Value STRING
)
STORED AS PARQUET
LOCATION '/user/hadoop/la_kings_stats/cleaned_data.parquet';


-- run this in Hive CLI: hive -f hive_queries.sql
