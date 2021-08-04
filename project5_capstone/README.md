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
  - This dataset came from Kaggle. You can read more about it [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)
- **U.S. City Demographic Data**
  - This data comes from OpenSoft. You can read more about it [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)
- **Airport Code Table**
  - This is a simple table of airport codes and corresponding cities.

# Architecture

![image](https://user-images.githubusercontent.com/81280674/126436051-bd8ede22-3321-4f94-8add-f4637efbd546.png)

# File Structure

```sh
/config
  dwh.cfg                 # Configuration files for DB access
Captone Project.ipynb     # Jupyter notebook project
create_tables.py          # Python document for Table creation
sql_queries.py            # Python with DROP, CREATE, and INSERT queries
README.md                 # Documentation
```

# Data dictionary

#### airport_dim

| Attribute    | Description                                                   |
| ------------ | ------------------------------------------------------------- |
| iata_code    | International Air Transport Association - Location identifier |
| name         | Airport name                                                  |
| city         | Airport city                                                  |
| state        | Airport state                                                 |
| type         | Airport type                                                  |
| local_code   | Airport local_code                                            |
| coordinates  | Airport coordinates                                           |
| elevation_ft | Airport elevation_ft                                          |
| continent    | Airport continent                                             |
| iso_country  | Airport ISO Country                                           |
| iso_region   | Airport ISO Region                                            |
| municipality | Airport municipality                                          |
| gps_code     | Airport GPS Code                                              |

#### demographic_dim

| Attribute              | Description                                |
| ---------------------- | ------------------------------------------ |
| city                   | US City                                    |
| state                  | US State                                   |
| median_age             | US Median Age by City / State              |
| male_population        | US Male population by City / State         |
| female_population      | US Female population by City / State       |
| total_population       | US Total population by City / State        |
| number_of_veterans     | US number_of_veterans by City / State      |
| foreign_born           | foreign_born by City / State               |
| average_household_size | The average household size by City / State |
| state_code             | The state code                             |
| race                   | Ethnicity                                  |
| count                  | Total count                                |

#### temperature_dim

| Attribute                       | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| timestamp                       | Timestamp                                           |
| average_temperature             | Average temperature by City and Country             |
| average_temperature_uncertainty | Average temperature uncertainty by City and Country |
| city                            | City                                                |
| country                         | Country                                             |
| latitude                        | Latitude by City and Country                        |
| longitude                       | Longitude by City and Country                       |

#### immigration_fact

| Attribute | Description                                                                           |
| --------- | ------------------------------------------------------------------------------------- |
| cicid     | ID from SAS file                                                                      |
| year      | 4 digit year                                                                          |
| month     | Numeric month                                                                         |
| cit       | 3 digit code of source city for immigration (Born country)                            |
| res       | 3 digit code of source country for immigration (Residence country)                    |
| iata      | i94 port admitted through                                                             |
| arrdate   | Arrival date in the USA                                                               |
| mode      | Mode of transportation (1 = Air; 2 = Sea; 3 = Land; 9 = Not reported)                 |
| addr      | State of arrival                                                                      |
| depdate   | Departure date                                                                        |
| bir       | Age of respondents in Years                                                           |
| visa      | Visa codes collapsed into three categories: (1 = Business; 2 = Pleasure; 3 = Student) |
| count     | Total count                                                                           |
| dtadfile  | Character date field                                                                  |
| entdepa   | Arrival flag. Whether admitted or paroled into the US                                 |
| entdepd   | Departure flag. Update of Visa, either apprehend, overstayed, or updated to PR        |
| matflag   | Match flag                                                                            |
| biryear   | 4 digit year of birth                                                                 |
| dtaddto   | Character date field to when admitted in the US                                       |
| gender    | Gender                                                                                |
| airline   | Airline used to arrive in the US                                                      |
| admnum    | Admission number, should be unique and not nullable                                   |
| fltno     | Flight number or Airline used to arrive in the US                                     |
| visatype  | Class of admission legally admitting the non-immigrant to temporarily stay in the US  |

#

# Project write up

**Rationaly for the choice of tools and technologies for the project**
Pandas, numpy, psycopg2 are the python modules used to extract, manipulate, and store the data into POSTGRESQL

**How often the data should be update and why**
Weekly updates is recommended as it may provide weekly aggregations and reports of the US immigrations status

**If the data was increase by 100x**
Storing the data in S3 buckets to save costs, and making use of AWS EMR with Spark to parallelize the processing of files big enough that it consumes most processing resources of the uniquely allocated CPU.

**If the data populates a dashboard that must be updated on a daily basis by 7am every day**
Use Apache Airflow to run scheduled pipelines on a daily basis accounting it to finish before the dashboard needs to be used. In other words, have the pipeline run and complete its execution before 7am.

**If the database needed to be accessed by 100+ people**
AWS Redshift makes a good candidate to allow clustered and distributed processing of the data without having one process to delay the processing of other requests.

# Author

**Giwoo G Lee**
Data Engineer  
[Linkedin](https://linkedin.com/in/leegiwoo)
