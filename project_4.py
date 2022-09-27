# This is our project 3 script that will preform the tasks required in the lab
import collections
from pip._vendor import requests
import requests 
from os.path import exists
import os.path
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


# How many requests were made on each day?

# How many requests were made on each day?
def count_days():
    day_regex = '(\d+/.../\d+)'
    day_check = '24/Oct/1994'
    lines = []
    for line in total_log:
        day = str(re.findall(day_regex, str(line)))
        day = day[2:13]

        if day != day_check:
            if len(day) == 0:
                continue
            else:
                print(len(lines), "is the number of requests on", day_check)
                lines = []

        lines.append(line)
        day_check = day
    print(len(lines), "is the number of requests on", day_check)


# How many requests were made on a week-by-week basis?
def count_week():
    day_regex = '(\d+/.../\d+)'
    day_check = '24/Oct/1994'
    week_count = 0
    lines = []
    for line in total_log:
        day = str(re.findall(day_regex, str(line)))
        day = day[2:13]

        if day != day_check:
            if len(day) == 0:
                continue
            elif week_count == 6:
                print(len(lines), "is the number of requests on", day_check)
                lines = []
                week_count = 0
            else:
                week_count += 1

        lines.append(line)
        day_check = day
    print(len(lines), "is the number of requests on", day_check)


# Per month?
def count_month():
    month_regex = '(/.../\d+)'
    month_check = 'Oct/1994'
    lines = []
    for line in total_log:
        month = str(re.findall(month_regex, str(line)))
        month = month[3:11]
        if month != month_check:
            if len(month) == 0:
                continue
            else:
                print(len(lines), "is the number of requests on", month_check)
                lines = []

        lines.append(line)
        month_check = month
    print(len(lines), "is the number of requests on", month_check)


# What percentage of the requests were not successful (any 4xx status code)?
def count4x():
    total_lines = 0
    total_4x = 0
    print("Calculating...")
    for line in total_log:
        stat_code = line.split()[-2]
        if re.match("4\d\d", stat_code):
            total_4x += 1
        total_lines += 1
    percent = total_4x / total_lines * 100
    print(f"Percentage of 4xx Requests: {percent:.2f}%")
        

# What percentage of the requests were redirected elsewhere (any 3xx codes)?

def count_3x():
    total_lines = 0
    total_3x = 0
    print("Calculating...")
    for line in total_log:
        stat_code = line.split()[-2]
        if re.match("3\d\d", stat_code):
            total_3x += 1
        total_lines += 1
    percent = total_3x / total_lines * 100
    print(f"Percentage of 3xx Requests: {percent:.2f}%")

# What was the most-requested file? # What was the least-requested file?
def most_least_req():
    lines = ""
    print("Checking, please wait, this may take about a minute")
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
    if not exists("Split_Files"):
        os.mkdir("Split_Files")
    else:
        return print("There is already an instance of Split_Files, please move or delete and re-run")

    # create empty list for storing each month
    lines = []
    # This variable lets us know if the new line from the log file has changed months
    month_check = "Oct"

    print("Splitting the files now, please wait")
    # for loop runs through each line of log file
    for line in total_log:
        # uses regex to look for the pattern where the month is located
        month = str(re.findall('/(...)/', str(line)))
        # formatting so it is only Oct or whatever month it is, regex makes it ['Oct']
        month = month[2:5]
        # ensuring we don't run into function compatibility issues
        line = str(line)

        # Checks if month was updated, if it was, we know the month changed, and we need to dump what we have
        if month != month_check:
            with open("Split_Files/" + month_check + ".txt", 'a+') as month_file:
                # writes what was stored in lines and empties lines for next month
                month_file.writelines(lines)
                lines = []
                month_file.close()

        # These happen after we check if month changed so that we don't have some months seeping into wrong files
        lines.append(line)
        month_check = month
    with open("Split_Files/" + month_check + ".txt", 'a+') as month_file:
        month_file.writelines(lines)
        month_file.close()

    return print("Logs are now split and located in the Split_Files directory")


menu = """--------------------------------------------


Please enter a number that corresponds with the operation you would like to perform
Requests per day: 1
Requests per week: 2
Requests per month: 3
Most and least requested files: 4
Split the log by month: 5
Percentage of '4xx' requests: 6
Percentage of '3xx' requests: 7

Choice: """

while True:
    total_log = open("total_log.txt", 'r')

    try:
        user_choice = int(input(menu))
    except:
        print("That was not a number!")

        continue
    if user_choice == 1:
        count_days()
    elif user_choice == 2:
        count_week()
    elif user_choice == 3:
        count_month()
    elif user_choice == 4:
        most_least_req()
    elif user_choice == 5:
        split_log()
    elif user_choice == 6:
        count4x()
    elif user_choice == 7:
        count_3x()
    elif user_choice > 7 & user_choice <= 0:
        print("Not a valid entry")

