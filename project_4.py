# This is our project 3 script that will preform the tasks required in the lab
import requests
from os.path import exists

# Set variables for static values, url, dates etc
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

# check for cached log file or pull the log file from apache server
if not exists("project_3_output.txt"):
    log = requests.get(url)
    with open("project_3_output.txt", 'wb') as out:
        out.write(log.content)
    print("we got the log from the internet")
else:
    print("there was already a log on your local machine")

# how many total requests have been made in the last 6 months, output to txt file
with open("project_3_output.txt") as log_file:
    lines = []
    for line in log_file:
        lines.append(line)

start = 0
date = "11/Apr/1995"
for line in lines:
    start += 1
    if date in line:
        break
        
# how many total requests have been made over the entire report, output to txt file
lines_total = len(lines)

# sixMonths is a variable used to count the lines between lines_total and start
sixMonths = lines_total - start + 1

# How many requests were made on each day?

# How many requests were made on a week-by-week basis? Per month?

# What percentage of the requests were not successful (any 4xx status code)?

# What percentage of the requests were redirected elsewhere (any 3xx codes)?

# What was the most-requested file?

# What was the least-requested file?


# output the data from the for loops
print("In the report, there are " + str(lines_total) + " requests total and " + str(sixMonths) + " in the last six months.")
