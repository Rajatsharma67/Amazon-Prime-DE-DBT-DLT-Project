import sqlite3
import dlt


def amazon_ops_source():
    conn = sqlite3.connect("RSDB.db")
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name='amazon_ops'
    """)

    if not cursor.fetchone():
        raise Exception("Table 'amazon_ops' does not exist in RSDB.db")

    cursor.execute("SELECT * FROM amazon_ops")

    columns = [c[0] for c in cursor.description]

    for row in cursor.fetchall():
        yield dict(zip(columns, row))


# ✅ Convert to proper dlt resource
@dlt.resource(name="amazon_prime_raw")
def amazon_prime_resource():
    yield from amazon_ops_source()


# Pipeline
pipeline = dlt.pipeline(
    pipeline_name="sqlite_pipeline",
    destination="postgres",
    dataset_name="analytics_raw",
    dev_mode=False,
)

load_info = pipeline.run(
    amazon_prime_resource(),
    table_name="amazon_prime_raw",
    write_disposition="replace"
)

print(load_info)