"""
Task Automation with Python Scripts
------------------------------------
Goal: Move all .jpg / .jpeg image files from a source folder
to a destination folder.

Key Concepts Used: os, shutil, file handling, try-except
"""

# Import the required modules
import os
import shutil


def move_jpg_files():
    """
    Asks the user for a source and destination folder,
    then moves all .jpg and .jpeg files from source to destination.
    """

    # Step 1: Ask the user to enter the source folder path
    source_folder = input("Enter the source folder path: ").strip()

    # Step 2: Ask the user to enter the destination folder path
    destination_folder = input("Enter the destination folder path: ").strip()

    # Step 3: Check whether the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return  # Stop the program if source folder is missing

    # Step 4: Check whether the destination folder exists
    if not os.path.exists(destination_folder):
        print(f"Error: Destination folder '{destination_folder}' does not exist.")
        return  # Stop the program if destination folder is missing

    # Step 5: Get the list of all files in the source folder
    all_files = os.listdir(source_folder)

    # Step 6: Keep a counter to track how many files were moved
    moved_count = 0

    # Step 7: Loop through each file in the source folder
    for file_name in all_files:

        # Step 8: Check if the file ends with .jpg or .jpeg (case-insensitive)
        if file_name.lower().endswith((".jpg", ".jpeg")):

            # Build the full file paths for source and destination
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Step 9: Try to move the file, and handle any errors that occur
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {file_name}")
                moved_count += 1  # Increase the counter after a successful move

            except Exception as error:
                # If something goes wrong (permission issue, file in use, etc.)
                print(f"Could not move '{file_name}'. Reason: {error}")

    # Step 10: Display the final result to the user
    if moved_count == 0:
        print("No .jpg or .jpeg image files were found in the source folder.")
    else:
        print(f"\nTotal files moved: {moved_count}")


# Step 11: Run the function only when this script is executed directly
if __name__ == "__main__":
    move_jpg_files()
