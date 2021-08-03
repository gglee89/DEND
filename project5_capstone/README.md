# About

This is the capstone project for the Udacity Data Engineering Nanodegree (DEND) program.

# Project summary

This project intends to demonstrate the combination of knowledge gained throughout the program. And following Udacity's instructions, this project is broken into 5 steps.

# Steps

1. **Scope the Project and Gather Data**
   Since the scope of the project will be highly dependent on the data, these two things happen simultaneously. Identify and gather the data to use for the project (at least two sources and more than 1 million rows). See Project Resources for ideas of what data you can use. - Explain what end use cases you'd like to prepare the data for (e.g., analytics table, app back-end, source-of-truth database, etc.)
2. **Explore and Assess the Data**
   - Explore the data to identify data quality issues, like missing values, duplicate data, etc.
   - Document steps necessary to clean the data
3. **Define the Data Model**
   - Map out the conceptual data model and explain why you chose that model
   - List the steps necessary to pipeline the data into the chosen data model
4. **Run ETL to Model the Data**
   - Create the data pipelines and the data model.
   - Include a data dictionary.
   - Run data quality checks to ensure the pipeline ran as expected
     - Integrity constraints on the relational database (eg.: Unique key, Data type, etc.)
     - Unit tests for the scripts to ensure they are doing the right thing
     - Source/count checks to ensure completeness
5. **Complete Project Write Up**
   - What's the goal? What queries will you want to run? How would Spark or Airflow be incorporated? Why did you choose the model you chose?
   - Clearly state the rationale for the choice of tools and technologies for the project.
   - Document the steps of the process.
   - Propose how often the data should be updated and why.
   - Post your write-up and final data model in a GitHub repo.
   - Include a description of how you would approach the problem differently under the following scenarios:
     - If the data was increased by 100x.
     - If the pipelines were run on a daily basis by 7am.
     - If the database needed to be accessed by 100+ people.

# Research questions

1. What are the top 10 airports where immigration into the US went through?
2. What are the top 10 cities in the US with most immigrants?
3. What are the temperature of the top 10 cities with most immigrants?

# Data source

- **I94 Immigration data**
  - This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace. This is where the data comes from. There's a sample file so you can take a look at the data in csv format before reading it all in. You do not have to use the entire dataset, just use what you need to accomplish the goal you set at the beginning of the project.
- **World Temperature Data**
  - This dataset came from Kaggle
- **U.S. City Demographic Data**
  - This data comes from OpenSoft.
- **Airport Code Table**
  - This is a simple table of airport codes and corresponding cities.

# Architecture

![image](https://user-images.githubusercontent.com/81280674/126436051-bd8ede22-3321-4f94-8add-f4637efbd546.png)

# File Structure

```sh
README.md                 # Documentation
```

# Author

**Giwoo G Lee**
Data Engineer  
[Linkedin](https://linkedin.com/in/leegiwoo)
