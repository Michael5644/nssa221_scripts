#!/usr/bin/python3
# -------------------------------------------
# ping_test.py
# Student: Michael Chen
# Date: 9/3/2025
#
# Assignment #1
# -------------------------------------------

import os
import subprocess

# This function clears the terminal when it runs
def clear_screen():
    os.system("clear")

# This function dynamically finds the system's default gateway
def get_default_gateway():
    try:     
        result = subprocess.getoutput("ip r") # This line runs the 'ip r' command and captures the output
    
        for line in result.splitlines():
            if line.startswith("default"):
                parts = line.split()
                return parts[2] # The 3rd part (right after 'default via') is the gateway
     
        return None # If the line does not start with default

    except subprocess.CalledProcessError:
        return None

# This function takes a given IP or hostname and pings it 4 times
def ping_target(target):
    try: 
        subprocess.run(["ping","-c", "4", target], check = True) # By using '-c 4' after ping, it allows us to send 4 pings to the target
    
    except subprocess.CalledProcessError:
        print("Ping to the target has failed.") # Lets the user know if the ping fails

# Main program that loops until the user selects '5' to exit.
while True:
    clear_screen()
    print("===== Ping Test Menu =====")
    print("1. Display the default gateway")
    print("2. Test Local Connectivity")
    print("3. Test Remote Connectivity")
    print("4. Test DNS Resolution")
    print("5. Exit/quit the script")
    print("===========================")

    choice = input("Enter your choice: ")
    gateway = get_default_gateway() # Stores it into a variable for easier access for the following commands
    
    if choice == "1":
        print("Default Gateway:", gateway) # Shows the default gateway (Varies between systems)

    elif choice == "2":
        print("Pinging the default gateway: ", gateway)
        ping_target(gateway) # Tests the local connectivity to the gateway

    elif choice == "3":
        print("Pinging RIT's DNS server...")
        ping_target("129.21.3.17") # Tests the remote connectivity to RIT's DNS server

    elif choice == "4":
        print("Pinging www.google.com...")
        ping_target("www.google.com") # Tests the DNS resolution by pinging Google

    elif choice == "5":
        print("Quitting.")
        break # Stops the program entirely when user chooses to quit

    else:
        print("Invalid choice detected. Please pick between 1 to 5 only.")
    
    input("Press enter to continue...")


