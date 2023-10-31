
# Remove Rows from CSV based on Keywords 📜❌

This script provides functionality to remove specific rows from a CSV file based on keywords specified in a `remove.txt` file.

## Features 🌟

- Automatically detects a CSV file in the current directory.
- Reads keywords from `remove.txt` to filter out rows.
- Provides a confirmation prompt before removing rows.
- Updates the original CSV file with the filtered content.

## How to Use 🚀

1. Ensure that you have only one CSV file in the current directory that you want to process.
2. Create a `remove.txt` file in the same directory and populate it with keywords, one on each line. These keywords are used to match against a column named "Keyword" in the CSV file.
3. Run the script:
    
    Copy code
    
    `python script_name.py`
    
4. The script will provide feedback about how many rows match the keywords from `remove.txt` and ask for confirmation to proceed.
5. If you confirm, the script will remove those rows and update the original CSV file.

## Dependencies 📦

- `os` (Standard Library)
- `pandas` (`pip install pandas`)

## Important Notes 📝

- This script assumes that the CSV has a column named "Keyword".
- If there are multiple CSV files in the directory, the script will choose the first one.
- It's always a good idea to backup your CSV file before using this script.

## Contributing 🤝

Feel free to fork this repository, make changes, and submit pull requests. Any feedback is welcome!