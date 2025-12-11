#!/usr/bin/python3
# Name: Michael Chen
# Date: 10/1/2025
# Script Assignment #3
# This script helps a user create, delete and manage symbolic links in Linux using Python.

import os
import pathlib
import sys

# Clears the terminal when this script runs
def clear_screen():
	os.system("clear")

# Returns the current user's desktop path without hardcoding it
def get_desktop_path():
	return pathlib.Path.home() / "Desktop"

# This function creates a symbolic link (Option 1)
def create_symbolic_link():
	print("\n---- Create a Symbolic Link ----")
	file_name = input("Enter the file name or the absolute path of the file you want to link: ").strip()
	
	# If the user provided an absolute path to the file, use it
	if os.path.isabs(file_name):
		src = pathlib.Path(file_name)
	
	else:
		# If the user only gives a file name and not the absolute path, assume it's in the current working directory
		src = pathlib.Path(os.getcwd()) / file_name

	# Checks if the specified file exists
	if not src.exists():
		print("Error: The file does not exist. Please check the file name carefully and try again.\n")
		return

	desktop = get_desktop_path()
	link_path = desktop / src.name

	# Checks if the link already exists
	if link_path.exists():
		print("Error: A file/link with the same name already exists.\n")
		return

	try:
		os.symlink(src, link_path)
		print(f"Successfully created symbolic link on the Desktop: {link_path}\n")

	except Exception as e:
		print(f"Error: Could not create the symbolic link. ({e})\n")

# This function deletes a specified symbolic link (Option 2)
def delete_symbolic_link():
	print("\n---- Delete a Symbolic Link ----")
	desktop = get_desktop_path()
	link_name = input("Enter the file name or the absolute path of the symbolic link to delete: ").strip()
	
	# If the the user provided an absolute path to the file, use it
	if os.path.isabs(link_name):
		link_path = pathlib.Path(link_name)
	
	else:
		# If the user only types a file name and not an absolute path, assume the file is in the Desktop directory
		link_path = desktop / link_name

	# Checks if the link exists and if it is a symbolic link
	if not link_path.exists():
		print("Error: That link does not exist.\n")
		return

	if not link_path.is_symlink():
		print("Error: That file is not a symbolic link.\n")
		return

	try:
		link_path.unlink()
		print("Symbolic link deleted successfully.\n")
	
	except Exception as e:
		print("Error with deleting the symbolic link:", e, "\n")


# This function generates a symbolic link report (Option 3)
def generate_report():
	print("\n---- Symbolic Link Report ----")
	home = pathlib.Path.home()
	total_links = 0

	# Looks through the system for symbolic links
	for path in home.rglob("*"):
		if path.is_symlink():
			try:
				target = os.readlink(path)
				print("Symbolic Link:", path, " | ", "Target Path:", target)
				total_links += 1
			
			except Exception:
				pass

	if total_links == 0:
		print("No symbolic links found.\n")
	
	else:
		print("\nTotal symbolic links found:", total_links, "\n")


# Code responsible for the main menu
def main():
	clear_screen()
	print("------- Symbolic Link Creator -------")
	print("------- Your current working directory is:", os.getcwd())
	
	while True:
		print("Menu Options:")
		print("[1] Create a symbolic link")
		print("[2] Delete a symbolic link")
		print("[3] Generate a symbolic link report")
		print("[4] Quit")

		choice = input("\nEnter your choice (1-3) or type 'quit' or '4' to exit the menu: ").strip().lower()
	
		if choice == "1":
			clear_screen()
			create_symbolic_link()
	
		elif choice == "2":
			clear_screen()
			delete_symbolic_link()
	
		elif choice == "3":
			clear_screen()
			generate_report()

		elif choice == "4" or choice == "quit":
			print("Leaving the menu...")
			sys.exit()

		else:
			clear_screen()
			print("Invalid choice, please try again.\n")

if __name__ == "__main__":
	main()
