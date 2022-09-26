# This is our project 3 script that will preform the tasks required in the lab
import collections
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

day_regex = '(\d+/.../\d+)'

with open("total_log.txt") as log_file:
    lines = []
    for line in log_file:
        lines.append(line)


# How many requests were made on a week-by-week basis?


# Per month?


# What percentage of the requests were not successful (any 4xx status code)?


# What percentage of the requests were redirected elsewhere (any 3xx codes)?


# What was the most-requested file? # What was the least-requested file?
def most_least_req():
    lines = ""
    for line in total_log:
        lines = lines + line
    arg = re.findall("GET(.+)HTTP", str(lines))
    count = collections.Counter(arg)
    max_value = 0
    max_element = 0
    min_element = 0

    for element in list(count.keys()):
        if count[element] >= max_value:
            max_value = count[element]
            max_element = element

        if count[element] == 1:
            min_element = element

    print(max_element, "is the most requested file")
    print(min_element, "is the least requested file")


# split total log into by month log files
def split_log():
    # create empty list for storing each month
    lines = []
    # This variable lets us know if the new line from the log file has changed months
    month_check = "Oct"

    # for loop runs through each line of log file
    for line in total_log:
        # uses regex to look for the pattern where the month is located
        month = str(re.findall('/(...)/', str(line)))
        # formatting so it is only Oct or whatever month it is, regex makes it ['Oct']
        month = month[2:5]
        # ensuring we don't run into function compatibility issues
        line = str(line)

        # Checks if month was updated, if it was, we know the month changed and we need to dump what we have
        if month != month_check:
            with open("Split_Files/" + month_check + ".txt", 'a+') as month_file:
                # writes what was stored in lines and empties lines for next month
                month_file.writelines(lines)
                lines = []
            month_file.close()

        # These happen after we check if month changed so that we don't have some months seeping into wrong files
        lines.append(line)
        month_check = month

    return "Logs are now split and located in the Split_Files directory"

most_least_req()
split_log()