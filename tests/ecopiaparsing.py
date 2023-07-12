import os
import csv

# Column names we are interested in
columns = ['I[mA]', 'Nb[/cm^3]', 'u[cm^2/Vs]', 'NS[/cm^2]']

# Create a CSV writer
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()

    # Iterate over all files in the current directory
    for filename in os.listdir():
        # Only process .txt files
        if filename.endswith('.txt'):
            # Open each file
            with open(filename, 'r') as file:
                lines = file.readlines()

                # Find the lines with the desired data
                for i in range(len(lines)):
                    if 'I[mA]' in lines[i]:
                        data1_line = lines[i+1].strip().split()

                    if 'Nb[/cm^3]' in lines[i]:
                        data2_line = lines[i+1].strip().split()

                # Map the data to the column names
                data = {
                    'I[mA]': data1_line[0],
                    'Nb[/cm^3]': data2_line[0],
                    'u[cm^2/Vs]': data2_line[1],
                    'NS[/cm^2]': data2_line[6]
                }

                # Write the data to the CSV file
                writer.writerow(data)
