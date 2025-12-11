#!/usr/bin/python3
# Script Assignment 2
# Date: 9/25/2025
# Creator: Michael Chen
# Description: This is a script that gathers and outputs the system information of a host.

import os
import platform
import subprocess

# This function runs a command and returns the result of said command
def run_command(command):
	#subprocess.run executes commands, and by setting capture_output to true, we can collect what the command prints. text=True makes the output will be printed as a string.
	result = subprocess.run(command, shell=True, capture_output=True, text=True)
	
	# Returns the result, stripping it of any leading/trailing whitespaces.
	return result.stdout.strip()

def main():
	# Clears the terminal when starting the script
	os.system("clear")
	
	# Gets the current date from the system	
	date_now = subprocess.getoutput("date '+%B %d, %Y'")
	
	# Grabs the host and domain information from the system
	hostname = platform.node() # Returns hostname
	domain_name = run_command("hostname -d") # Returns the domain name (if applicable)

	# Grabs the network information from the system
	ipv4_address = run_command("hostname -I") # Returns the IPv4 address
	gateway = run_command("ip route | grep default | awk '{print $3}'") # Returns the default gateway
	network_mask = run_command("ifconfig | grep netmask | awk '{print $4}' | head -1")
	dns1 = run_command("grep 'nameserver' /etc/resolv.conf | awk 'NR ==1 {print $2}'")
	dns2 = run_command("grep 'nameserver' /etc/resolv.conf | awk 'NR==2 {print $2}'")
	
	# Grabs the OS information from the system
	os_name = run_command("grep PRETTY_NAME /etc/*release | cut -d '\"' -f2")
	os_version = run_command("grep PRETTY_NAME /etc/*release | cut -d '\"' -f2 | awk '{print $3}'")
	kernel_version = platform.release()

	# Grabs the disk info from the system
	disk_total = run_command("df -h --total | grep total | awk '{print $2}'")
	disk_used = run_command("df -h --total | grep total | awk '{print $3}'")
	disk_free = run_command("df -h --total | grep total | awk '{print $4}'")

	# Grabs the storage information from the system
	cpu_model = run_command("grep 'model name' /proc/cpuinfo | head -1 | cut -d ':' -f2").strip()
	cpu_count = run_command("grep -c '^processor' /proc/cpuinfo") 
	cpu_cores = run_command("grep -c 'cpu cores' /proc/cpuinfo")

	# Grabs the memory information from the system
	ram_total = run_command("free -h | grep Mem | awk '{print $2}'")
	ram_free = run_command("free -h | grep Mem | awk '{print $7}'")

	# Report format:
	report = f"""
========================= System Report - {date_now} =========================

Device Information
Hostname: 				{hostname}
Domain: 				{domain_name}

Network Information
IP Address: 				{ipv4_address}
Gateway: 				{gateway}
Network Mask: 				{network_mask}
DNS1: 					{dns1}
DNS2: 					{dns2}

Operating System Information
Operating System: 			{os_name}
OS Version: 				{os_version}
Kernel Version: 			{kernel_version}

Storage Information
System Drive Total: 			{disk_total}
System Drive Used: 			{disk_used}
System Drive Free: 			{disk_free}

Processor Information
CPU Model: 				{cpu_model}
Number of Processors: 			{cpu_count}
Number of Cores: 			{cpu_cores}

Memory Information
Total RAM: 				{ram_total}
Available RAM: 				{ram_free}

======================================================================================
"""
	
	# Prints it to terminal
	print(report)

	# Saves this report as a logfile in home directory
	logfile = os.path.expanduser(f"~/{hostname}_system_report.log")

	with open(logfile, "w") as f:
		f.write(report)

if __name__ == "__main__":
	main()
