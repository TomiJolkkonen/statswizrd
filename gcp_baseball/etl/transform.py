import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class TransformDodgersStats(beam.DoFn):
    def process(self, element):
        record = json.loads(element)
        transformed = [{"Stat": k, "Value": v} for k, v in record.items()]
        return transformed

def run():
    options = PipelineOptions(
        runner="DataflowRunner",
        project="your-gcp-project",
        temp_location="gs://your-gcs-bucket/temp"
    )

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | "Read GCS" >> beam.io.ReadFromText("gs://your-gcs-bucket/dodgers_stats.json")
            | "Transform Data" >> beam.ParDo(TransformDodgersStats())
            | "Write to GCS" >> beam.io.WriteToText("gs://your-gcs-bucket/dodgers_cleaned", file_name_suffix=".json")
        )

if __name__ == "__main__":
    run()
