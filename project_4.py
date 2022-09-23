# This is our project 3 script that will preform the tasks required in the lab
import requests
from os.path import exists
import re

# Set variables for static values, url, dates etc
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

# check for cached log file or pull the log file from apache server
if not exists("total_log.txt"):
    print("There was no log file found, searching the internet")
    log = requests.get(url)
    with open("total_log.txt", 'wb') as out:
        out.write(log.content)
    print("we got the log from the internet")
else:
    print("there was already a log on your local machine")

total_log = open("total_log.txt", 'r')

# How many requests were made on each day?



# How many requests were made on a week-by-week basis?



# Per month?



# What percentage of the requests were not successful (any 4xx status code)?



# What percentage of the requests were redirected elsewhere (any 3xx codes)?



# What was the most-requested file?



# What was the least-requested file?



# split total log into by month log files

# for line in total_log:
#     month = re.findall('/.../', str(line))
#     month = str(month) + ".txt"
#     with open(month, 'w') as month_file:
#         month_file.write(line)
#     print(month)
