This file shows how to run log analysis in order to get following metrices
1. What are the most popular three articles of all time.
2. Who are the most popular article authors of all time.
3. On which days did more than 1% of requests lead to errors.

Open up terminal and run this command - python log_analysis.py

I have created two views here - all_calls and error_calls
all_call - this view constains date wise all api calls irrespective of whether it is success or error calls.
error_calls - date wise number of error calls.

Above two views helped a lot in finding out % error calls.
