
import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config.get('AWS', 'AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('AWS','AWS_SECRET_ACCESS_KEY')


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Process the song data
    
    - 1. Reads the song dataset from s3 bucket
    - 2. Process the file with Spark
    - 3. Saves in a difference bucket
    """
    # get filepath to song data file
    file_path = input_data + 'song_data/*/*/*/*.json'
        
    # read song data file
    df_song = spark.read.json(file_path)

    # create view in spark
    songs_table = df_song.createOrReplaceTempView('song_table')
    
    # write songs table to parquet files partitioned by year and artist
    songs_table = spark.sql("""
        SELECT DISTINCT s.song_id,
                        s.title,
                        s.artist_id,
                        s.year,
                        s.duration
                   FROM song_table as s
                  WHERE stb.song_id IS NOT NULL
    """)

    # writes them to partitioned parquet files in table directories on S3.
    songs_table.write.mode('overwrite').partitionBy('year', 'artist_id').parquet(output_data+'songs_table/')

    # extract columns to create artists table
    artists_table = spark.sql("""
        SELECT DISTINCT s.artist_id,
                        s.artist_name,
                        s.artist_location,
                        s.artist_latitude,
                        s.artist_longitude
                   FROM song_table s
                  WHERE s.artist_id IS NOT NULL
    """)
    
    # write artists table to parquet files
    artists_table = artists_table.write.mode('overwrite').parquet(output_data+'artists_table/')


def process_log_data(spark, input_data, output_data):
    """
    Process the log data (User activity)
    
    - 1. Reads the log dataset from s3 bucket
    - 2. Process the file with Spark
    - 3. Saves in a difference bucket
    """
    
    # get filepath to log data file
    log_path = input_data + 'log_data/*/*/*.json'

    # read log data file
    df = spark.read.json(log_path)
    
    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong')

    # extract columns for users table    
    users_table = spark.sql("""
        SELECT DISTINCT l.userId,
                        l.firstName
                        l.lastName,
                        l.gender,
                        l.level
                   FROM log_table l
                  WHERE u.userId IS NOT NULL
    """)
    
#     # write users table to parquet files
    users_table.write.mode('overwrite').parquet(output_data+'users_table/')

#     # create timestamp column from original timestamp column
#     get_timestamp = udf()
#     df = 
    
#     # create datetime column from original timestamp column
#     get_datetime = udf()
#     df = 
    
    # extract columns to create time table
    time_table = spark.sql("""
        SELECT DISTINCT tm.start_time_sub,
                        hour(tm.start_time_sub),
                        dayofmonth(tm.start_time_sub),
                        weekofyear(tm.start_time_sub),
                        month(tm.start_time_sub),
                        year(tm.start_time_sub),
                        dayofweek(tm.start_time_sub)
                   FROM (SELECT to_timestamp(lt.ts/1000)
                           FROM log_table lt
                          WHERE lt.ts IS NOT NULL
                        ) tm
    """)
    
    # write time table to parquet files partitioned by year and month
    time_table.write.mode('overwrite').partitionBy("year", "month").parquet(output_data + 'time_table/')

    # read in song data to use for songplays table
    song_df = spark.read.parquet(output_data + '/songs_table')
    song_df.createOrReplaceTempView('songs_table')

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = spark.sql("""
        SELECT monotonically_increasing_id(),
                to_timestamp(lt.ts/1000),
                month(to_timestamp(lt.ts/1000)),
                year(to_timestamp(lt.ts/1000)),
                lt.userId,
                lt.level,
                st.song_id,
                st.artist_id,
                lt.sessionId,
                lt.location,
                lt.userAgent
           FROM log_table lt
           JOIN song_table st on lt.artist = st.artist_name AND lt.song = st.title
    """)

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.mode('overwrite').partitionBy('year', 'month').parquet(output_data + 'songs_table/')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://data-lake.dend/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
