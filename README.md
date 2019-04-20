Project Name: News Website Logs Analysis Statistics

This project sets up a PostgreSQL database for a news website.
The provided Python script log_analysis.py uses the psycopg2 library to query
the database and produce a report that answers the following questions.

1. What are the most popular three articles of all time.
2. Who are the most popular article authors of all time.
3. On which days did more than 1% of requests lead to errors.

For this project, first of all you need to download news data from here (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
, unzip this and import news.sql into PostgreSQL database using following command

$ psql -d news -f news.sql

Open up terminal and run this command - python log_analysis.py

$ python log_analysis.py

I have created two views here - all_calls and error_calls

all_call - 

create view all_calls as select DATE(time) as date, count(*) as all_count from log group by DATE(time)

this view constains date wise all api calls irrespective of whether it is success or error calls.

error_calls -

create view error_calls as select DATE(time) as date, count(*) as error_count from log where status ='404 NOT FOUND' group by DATE(time), status

date wise number of error calls.

Above two views helped a lot in finding out % error calls.
