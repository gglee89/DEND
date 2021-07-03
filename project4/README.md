# Project: Data Pipelines with Airflow

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

# How to Run

# File Structure

```sh
/dags
  udac_example_dag.py
/data
  log_data.zip
  song_data.zip
/notes
  README.md
/plugins
  /helpers
    __init__.py
    sql_queries.py
  /operators
    __init__.py
    data_quality.py
    load_dimension.py
    load_fact.py
    stage_redshift.py
  __init__.py
create_tables.sql
```

# Tasks

- [] Implement four empty operators that needs to be made into functional pieces of the data pipeline;
- [] Link set of tasks to achieve a coherent and sensible data flow within the pipeline; (ie.: Configure task dependencies so that after the dependencies are set, the graph view follows the flow shown in the image below.)
- []

# Steps for the pipeline

**Guidelines:**

- Staging the data
- Filling the data
- Warehouse
-

# Author

Giwoo G Lee
