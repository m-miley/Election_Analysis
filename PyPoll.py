# The data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

#READING A FILE
#Add our Dependencies
import csv
# op sys module for indirect path
import os

# Assign a variable for the file to load and the path.
# # file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election results and read the file.
# # election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: perform analaysis.
    #Read the file object with the reader function -csv module
    file_reader = csv.reader(election_data)
    #print each row in the CSV file
    # for row in file_reader:
    #     print(row[0])
    #print header row.
    headers = next(file_reader)
    print(headers)
#     print(election_data)
# Close the file.
# election_data.close()

#WRITING A FILE
#create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# #Using the open() funciton with the "w" mode we will write data to the file.
# open(file_to_save, "w") #this alone results in IO error, output, doesn't exist.
#must create the folder "analysis" in directory before running again. =>creates file

#add text to new "election_analysis.txt"
#Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# #Use the open statement to open the file as a text file.
# # outfile = open(file_to_save, "w")
# with open(file_to_save, "w") as outfile:
# #Write some data to the file.
# # outfile.write("Hello World")
#     outfile.write(f"""Counties in the Election
# --------------------------------------------
# """)
#     outfile.write("Arapahoe\nDenver\nJefferson\n")
# #Close the file
# # outfile.close()
