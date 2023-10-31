import os
import pandas as pd

def remove_rows_from_csv():
    # Read the file remove.txt to get the keywords to remove
    with open('remove.txt', 'r') as f:
        remove_keywords = [line.strip().lower() for line in f.read().splitlines()]

    # Identify the CSV file in the directory (assuming there's only one CSV file)
    csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
    if not csv_files:
        print("No CSV file found.")
        return
    elif len(csv_files) > 1:
        print("Multiple CSV files found. Using the first file.")
        csv_file = csv_files[0]
    else:
        csv_file = csv_files[0]

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Normalize the column "Keyword"
    df['Keyword_normalized'] = df['Keyword'].str.strip().str.lower()

    # Find the number of keywords matching the ones in remove.txt
    matching_keywords = df[df['Keyword_normalized'].apply(lambda x: any(keyword in x for keyword in remove_keywords))]
    num_matching_keywords = len(matching_keywords)
    print(f"{num_matching_keywords} keywords match the list in remove.txt.")

    # Confirm before removing rows
    confirm = input("Do you want to continue and remove these rows? (Yes/No): ")
    if confirm.lower() != 'yes':
        print("Operation canceled.")
        return

    # Remove rows containing the keywords
    initial_rows = len(df)
    df_filtered = df[~df['Keyword_normalized'].apply(lambda x: any(keyword in x for keyword in remove_keywords))]
    final_rows = len(df_filtered)

    # Number of rows removed
    rows_removed = initial_rows - final_rows
    print(f"{rows_removed} rows have been removed.")

    # Drop the 'Keyword_normalized' column and save the new CSV, replacing the original file
    df_filtered = df_filtered.drop(columns=['Keyword_normalized'])
    df_filtered.to_csv(csv_file, index=False)
    print(f"The original CSV file has been replaced by the filtered file.")

if __name__ == "__main__":
    remove_rows_from_csv()
