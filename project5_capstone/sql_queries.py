#################
## DROP TABLES ##
#################
airports_table_drop = "DROP TABLE IF EXISTS airports";
demographics_table_drop = "DROP TABLE IF EXISTS demographics";
immigrations_table_drop = "DROP TABLE IF EXISTS immigrations";
temperatures_table_drop = "DROP TABLE IF EXISTS temperatures";

drop_tables = [
    airports_table_drop,
    demographics_table_drop,
    immigrations_table_drop,
    temperatures_table_drop
]

#################
# CREATE TABlES #
#################
airports_table_create = """
    CREATE TABLE IF NOT EXISTS airports_table (
        iata_code      VARCHAR PRIMARY KEY,
        name           VARCHAR,
        type           VARCHAR,
        local_code     VARCHAR,
        coordinates    VARCHAR,
        city           VARCHAR,
        elevation_ft   VARCHAR,
        continent      VARCHAR,
        iso_country    VARCHAR,
        iso_region     VARCHAR,
        municipality   VARCHAR,
        gps_code       VARCHAR
    );
"""

demographics_table_create = """
    CREATE TABLE IF NOT EXISTS demographics_table (
        city                   VARCHAR,
        state                  VARCHAR,
        media_age              FLOAT,
        male_population        INT,
        female_population      INT,
        total_population       INT,
        num_veterans           INT,
        foreign_born           INT,
        average_household_size FLOAT,
        state_code             VARCHAR(2),
        race                   VARCHAR,
        count                  INT
    );
"""

immigrations_table_create = """
    CREATE TABLE IF NOT EXISTS immigrations (
        cicid            FLOAT PRIMARY KEY,
        year             FLOAT,
        month            FLOAT,
        cit              FLOAT,
        res              FLOAT,
        iata             VARCHAR(3),
        arrdate          FLOAT,
        mode             FLOAT,
        addr             VARCHAR,
        depdate          FLOAT,
        bir              FLOAT,
        visa             FLOAT,
        count            FLOAT,
        dtadfile         VARCHAR,
        entdepa          VARCHAR(1),
        entdepd          VARCHAR(1),
        matflag          VARCHAR(1),
        biryear          FLOAT,
        dtaddto          VARCHAR,
        gender           VARCHAR(1),
        airline          VARCHAR,
        admnum           FLOAT,
        fltno            VARCHAR,
        visatype         VARCHAR
    );
"""

temperatures_table_create = """
CREATE TABLE IF NOT EXISTS temperatures (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

create_tables = [
    airports_table_create,
    demographics_table_create,
    immigrations_table_create,
    temperatures_table_create
]


#################
# INSERT TABLES #
#################
airports_table_insert = """
    INSERT INTO airports (iata_code, name, type, local_code, coordinates,
                          city, elevation_ft, continent, iso_country, iso_region,
                          municipality, gps_code)
                  VALUES (%s, %s, %s, %s, %s, 
                          %s, %s, %s, %s, %s,
                          %s, %s)
"""

demographics_table_insert = """
    INSERT INTO demographics (city, state, media_age, male_population,
                              female_population, total_population, num_veterans, foreign_born,
                              average_household_size, state_code, race, count)
                      VALUES (%s, %s, %s, %s,
                              %s, %s, %s, %s,
                              %s, %s, %s, %s)
"""

immigrations_table_insert = """
    INSERT INTO immigrations (cicid, year, month, cit, res, iata, arrdate,
                              mode, addr, depdate, bir, visa, count, dtadfile,
                              entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, 
                              admnum, fltno, visatype)
                      VALUES (%s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s)
"""

temperatures_table_insert = """
    INSERT INTO temperatures (timestamp, average_temperature, average_temperature_uncertainty,
                             city, country, latitude, longitude)
                     VALUES (%s, %s, %s,
                             %s, %s, %s, %s)
"""