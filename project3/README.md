# About Sparkify

**Sparkify** is a music streaming platform (i.e.: Spotify) in which users' activity & song meta data are collected for data analysis purposes.

# Data Lake with Spark

The goal of this project is to build the Data Lake as it is seen below.
![image](https://user-images.githubusercontent.com/81280674/122188772-41a5cd00-cecb-11eb-91a2-2ecb264a7fe9.png)

# How to run

Execute the python script `etl.py` (eg.: `python etl.py`).  
This will trigger both processes to **process the song data** and **process the log (user activity) data**.

# File Structure

In project3 this is what each file represent
```sh
/data         # Sample data
  log-data.zip
  song-data.zip
.gitignore    # File to be ignored
dl.cfg        # MAKE SURE YOU DON'T PUSH THIS TO GIT
etl.py        # Python script to run the ELT (Extract Load Transform) process
README.md     # Documentation
```

# Table schema

![image](https://user-images.githubusercontent.com/81280674/122728605-45629680-d2b3-11eb-8fd0-151e2c5a8bb3.png)

# Author

**Giwoo Lee**
Software Engineer / Data Engineer
[linkedin](https://linkedin.com/in/leegiwoo)
