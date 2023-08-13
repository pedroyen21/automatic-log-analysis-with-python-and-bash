#! ./venv/bin/python

import csv
import re

users = {}
errors = {}

with open("syslog.log") as file:
    info_pattern = r"ticky: INFO .*\((.+)\)"
    error_pattern = r"ticky: ERROR (.*) \((.+)\)"

    for line in file.readlines():
        match = re.search(info_pattern, line)
        if match != None:
            if match[1] not in users:
                users[match[1]] = [0,0]
            users[match[1]][0] += 1

        match = re.search(error_pattern, line)
        if match != None: 
            if match[2] not in users:
                users[match[2]] = [0,0]
            users[match[2]][1] += 1
            errors[match[1]] = errors.get(match[1], 0) + 1
    file.close()

users = dict(sorted(users.items()))
errors = dict(sorted(errors.items(), key=lambda error: error[1], reverse=True))

with open("error_message.csv", "w") as file:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for error in errors.items():
        writer.writerow({"Error": error[0], "Count": error[1]})
    file.close()   

with open("user_statistics.csv", "w") as file:
    fieldnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for user in users.items():
        writer.writerow({"Username": user[0], "INFO": user[1][0], "ERROR": user[1][1]})
    file.close()    
