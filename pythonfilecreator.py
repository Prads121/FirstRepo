#This script can create text files
import os

def create():
    fname = input("Enter the name of the text file (with .txt extension): ")
    if not fname.endswith(".txt"):
        fname += ".txt"
    
    if os.path.exists(fname):
        print(f"Warning: '{fname}' already exists! It will not be modified.")
    else:
        with open(fname, "x") as file:
            print(f"File '{fname}' has been created successfully!")
    

def main():
    while True:
        print("\nOptions:")
        print("1. Create text file")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            create()
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
