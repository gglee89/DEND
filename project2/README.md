# Project: Sparkify (Data Warehouse with AWS Redshift)

Udacity's Data Engineering Nanodegree project.

# About this project

As part of the Nanodegree program, the **Sparkify** project asks students to build a Datawarehousing application with AWS Redshift. This project consists of 4 (four) steps that needs to be manually executed in order to successfully execute the **ETL pipeline**. The steps are:

- Setup AWS Redshift clusters
  - Use **AWSSDK** (needs client_key & client_secret)
  - Use **IaC (Infrastructure as code)** principles to spin-off AWS Redshift clusters
- Create tables (scripts/create_tables.py ==> scripts/sql_queries.py)
- Run ETL pipelines (scripts/etl.py ==> scripts/sql_queries.py)
- Test analytics queries

#### What is Sparkify?

The dataset is used to replicate a scenario you may find in a MUSIC STREAMING APP. As an analogy, we can think of it as a SMALL SUBSET of dataset from a major company like **Apple Music**, **Soundcloud**, and **etc**

#### How is this project going to help?

We can identify cases such as:

- What time of the day are users listening to music the most?
- Are users going to UPGRADE or DOWNGRADE their service plans?
- What are the top country that listens to music on Sparkify?
- etc.

# File Architecture

```js
/project2
  /scripts
    create_tables.py
    etl.py
    sql_queries.py
  awsconnect.ipynb
  awsexecute.ipynb
  *dwh.cfg
  README.md
  .gitignore
```

# ETL Architecture

![image](https://user-images.githubusercontent.com/16644017/121112410-56d78780-c84b-11eb-8e8d-8f03f698b494.png)

# ER Diagram

![image](https://user-images.githubusercontent.com/16644017/121111193-69e95800-c849-11eb-8b9b-ad394c60269e.png)

# Steps to execute the data processing pipepine

**[awsconnect.ipynb]**

1. Setup AWS Redshift clusters

**[awsexecute.ipynb]**

1. Create tables
2. ETL Pipelines
3. Test analytics queries

# Author

**Giwoo G Lee**
Data Engineer
[Linkedin](https://linkedin.com/in/leegiwoo)
