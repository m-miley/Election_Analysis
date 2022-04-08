
#Add our Dependencies
import csv
# op sys module for indirect path
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename to save variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")



#Initialize an accumulator variable before opening, set to zero
total_votes = 0
candidate_options = []
candidate_votes = dict()

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file and Perform Analysis
with open(file_to_load) as election_data:

    #Read the file object with the reader function -csv module
    file_reader = csv.reader(election_data)
    #print header row.
    headers = next(file_reader)

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

#Open and Create file to save as txt and write results
with open(file_to_save, "w") as txt_file:
    #Print Header & Print the final vote count to the terminal.
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

        # Determine if the vote count that was calculated is greater than the winning_count.
        # If the vote count is greater than the winning_count and the percentage is greater than the winning_percentage, 
        # set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage.
        # Set the winning_count equal to the variable, candidate_name.
        
        #Determine winning vote count and candidate
            #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true, then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #Save the results to Text File

    winning_candidate_summary = (f"""
---------------------------------
Winner: {winning_candidate}
Winning Vote Count: {winning_count:,} 
Winning Percentage: {winning_percentage:.2f}% 
---------------------------------
""")
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    
    