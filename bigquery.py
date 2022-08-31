import io

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

file_path = '/Users/dan/lubycon/lubycon-event-gateway/data.json'
table_id = "lubycon-mgmt.sandbox.test"

job_config = bigquery.LoadJobConfig(
    schema_update_options=bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    autodetect=True, source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
