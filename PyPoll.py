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

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
       
with open(file_to_save, "w") as txt_file:
    #Print Header,#Print the final vote count to the terminal.
    election_results = (f"""
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
""")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    #Print each candidate, their voter count, and percentage to the terminal
    # Determine the percentage of votes for each candidate by looping through the counts. -module way
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.2f}% ({votes:,}).\n")
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

    #-my way
        # for k, v in candidate_votes.items():
        # vote_percentage = v/total_votes*100
        # print(f"Candidate {k} had {v:,} number of votes and {vote_percentage:.2f}% of the total votes")
        # print(f"Total number of votes were: {total_votes:,}")

        #     Next, we will create an if statement inside the for loop and do the following:

        # Determine if the vote count that was calculated is greater than the winning_count.
        # If the vote count is greater than the winning_count and the percentage is greater than the winning_percentage, set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage.
        # Set the winning_count equal to the variable, candidate_name, in the for loop.
        
        #Determine winning vote count and candidate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true, then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #Save the results to our Text File

    winning_candidate_summary = (f"""
---------------------------------
And the winner is!..... {winning_candidate}
Winning Vote Count: {winning_count:,} 
Winning Percentage: {winning_percentage:.2f}% 
---------------------------------
""")
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    # print(winning_candidate_summary)
            
    #Use if to check if first vote count for candidate is greater than zero
    #If true, then vote counte will be equal to "winning count"
    #candidates percentage of vote equal to "winning percentage"
    #then select candidate as "winning candidate from candidate_options list

    #Delcare a variable that holds an empty string value for the winning candidate
    #Declare a variable for the "winning count" equal to zero
    #Declare a variable for the "winning percentage" equal to zero
    #All before "With statement" opening

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


