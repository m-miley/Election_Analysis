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
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Open the election results and read the file.
# # election_data = open(file_to_load, 'r')

#Initialize an accumulator variable before opening, set to zero
total_votes = 0
candidate_options = []
candidate_votes = dict()

with open(file_to_load) as election_data:

    # To do: perform analaysis.
    #Read the file object with the reader function -csv module
    file_reader = csv.reader(election_data)
    #print header row.
    headers = next(file_reader)
    # print(headers)
    #print each row in the CSV file
    for row in file_reader:
        #Increment total_votes by 1
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate, add to list
        if candidate_name not in candidate_options:
            #1. Add candidate name to candidate list
            candidate_options.append(candidate_name)  
            #2. Create key for candidate in dict and initialize value to 0 to track vote count
            candidate_votes[candidate_name] = 0
        #Increment the candidate's vote count value by 1
        candidate_votes[candidate_name] += 1
        # print(row[0])

# Determine the percentage of votes for each candidate by looping through the counts. -module way
# 1. Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate_name}: received {vote_percentage}% of the vote.")

#-my way
for k, v in candidate_votes.items():
    vote_percentage = v/total_votes*100
    print(f"Candidate {k} had {v:,} number of votes and {vote_percentage:.2f}% of the total votes")
print(f"Total number of votes were: {total_votes:,}")

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
