# Dynamic-IP-Change-Logger
A script to check a router's public facing IP address every 30 minutes to discover what time and how often the IP changes.
The user can dictate how long the program will run in hours and how often it will check. i.e. ">python IPChecker.py 48 0.25" will run for 48 hours and check every 15 minutes.
Upon every check the program will log to a file only if there has been a change of the public IP address or if the internet can't be connected to. The times will be declared for both the scenarios.
ip.42.pl/short is used to return the user's IP address.
The time between IP changes is logged at the end of the file.
