# Election_Analysis

## Project Overview
A Colorado Board of Elections employee tasked me with the following activities to complete an analysis of the election results concerning a recent, local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received the votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.66.0

## Summary
Conclusive results are as follows:
1. Total votes cast:  369,711 
2. Candidates:
      - Charles Casper
      - Diana DeGette
      - Raymon Anthony Doane
3/4. Candidate Results:
      - Charles Casper received 85,213 votes at 23.05% of total votes.
      - Diana DeGette received 272,892 votes at 73.81% of total votes.
      - Raymon Anthony Doane received 11,606 votes at 3.14% of total votes.
5. The winner of the election was:
      - Diana DeGette who received 272,892 votes at 73.81% of total votes.


## Challenge Overview
Furthermore, the following tasks were amended to the original project to determine tally results for county turnout.

1. Get a complete list of counties who participated in the election.
2. Determine the voter turnout for each county.
3. Calculate the percentage of votes from each county from the total count.
4. Express the county with the highest turnout.

## Challenge Summary
1. Counties:
      - Jefferson
      - Denver
      - Arapahoe
2/3. County count results:
      - Jefferson County received 38,855 votes with 10.5% of the total votes.
      - Denver County received 306,055 votes with 82.8% of the total votes.
      - Arapahoe County received 24,801 votes with 6.7% of the total votes.
4. The county with the largest turnout was:
      - Denver

In summary, we have successfully coded a program to read the election_results.csv file and create/write an output file as election_analysis.txt where we stored the results.  This script can be further ammended to apply to other files containing a similar data structure.  * *First*, it must be a csv file because that is the module we imported and file type we read.  However, if we want to use an alternative file type, we should look into modifications that would suit this purpose.  * *Secondly*, the data structure of the csv file should be similar to this file. * *Thirdly*, if you use a file with rows containing a different ordering of the candidates and counties, you must modify the code for indexing in the for loop file in the reader to match the list items in the new file. * *Next*, you would need to consider if there is a header in the new data and determine whether or not the first row needs to be skipped.  If no header exists, you must remove line 38 where we next() the header line of our reader.  * *Lastly*, of course, you would need to change the path for the file_to_load variable so that it matches the file path of the local computer.  
