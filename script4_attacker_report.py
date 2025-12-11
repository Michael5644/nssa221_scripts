#!/usr/bin/python3
# Name: Michael Chen
# Date: 10/31/2025
# Script Assignment #4
# This script analyzes the system log files, and reports IPs with 10 or more failed attempts, including their country.

from geoip import geolite2
import os
import re
from datetime import datetime

# Clears the terminal
os.system('clear')

# Path to the syslog file
log_file = "/home/student/syslog.log"

# Tracks the failed attempts per IP using a dictionary
ip_counts = {}

# Regex pattern to find IP addresses
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# Opens the log file and reads it line by line
with open(log_file, 'r') as file:
    for line in file:
        if "Failed password" in line:
            match = ip_pattern.search(line)
	
            if match:
                ip = match.group()
				
		# Count how many times each IP appears
                if ip in ip_counts:
                    ip_counts[ip] = ip_counts[ip] + 1
					
                else:
                    ip_counts[ip] = 1

# Filters out the IPs that has 10 or more failed attempts
attackers = {}

for ip in ip_counts:
    if ip_counts[ip] >= 10:
        attackers[ip] = ip_counts[ip]
		
# A simple function to help with sorting by count (ascending)
def sort_by_count(item):
    return item[1]
	
# Sorts the attackers by turning the dictionary to tuples, then sort
sorted_attackers = sorted(attackers.items(), key=sort_by_count)

# Code responsible for the header layout
print("=" * 40)
print("Attacker Report -", datetime.now().strftime("%B %d, %Y"))
print()
print(f"{'COUNT':<10}{'IP ADDRESS':<20}{'COUNTRY'}")

# Finds the country of origin for each IP
for ip, count in sorted_attackers:
    match = geolite2.lookup(ip)
	
    if match is not None and match.country is not None:
        country = match.country
	
    else:
        country = "Unknown"

    print(f"{count:<10}{ip:<20}{country}")

print("=" * 40)
print("Report Complete.")
