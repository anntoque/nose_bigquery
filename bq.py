from google.cloud import bigquery

client = bigquery.Client()
QUERY = (
    'SELECT 1 as test_row')

query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.test_row)