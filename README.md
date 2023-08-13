This is a simple project proposed by a Google course on Coursera: Using Python to interact with the operating system

Introduction to the problem:
Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it

My script parses a log file with regular expressions and creates two csv files:

1 - The errors names and how many times they appear ordered by the most often to the least 

2 - The usernames and how many INFO and ERROR logs they generated in the ticky system ordered by the username

To execute the script, give it the proper permissions:

chmod +x main.sh

Then execute the file:

./main.sh